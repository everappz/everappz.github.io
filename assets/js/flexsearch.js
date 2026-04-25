// Search functionality using FlexSearch.

// Change shortcut key to cmd+k on Mac, iPad or iPhone.
document.addEventListener("DOMContentLoaded", function () {
  if (/iPad|iPhone|Macintosh/.test(navigator.userAgent)) {
    // select the kbd element under the .hextra-search-wrapper class
    const keys = document.querySelectorAll(".hextra-search-wrapper kbd");
    keys.forEach(key => {
      key.innerHTML = '<span class="hx:text-xs">⌘</span>K';
    });
  }
});

// Render the search data as JSON.
// {{ $searchDataFile := printf "%s.search-data.json" .Language.Lang }}
// {{ $searchData := resources.Get "json/search-data.json" | resources.ExecuteAsTemplate $searchDataFile . }}
// {{ if hugo.IsProduction }}
//   {{ $searchData := $searchData | minify | fingerprint }}
// {{ end }}
// {{ $noResultsFound := (T "noResultsFound") | default "No results found." }}
// {{ $readMore := (T "readMore") | default "Read more" }}

(function () {
  const searchDataURL = '{{ $searchData.RelPermalink }}';

  const inputElements = document.querySelectorAll('.hextra-search-input');
  for (const el of inputElements) {
    el.addEventListener('focus', init);
    el.addEventListener('keyup', search);
    el.addEventListener('keydown', handleKeyDown);
    el.addEventListener('input', handleInputChange);
  }

  // Restore search results after back-navigation (bfcache)
  window.addEventListener('pageshow', function (e) {
    if (e.persisted) {
      for (const el of inputElements) {
        if (el.value) {
          el.dispatchEvent(new Event('focus'));
          el.dispatchEvent(new KeyboardEvent('keyup'));
        }
      }
    }
  });

  const shortcutElements = document.querySelectorAll('.hextra-search-wrapper kbd');

  function setShortcutElementsOpacity(opacity) {
    shortcutElements.forEach(el => {
      el.style.opacity = opacity;
    });
  }

  function handleInputChange(e) {
    const opacity = e.target.value.length > 0 ? 0 : 100;
    setShortcutElementsOpacity(opacity);
  }

  // Get the search wrapper, input, and results elements.
  function getActiveSearchElement() {
    const inputs = Array.from(document.querySelectorAll('.hextra-search-wrapper')).filter(el => el.clientHeight > 0);
    if (inputs.length === 1) {
      return {
        wrapper: inputs[0],
        inputElement: inputs[0].querySelector('.hextra-search-input'),
        resultsElement: inputs[0].querySelector('.hextra-search-results')
      };
    }
    return undefined;
  }

  const INPUTS = ['input', 'select', 'button', 'textarea']

  // Focus the search input when pressing ctrl+k/cmd+k or /.
  document.addEventListener('keydown', function (e) {
    const { inputElement } = getActiveSearchElement();
    if (!inputElement) return;

    const activeElement = document.activeElement;
    const tagName = activeElement && activeElement.tagName;
    if (
      inputElement === activeElement ||
      !tagName ||
      INPUTS.includes(tagName) ||
      (activeElement && activeElement.isContentEditable))
      return;

    if (
      e.key === '/' ||
      (e.key === 'k' &&
        (e.metaKey /* for Mac */ || /* for non-Mac */ e.ctrlKey))
    ) {
      e.preventDefault();
      inputElement.focus();
    } else if (e.key === 'Escape' && inputElement.value) {
      inputElement.blur();
    }
  });

  // Dismiss the search results when clicking outside the search box.
  document.addEventListener('mousedown', function (e) {
    const { inputElement, resultsElement } = getActiveSearchElement();
    if (!inputElement || !resultsElement) return;
    if (
      e.target !== inputElement &&
      e.target !== resultsElement &&
      !resultsElement.contains(e.target)
    ) {
      setShortcutElementsOpacity(100);
      hideSearchResults();
    }
  });

  // Get the currently active result and its index.
  function getActiveResult() {
    const { resultsElement } = getActiveSearchElement();
    if (!resultsElement) return { result: undefined, index: -1 };

    const result = resultsElement.querySelector('.hextra-search-active');
    if (!result) return { result: undefined, index: -1 };

    const index = parseInt(result.dataset.index, 10);
    return { result, index };
  }

  // Set the active result by index.
  function setActiveResult(index) {
    const { resultsElement } = getActiveSearchElement();
    if (!resultsElement) return;

    const { result: activeResult } = getActiveResult();
    activeResult && activeResult.classList.remove('hextra-search-active');
    const result = resultsElement.querySelector(`[data-index="${index}"]`);
    if (result) {
      result.classList.add('hextra-search-active');
      result.focus();
    }
  }

  // Get the number of search results from the DOM.
  function getResultsLength() {
    const { resultsElement } = getActiveSearchElement();
    if (!resultsElement) return 0;
    return resultsElement.dataset.count;
  }

  // Finish the search by hiding the results and clearing the input.
  function finishSearch() {
    const { inputElement } = getActiveSearchElement();
    if (!inputElement) return;
    hideSearchResults();
    inputElement.value = '';
    inputElement.blur();
  }

  function hideSearchResults() {
    const { resultsElement } = getActiveSearchElement();
    if (!resultsElement) return;
    resultsElement.classList.add('hx:hidden');
  }

  // Handle keyboard events.
  function handleKeyDown(e) {
    const { inputElement } = getActiveSearchElement();
    if (!inputElement) return;

    const resultsLength = getResultsLength();
    const { result: activeResult, index: activeIndex } = getActiveResult();

    switch (e.key) {
      case 'ArrowUp':
        e.preventDefault();
        if (activeIndex > 0) setActiveResult(activeIndex - 1);
        break;
      case 'ArrowDown':
        e.preventDefault();
        if (activeIndex + 1 < resultsLength) setActiveResult(activeIndex + 1);
        break;
      case 'Enter':
        e.preventDefault();
        if (activeResult) {
          activeResult.click();
        }
        finishSearch();
      case 'Escape':
        e.preventDefault();
        hideSearchResults();
        // Clear the input when pressing escape
        inputElement.value = '';
        inputElement.dispatchEvent(new Event('input'));
        // Remove focus from the input
        inputElement.blur();
        break;
    }
  }

  // Initializes the search.
  function init(e) {
    e.target.removeEventListener('focus', init);
    if (!(window.pageIndex && window.sectionIndex)) {
      preloadIndex();
    }
  }

  /**
   * Preloads the search index by fetching data and adding it to the FlexSearch index.
   * @returns {Promise<void>} A promise that resolves when the index is preloaded.
   */
  async function preloadIndex() {
    const tokenize = '{{- site.Params.search.flexsearch.tokenize | default  "forward" -}}';

    // https://github.com/TryGhost/Ghost/pull/21148
    const regex = new RegExp(
      `[\u{4E00}-\u{9FFF}\u{3040}-\u{309F}\u{30A0}-\u{30FF}\u{AC00}-\u{D7A3}\u{3400}-\u{4DBF}\u{20000}-\u{2A6DF}\u{2A700}-\u{2B73F}\u{2B740}-\u{2B81F}\u{2B820}-\u{2CEAF}\u{2CEB0}-\u{2EBEF}\u{30000}-\u{3134F}\u{31350}-\u{323AF}\u{2EBF0}-\u{2EE5F}\u{F900}-\u{FAFF}\u{2F800}-\u{2FA1F}]|[0-9A-Za-zа-я\u00C0-\u017F\u0400-\u04FF\u0600-\u06FF\u0980-\u09FF\u1E00-\u1EFF\u0590-\u05FF]+`,
      'mug'
    );
    const encode = (str) => { return ('' + str).toLowerCase().match(regex) ?? []; }

    window.pageIndex = new FlexSearch.Document({
      tokenize,
      encode,
      cache: 100,
      document: {
        id: 'id',
        store: ['title', 'content', 'url', 'display', 'crumb'],
        index: "content"
      }
    });

    window.sectionIndex = new FlexSearch.Document({
      tokenize,
      encode,
      cache: 100,
      document: {
        id: 'id',
        store: ['title', 'content', 'url', 'display', 'crumb'],
        index: "content",
        tag: [{
          field: "pageId"
        }]
      }
    });

    const resp = await fetch(searchDataURL);
    const data = await resp.json();
    let pageId = 0;
    for (const route in data) {
      let pageContent = '';
      ++pageId;
      const urlParts = route.split('/').filter(x => x != "" && !x.startsWith('#'));

      let crumb = '';
      let searchUrl = '/';
      for (let i = 0; i < urlParts.length; i++) {
        const urlPart = urlParts[i];
        searchUrl += urlPart + '/'

        const crumbData = data[searchUrl];
        if (!crumbData) {
          console.warn('Excluded page', searchUrl, '- will not be included for search result breadcrumb for', route);
          continue;
        }

        let title = data[searchUrl].title;
        if (title == "_index") {
          title = urlPart.split("-").map(x => x).join(" ");
        }
        crumb += title;

        if (i < urlParts.length - 1) {
          crumb += ' > ';
        }
      }

      for (const heading in data[route].data) {
        const [hash, text] = heading.split('#');
        const url = route.trimEnd('/') + (hash ? '#' + hash : '');
        const title = text || data[route].title;

        const content = data[route].data[heading] || '';
        const paragraphs = content.split('\n').filter(Boolean);

        sectionIndex.add({
          id: url,
          url,
          title,
          crumb,
          pageId: `page_${pageId}`,
          content: title,
          ...(paragraphs[0] && { display: paragraphs[0] })
        });

        for (let i = 0; i < paragraphs.length; i++) {
          sectionIndex.add({
            id: `${url}_${i}`,
            url,
            title,
            crumb,
            pageId: `page_${pageId}`,
            content: paragraphs[i]
          });
        }

        pageContent += ` ${title} ${content}`;
      }

      const url = route.trimEnd('/') + '';

      window.pageIndex.add({
        id: pageId,
        url,
        title: data[route].title,
        crumb,
        content: pageContent
      });

    }
  }

  /**
   * Strips question words and detects intent to improve FlexSearch matching.
   */
  function preprocessQuery(raw) {
    const trimmed = raw.trim();
    if (trimmed.length < 2) return { original: trimmed, cleaned: trimmed, intent: null, isQuestion: false };

    const lower = trimmed.toLowerCase();
    const questionPatterns = [
      { regex: /^how\s+(do|can|to|does|did|should|would|is|are)\s+/i, intent: 'howto' },
      { regex: /^what\s+(is|are|was|were|does|do)\s+/i, intent: 'definition' },
      { regex: /^(can|could|is|are|does|do|will|would|should|has|have|did)\s+/i, intent: 'yesno' },
      { regex: /^(where|when|which|who|why)\s+/i, intent: 'factoid' },
      { regex: /^how\s+/i, intent: 'howto' }
    ];

    for (const { regex, intent } of questionPatterns) {
      if (regex.test(trimmed)) {
        let cleaned = trimmed.replace(regex, '').replace(/\?+$/, '').trim();
        if (!cleaned) cleaned = trimmed.replace(/\?+$/, '').trim();
        return { original: trimmed, cleaned, intent, isQuestion: true };
      }
    }

    if (trimmed.endsWith('?')) {
      const cleaned = trimmed.replace(/\?+$/, '').trim();
      return { original: trimmed, cleaned, intent: 'general', isQuestion: true };
    }

    return { original: trimmed, cleaned: trimmed, intent: null, isQuestion: false };
  }

  /**
   * Re-ranks FlexSearch results by query term overlap and content signals.
   */
  function rerankResults(results, queryInfo) {
    const terms = queryInfo.cleaned.toLowerCase().split(/\s+/).filter(t => t.length > 1);
    if (!terms.length) return results;

    for (const r of results) {
      let score = 0;
      const title = (r.children.title || '').toLowerCase();
      const content = (r.children.content || '').toLowerCase();
      const route = (r.route || '').toLowerCase();

      let titleHits = 0, contentHits = 0;
      for (const term of terms) {
        if (title.includes(term)) { score += 3; titleHits++; }
        if (content.includes(term)) { score += 2; contentHits++; }
      }

      // All terms present bonus
      if (titleHits === terms.length) score += 10;
      if (contentHits === terms.length) score += 10;

      // Exact phrase match bonus
      const phrase = queryInfo.cleaned.toLowerCase();
      if (title.includes(phrase)) score += 20;
      if (content.includes(phrase)) score += 15;

      // Section priority boost (higher = more important)
      if (route.includes('/docs/howto/')) score += 12;
      else if (route.includes('/docs/guide/')) score += 10;
      else if (route.includes('/docs/faq/')) score += 8;
      else if (route.includes('/blog/')) score += 6;
      else if (route.includes('/products/')) score += 4;

      // Content-type boost based on intent
      if (queryInfo.intent === 'howto' && (route.includes('/howto/') || route.includes('/how-to/'))) score += 5;
      if (queryInfo.intent === 'definition' && (route.includes('/faq/') || route.includes('/docs/'))) score += 5;

      // Content length quality signal
      const len = content.length;
      if (len >= 50 && len <= 600) score += 3;
      else if (len > 600) score += 1;

      r._smartScore = score;
    }

    results.sort((a, b) => b._smartScore - a._smartScore);
    return results;
  }

  /**
   * Extracts answer snippets from top re-ranked results (up to 3 answer cards).
   */
  function extractAnswers(results, queryInfo) {
    if (!queryInfo.isQuestion || !results.length) return [];

    const answers = [];
    const seenUrls = new Set();
    const terms = queryInfo.cleaned.toLowerCase().split(/\s+/).filter(t => t.length > 1);

    for (const r of results) {
      if (answers.length >= 3) break;
      if (!r._smartScore || r._smartScore < 8) continue;

      const content = r.children.content || '';
      if (!content || seenUrls.has(r.route)) continue;
      seenUrls.add(r.route);

      let text;
      if (content.length <= 300) {
        text = content;
      } else {
        const sentences = content.split(/(?<=[.!?])\s+/).filter(s => s.length > 15);
        if (!sentences.length) {
          text = content.slice(0, 300);
        } else {
          const scored = sentences.map((s, i) => {
            const lower = s.toLowerCase();
            let sc = 0;
            for (const t of terms) { if (lower.includes(t)) sc += 3; }
            if (i === 0) sc += 2;
            return { text: s, score: sc };
          });
          scored.sort((a, b) => b.score - a.score);
          const best = scored.slice(0, 3).filter(s => s.score > 0);
          if (!best.length) {
            text = sentences[0];
          } else {
            const selected = best.map(b => b.text);
            text = sentences.filter(s => selected.includes(s)).join(' ');
          }
        }
      }

      answers.push({ text, source: r.children.title, url: r.route, prefix: r.prefix });
    }

    return answers;
  }

  /**
   * Performs a search based on the provided query and displays the results.
   * @param {Event} e - The event object.
   */
  function search(e) {
    const rawQuery = e.target.value;
    if (!rawQuery) {
      hideSearchResults();
      return;
    }

    const { resultsElement } = getActiveSearchElement();
    while (resultsElement.firstChild) {
      resultsElement.removeChild(resultsElement.firstChild);
    }
    resultsElement.classList.remove('hx:hidden');

    const queryInfo = preprocessQuery(rawQuery);
    const query = rawQuery;

    // Search with both original and cleaned queries, merge results
    const pageResults = window.pageIndex.search(query, 5, { enrich: true, suggest: true })[0]?.result || [];
    if (queryInfo.isQuestion && queryInfo.cleaned !== query) {
      const cleanedPageResults = window.pageIndex.search(queryInfo.cleaned, 5, { enrich: true, suggest: true })[0]?.result || [];
      const existingIds = new Set(pageResults.map(r => r.id));
      for (const r of cleanedPageResults) {
        if (!existingIds.has(r.id)) pageResults.push(r);
      }
    }
    // console.debug(`[Search] Found ${pageResults.length} pageResults`);

    const results = [];
    const pageTitleMatches = {};
    const occurred = {}; // Shared deduplication map

    // === 1. Primary: per-page scoped section search ===
    for (let i = 0; i < pageResults.length; i++) {
      const result = pageResults[i];
      pageTitleMatches[i] = 0;

      // Show the top 5 results for each page
      const sectionResults = window.sectionIndex.search(query, 5, { enrich: true, suggest: true, tag: { 'pageId': `page_${result.id}` } })[0]?.result || [];
      // console.debug(`[Search] Page[${i}] "${result.doc.title}" has ${sectionResults.length} sectionResults`);

      let isFirstItemOfPage = true

      // fallback: add page-level result manually
      if (sectionResults.length === 0) {
        const { id, url, title, crumb, content} = result.doc;
        results.push({
          _page_rk: i,
          _section_rk: 0,
          route: url,
          prefix: crumb,
          children: { title, content }
        });
        // console.debug(`[Search] Fallback: added page "${title}" url "${url}" to results`);
        continue;
      }

      for (let j = 0; j < sectionResults.length; j++) {
        const { doc } = sectionResults[j]
        const isMatchingTitle = doc.display !== undefined
        if (isMatchingTitle) {
          pageTitleMatches[i]++
        }
        const { url, title } = doc
        const content = doc.display || doc.content

        if (occurred[url + '@' + content]) continue
        occurred[url + '@' + content] = true
        results.push({
          _page_rk: i,
          _section_rk: j,
          route: url,
          prefix: isFirstItemOfPage ? result.doc.crumb : undefined,
          children: { title, content }
        })
        isFirstItemOfPage = false
      }
    }

    // === 2. Secondary: global section search (outside top pages) ===
    const globalSections = window.sectionIndex.search(query, 10, {
      enrich: true,
      suggest: true
    })[0]?.result || [];

    // console.debug(`[Search] Global sectionIndex search found ${globalSections.length} results`);

    for (let j = 0; j < globalSections.length; j++) {
      const { doc } = globalSections[j];
      const { url, title, content, crumb } = doc;
      const display = doc.display || content;

      if (occurred[url + '@' + display]) continue;
      occurred[url + '@' + display] = true;

      results.push({
        _page_rk: 999, // rank later
        _section_rk: j + 1000,
        route: url,
        prefix: crumb,
        children: { title, content: display }
      });
    }

    // console.debug(`[Search] Total deduplicated results before sorting: ${results.length}`);

    const sortedResults = results
      .sort((a, b) => {
        // Custom boost for /docs folder
        const aIsDocs = a.route.includes('/docs/');
        const bIsDocs = b.route.includes('/docs/');
        if (aIsDocs !== bIsDocs) {
          return bIsDocs - aIsDocs; // true > false => sort /docs/ on top
        }

        // Sort by number of matches in the title.
        if (a._page_rk === b._page_rk) {
          return a._section_rk - b._section_rk;
        }
        if (pageTitleMatches[a._page_rk] !== pageTitleMatches[b._page_rk]) {
          return (pageTitleMatches[b._page_rk] || 0) - (pageTitleMatches[a._page_rk] || 0);
        }
        return a._page_rk - b._page_rk;
      })
      .map(res => ({
        id: `${res._page_rk}_${res._section_rk}`,
        route: res.route,
        prefix: res.prefix,
        children: res.children
      }));

    // console.debug(`[Search] Final sortedResults ready to render:`, sortedResults);

    // Smart re-ranking and answer extraction for question queries
    if (queryInfo.isQuestion) {
      rerankResults(sortedResults, queryInfo);
    }
    const answers = extractAnswers(sortedResults, queryInfo);

    displayResults(sortedResults, query, answers);
  }

  /**
   * Displays the search results on the page.
   *
   * @param {Array} results - The array of search results.
   * @param {string} query - The search query.
   */
  function displayResults(results, query, answers) {
    const { resultsElement } = getActiveSearchElement();
    if (!resultsElement) return;

    if (!results.length) {
      resultsElement.innerHTML = `<span class="hextra-search-no-result">{{ $noResultsFound | safeHTML }}</span>`;
      return;
    }

    // Highlight the query in the result text.
    function highlightMatches(text, query) {
      const escapedQuery = query.replace(/[-\\^$*+?.()|[\]{}]/g, '\\$&');
      const regex = new RegExp(escapedQuery, 'gi');
      return text.replace(regex, (match) => `<span class="hextra-search-match">${match}</span>`);
    }

    // Create a DOM element from the HTML string.
    function createElement(str) {
      const div = document.createElement('div');
      div.innerHTML = str.trim();
      return div.firstChild;
    }

    function handleMouseMove(e) {
      const target = e.target.closest('a');
      if (target) {
        const active = resultsElement.querySelector('a.hextra-search-active');
        if (active) {
          active.classList.remove('hextra-search-active');
        }
        target.classList.add('hextra-search-active');
      }
    }

    const fragment = document.createDocumentFragment();
    let dataIdx = 0;

    // Build set of answer URLs to skip from regular results
    const answerUrls = new Set();
    if (answers && answers.length) {
      for (const a of answers) answerUrls.add(a.url + '@' + a.source);
    }

    // Render answer cards
    if (answers && answers.length) {
      for (let ai = 0; ai < answers.length; ai++) {
        const answer = answers[ai];
        const answerSource = answer.prefix ? answer.prefix : answer.source;
        const answerCard = createElement(`
          <li class="hextra-search-answer-card">
            <a data-index="${dataIdx}" href="${answer.url}" class="${dataIdx === 0 ? 'hextra-search-active hextra-search-answer-link' : 'hextra-search-answer-link'}">
              <div class="hextra-search-answer-header">
                <svg class="hextra-search-answer-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" width="16" height="16"><path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a.75.75 0 000 1.5h.253a.25.25 0 01.244.304l-.459 2.066A1.75 1.75 0 0010.747 15H11a.75.75 0 000-1.5h-.253a.25.25 0 01-.244-.304l.459-2.066A1.75 1.75 0 009.253 9H9z" clip-rule="evenodd" /></svg>
                <span class="hextra-search-answer-label">Answer</span>
              </div>
              <div class="hextra-search-answer-text">${highlightMatches(answer.text, query)}</div>
              <div class="hextra-search-answer-footer">
                <span class="hextra-search-answer-source">${answerSource}</span>
                <span class="hextra-search-answer-readmore">{{ $readMore }}</span>
              </div>
            </a>
          </li>`);
        answerCard.addEventListener('mousemove', handleMouseMove);
        answerCard.addEventListener('keydown', handleKeyDown);
        answerCard.querySelector('a').addEventListener('click', function () { hideSearchResults(); });
        fragment.appendChild(answerCard);
        dataIdx++;
      }

      // Separator between answer cards and regular results
      fragment.appendChild(createElement(`<li class="hextra-search-answer-separator" aria-hidden="true"></li>`));
    }

    // Render regular results as bubble cards
    for (let i = 0; i < results.length; i++) {
      const result = results[i];

      // Skip results already shown as answer cards
      if (answerUrls.has(result.route + '@' + result.children.title)) continue;

      const source = result.prefix || '';
      const li = createElement(`
        <li class="hextra-search-result-card">
          <a data-index="${dataIdx}" href="${result.route}" class="${dataIdx === 0 ? 'hextra-search-active hextra-search-result-link' : 'hextra-search-result-link'}">
            <div class="hextra-search-title">${highlightMatches(result.children.title, query)}</div>` +
        (result.children.content
          ? `<div class="hextra-search-excerpt">${highlightMatches(result.children.content, query)}</div>`
          : '') + `
            <div class="hextra-search-result-footer">
              <span class="hextra-search-result-source">${source}</span>
              <span class="hextra-search-result-readmore">{{ $readMore }}</span>
            </div>
          </a>
        </li>`);
      li.addEventListener('mousemove', handleMouseMove);
      li.addEventListener('keydown', handleKeyDown);
      li.querySelector('a').addEventListener('click', function () { hideSearchResults(); });
      fragment.appendChild(li);
      dataIdx++;
    }

    resultsElement.appendChild(fragment);
    resultsElement.dataset.count = dataIdx;
  }
})();
