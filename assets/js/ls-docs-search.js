// Everappz — docs/support inline search (independent of the theme's global
// navbar search). Provides question-intent detection, section re-ranking, and
// answer cards, scoped to the docs + support index only. Reuses window.FlexSearch
// loaded by the theme's stock search.

// Render the search data as JSON.
// {{ $searchDataFile := printf "%s.ls-docs-search-data.json" .Language.Lang }}
// {{ $searchData := resources.Get "json/ls-docs-search-data.json" | resources.ExecuteAsTemplate $searchDataFile . }}
// {{ if hugo.IsProduction }}
//   {{ $searchData = $searchData | minify | fingerprint }}
// {{ end }}
// {{ $noResultsFound := (T "noResultsFound") | default "No results found." }}
// {{ $readMore := (T "readMore") | default "Read more" }}

(function () {
  const searchDataURL = '{{ $searchData.RelPermalink }}';

  // Index instances are module-local (not window globals) so they never collide
  // with the theme's stock search.
  let lsPageIndex;
  let lsSectionIndex;

  // Debounce searching so fast typing coalesces into a single search + render
  // pass (clearing the input hides results immediately, with no delay).
  let searchTimer;
  function debouncedSearch(e) {
    const target = e.target;
    clearTimeout(searchTimer);
    if (!target || !target.value) { search({ target }); return; }
    searchTimer = setTimeout(() => search({ target }), 120);
  }

  const inputElements = document.querySelectorAll('.ls-docs-search-input');
  for (const el of inputElements) {
    el.addEventListener('focus', init);
    el.addEventListener('keyup', debouncedSearch);
    el.addEventListener('keydown', handleKeyDown);
  }

  // Wait for the FlexSearch library (loaded by the theme's stock search).
  function ensureFlexSearch() {
    if (window.FlexSearch) return Promise.resolve();
    return new Promise((resolve) => {
      const timer = setInterval(() => {
        if (window.FlexSearch) { clearInterval(timer); resolve(); }
      }, 50);
    });
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

  // Get the search wrapper, input, and results elements.
  function getActiveSearchElement() {
    const inputs = Array.from(document.querySelectorAll('.ls-docs-search-wrapper')).filter(el => el.clientHeight > 0);
    if (inputs.length === 1) {
      return {
        wrapper: inputs[0],
        inputElement: inputs[0].querySelector('.ls-docs-search-input'),
        resultsElement: inputs[0].querySelector('.ls-docs-search-results')
      };
    }
    return undefined;
  }

  // Dismiss the search results when clicking outside the search box.
  document.addEventListener('mousedown', function (e) {
    const active = getActiveSearchElement();
    if (!active) return;
    const { inputElement, resultsElement } = active;
    if (!inputElement || !resultsElement) return;
    if (
      e.target !== inputElement &&
      e.target !== resultsElement &&
      !resultsElement.contains(e.target)
    ) {
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
    if (!(lsPageIndex && lsSectionIndex)) {
      preloadIndex().then(() => {
        // If the user already typed while the index was loading, render now.
        const active = getActiveSearchElement();
        if (active && active.inputElement && active.inputElement.value) {
          search({ target: active.inputElement });
        }
      }).catch(() => {});
    }
  }

  /**
   * Preloads the search index by fetching data and adding it to the FlexSearch index.
   * @returns {Promise<void>} A promise that resolves when the index is preloaded.
   */
  async function preloadIndex() {
    await ensureFlexSearch();
    const tokenize = '{{- site.Params.search.flexsearch.tokenize | default  "forward" -}}';

    // https://github.com/TryGhost/Ghost/pull/21148
    const regex = new RegExp(
      `[\u{4E00}-\u{9FFF}\u{3040}-\u{309F}\u{30A0}-\u{30FF}\u{AC00}-\u{D7A3}\u{3400}-\u{4DBF}\u{20000}-\u{2A6DF}\u{2A700}-\u{2B73F}\u{2B740}-\u{2B81F}\u{2B820}-\u{2CEAF}\u{2CEB0}-\u{2EBEF}\u{30000}-\u{3134F}\u{31350}-\u{323AF}\u{2EBF0}-\u{2EE5F}\u{F900}-\u{FAFF}\u{2F800}-\u{2FA1F}]|[0-9A-Za-zа-я\u00C0-\u017F\u0400-\u04FF\u0600-\u06FF\u0980-\u09FF\u1E00-\u1EFF\u0590-\u05FF]+`,
      'mug'
    );
    const encode = (str) => { return ('' + str).toLowerCase().match(regex) ?? []; }

    lsPageIndex = new FlexSearch.Document({
      tokenize,
      encode,
      cache: 100,
      document: {
        id: 'id',
        store: ['title', 'content', 'url', 'display', 'crumb'],
        index: "content"
      }
    });

    lsSectionIndex = new FlexSearch.Document({
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

        lsSectionIndex.add({
          id: url,
          url,
          title,
          crumb,
          pageId: `page_${pageId}`,
          content: title,
          ...(paragraphs[0] && { display: paragraphs[0] })
        });

        for (let i = 0; i < paragraphs.length; i++) {
          lsSectionIndex.add({
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

      lsPageIndex.add({
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
  // Section priority: FAQ (specific Q&A) highest, then how-to, then guides (generic).
  function sectionBoost(route) {
    route = (route || '').toLowerCase();
    if (route.includes('/docs/faq/')) return 3;
    if (route.includes('/docs/howto/') || route.includes('/docs/how-to/')) return 2;
    if (route.includes('/docs/guide/')) return 1;
    return 0;
  }

  // True if every term has an occurrence within `window` chars of an occurrence
  // of every other term (the words appear close together, in any order).
  function termsAreNear(hay, terms, window) {
    const positions = terms.map(t => {
      const idxs = [];
      let i = hay.indexOf(t);
      while (i !== -1) { idxs.push(i); i = hay.indexOf(t, i + 1); }
      return idxs;
    });
    if (positions.some(p => !p.length)) return false;
    for (const p0 of positions[0]) {
      let all = true;
      for (let k = 1; k < positions.length; k++) {
        if (!positions[k].some(p => Math.abs(p - p0) <= window)) { all = false; break; }
      }
      if (all) return true;
    }
    return false;
  }

  // Rank groups for ALL queries. Priority, highest first:
  //   1. ALL query words present ("download" AND "music") — dominates partial matches
  //   2. words adjacent as a phrase, either order (download music / music download)
  //   3. words near each other (within ~60 chars)
  //   4. section priority: FAQ > how-to > guide
  //   5. heading hits, then FlexSearch relevance rank
  function scoreGroups(groups, queryInfo) {
    const terms = (queryInfo.cleaned || queryInfo.original || '').toLowerCase().split(/\s+/).filter(t => t.length > 1);
    const multi = terms.length > 1;

    for (const g of groups) {
      const title = (g.pageTitle || '').toLowerCase();
      const content = g.matches.map(m => `${m.title || ''} ${m.content || ''}`).join(' ').toLowerCase();
      const hay = title + ' ' + content;
      const route = (g.route || '').toLowerCase();

      let score = 0;
      let covered = 0;
      for (const t of terms) {
        const inTitle = title.includes(t);
        const inContent = content.includes(t);
        if (inTitle || inContent) covered++;
        if (inTitle) score += 4;
        if (inContent) score += 2;
      }
      g._allTerms = terms.length > 0 && covered === terms.length;

      // TIER 1 — all words present wins over any single-word (partial) match.
      if (multi && g._allTerms) {
        score += 1000;
        const asc = terms.join(' ');
        const desc = terms.slice().reverse().join(' ');
        if (hay.includes(asc) || hay.includes(desc)) score += 200;   // adjacent phrase (either order)
        else if (termsAreNear(hay, terms, 60)) score += 80;          // close together
      }

      // Section priority + heading hits + intent nudges.
      score += sectionBoost(route) * 10;
      score += (g._titleHits || 0) * 3;
      if (queryInfo.intent === 'howto' && (route.includes('/howto/') || route.includes('/how-to/'))) score += 8;
      if (queryInfo.intent === 'definition' && route.includes('/faq/')) score += 8;

      g._score = score;
      g._smartScore = score;
    }

    groups.sort((a, b) => (b._score - a._score) || (a._rk - b._rk));
    return groups;
  }

  /**
   * Extracts answer snippets from top re-ranked results (up to 3 answer cards).
   */
  function extractAnswers(groups, queryInfo) {
    if (!queryInfo.isQuestion || !groups.length) return [];

    const answers = [];
    const seenUrls = new Set();
    const terms = queryInfo.cleaned.toLowerCase().split(/\s+/).filter(t => t.length > 1);

    for (const g of groups) {
      if (answers.length >= 3) break;
      // Only confident answers: every query word must be present (single-word queries always qualify).
      if (terms.length > 1 && !g._allTerms) continue;

      const content = g.matches.map(m => m.content).filter(Boolean).join(' ').trim();
      if (!content || seenUrls.has(g.route)) continue;
      seenUrls.add(g.route);

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

      const deepUrl = (g.matches[0] && g.matches[0].route) || g.route;
      const source = (g.breadcrumbs && g.breadcrumbs.length)
        ? g.breadcrumbs.concat(g.pageTitle).join(' › ')
        : g.pageTitle;
      answers.push({ text, source, url: deepUrl });
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

    // Index is built lazily on focus (init). If a keystroke lands before it's
    // ready, bail — init()'s callback re-runs search() once the index loads.
    if (!lsPageIndex || !lsSectionIndex) return;

    const { resultsElement } = getActiveSearchElement();
    while (resultsElement.firstChild) {
      resultsElement.removeChild(resultsElement.firstChild);
    }
    resultsElement.classList.remove('hx:hidden');

    const queryInfo = preprocessQuery(rawQuery);
    const query = rawQuery;

    // Page-level results (merge in the question-word-stripped query too).
    const MAX_PAGES = 35;
    const MAX_SECTIONS = 15;
    const pageResults = lsPageIndex.search(query, MAX_PAGES, { enrich: true, suggest: true })[0]?.result || [];
    if (queryInfo.isQuestion && queryInfo.cleaned !== query) {
      const cleaned = lsPageIndex.search(queryInfo.cleaned, MAX_PAGES, { enrich: true, suggest: true })[0]?.result || [];
      const seen = new Set(pageResults.map(r => r.id));
      for (const r of cleaned) if (!seen.has(r.id)) pageResults.push(r);
    }

    // Build one GROUP per page: page title + breadcrumb + matching sections.
    const groups = [];
    const occurred = {};
    for (let i = 0; i < pageResults.length; i++) {
      const result = pageResults[i];
      const pageTitle = result.doc.title;
      const crumbParts = (result.doc.crumb || '').split(' > ').map(s => s.trim()).filter(Boolean);
      // The page title is the last crumb part; breadcrumb is the parent path.
      const breadcrumbs = crumbParts.slice(0, -1);
      const baseRoute = (result.doc.url || '').split('#')[0];

      const sectionResults = lsSectionIndex.search(query, MAX_SECTIONS, {
        enrich: true, suggest: true, tag: { 'pageId': `page_${result.id}` }
      })[0]?.result || [];

      let titleHits = 0;
      const matches = [];
      for (let j = 0; j < sectionResults.length; j++) {
        const { doc } = sectionResults[j];
        if (doc.display !== undefined) titleHits++;
        const { url, title } = doc;
        const rawContent = doc.display || doc.content || '';
        const key = url + '@' + rawContent;
        if (occurred[key]) continue;
        occurred[key] = true;
        // Drop the pseudo-entry where content just echoes the section title.
        matches.push({ route: url, title, content: rawContent === title ? '' : rawContent });
      }
      if (!matches.length) {
        matches.push({ route: baseRoute, title: pageTitle, content: '' });
      }

      groups.push({ _rk: i, _titleHits: titleHits, route: baseRoute, pageTitle, breadcrumbs, matches, pageText: result.doc.content || '' });
    }

    // Rank (all queries): all query words present first, then phrase/proximity,
    // then section priority FAQ > how-to > guide.
    scoreGroups(groups, queryInfo);
    const answers = extractAnswers(groups, queryInfo);

    // Highlight the meaningful terms (cleaned query drops question words).
    displayResults(groups, queryInfo.cleaned || query, answers);
  }

  /**
   * Displays the search results on the page.
   *
   * @param {Array} results - The array of search results.
   * @param {string} query - The search query.
   */
  function displayResults(groups, query, answers) {
    const { resultsElement } = getActiveSearchElement();
    if (!resultsElement) return;

    if ((!groups || !groups.length) && (!answers || !answers.length)) {
      resultsElement.innerHTML = `<div class="ls-docs-search-no-result">{{ $noResultsFound | safeHTML }}</div>`;
      resultsElement.dataset.count = 0;
      return;
    }

    // Highlight EACH query term (not just the exact phrase), so multi-word and
    // question queries always highlight the matched words.
    function highlightMatches(text, query) {
      if (!text) return '';
      const terms = (query || '').toLowerCase().split(/\s+/).filter(t => t.length > 1);
      if (!terms.length) return text;
      const escaped = terms
        .map(t => t.replace(/[-\\^$*+?.()|[\]{}]/g, '\\$&'))
        .sort((a, b) => b.length - a.length);
      const regex = new RegExp('(' + escaped.join('|') + ')', 'gi');
      return text.replace(regex, (m) => `<span class="hextra-search-match">${m}</span>`);
    }

    function createElement(str) {
      const div = document.createElement('div');
      div.innerHTML = str.trim();
      return div.firstChild;
    }

    function handleMouseMove(e) {
      const target = e.target.closest('a');
      if (!target) return;
      const active = resultsElement.querySelector('a.hextra-search-active');
      if (active) active.classList.remove('hextra-search-active');
      target.classList.add('hextra-search-active');
    }

    function wire(li) {
      li.addEventListener('mousemove', handleMouseMove);
      li.addEventListener('keydown', handleKeyDown);
      const a = li.querySelector('a');
      if (a) a.addEventListener('click', function () { hideSearchResults(); });
    }

    const fragment = document.createDocumentFragment();
    let dataIdx = 0;

    // === Answer cards (AI-style tips) first ===
    const answerRoutes = new Set();
    if (answers && answers.length) {
      for (let ai = 0; ai < answers.length; ai++) {
        const answer = answers[ai];
        answerRoutes.add(answer.url.split('#')[0]);
        const card = createElement(`
          <li class="hextra-search-answer-card">
            <a data-index="${dataIdx}" href="${answer.url}" class="${dataIdx === 0 ? 'hextra-search-active hextra-search-answer-link' : 'hextra-search-answer-link'}">
              <div class="hextra-search-answer-header">
                <svg class="hextra-search-answer-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" width="16" height="16"><path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a.75.75 0 000 1.5h.253a.25.25 0 01.244.304l-.459 2.066A1.75 1.75 0 0010.747 15H11a.75.75 0 000-1.5h-.253a.25.25 0 01-.244-.304l.459-2.066A1.75 1.75 0 009.253 9H9z" clip-rule="evenodd" /></svg>
                <span class="hextra-search-answer-label">Answer</span>
              </div>
              <div class="hextra-search-answer-text">${highlightMatches(answer.text, query)}</div>
              <div class="hextra-search-answer-footer">
                <span class="hextra-search-answer-source">${answer.source || ''}</span>
                <span class="hextra-search-answer-readmore">{{ $readMore }}</span>
              </div>
            </a>
          </li>`);
        wire(card);
        fragment.appendChild(card);
        dataIdx++;
      }
      fragment.appendChild(createElement(`<li class="hextra-search-answer-separator" aria-hidden="true"></li>`));
    }

    // Query-centered snippet from page text (fallback when a match has no excerpt).
    function makeSnippet(text, q, len) {
      if (!text) return '';
      text = text.replace(/\s+/g, ' ').trim();
      const terms = q.toLowerCase().split(/\s+/).filter(t => t.length > 1);
      const lower = text.toLowerCase();
      let idx = -1;
      for (const t of terms) {
        const i = lower.indexOf(t);
        if (i !== -1 && (idx === -1 || i < idx)) idx = i;
      }
      if (idx === -1) return text.slice(0, len).trim() + (text.length > len ? '…' : '');
      const start = Math.max(0, idx - Math.floor(len / 3));
      const end = Math.min(text.length, start + len);
      return (start > 0 ? '…' : '') + text.slice(start, end).trim() + (end < text.length ? '…' : '');
    }

    // === Grouped results: page (parent) row + indented section (child) rows ===
    for (const g of groups) {
      // Skip a page already surfaced as an answer card.
      if (answerRoutes.has(g.route)) continue;

      // Build informative child rows — every one carries an excerpt (its own, or a
      // query-centered page snippet) so results are never bare titles.
      const seen = new Set();
      const children = [];
      for (const m of g.matches) {
        const childTitle = (m.title && m.title !== g.pageTitle) ? m.title : '';
        const excerpt = m.content || makeSnippet(g.pageText, query, 150);
        if (!childTitle && !excerpt) continue;
        const key = (childTitle + '|' + excerpt).slice(0, 140);
        if (seen.has(key)) continue;
        seen.add(key);
        children.push({ route: m.route, title: childTitle, content: excerpt });
        if (children.length >= 8) break;
      }

      const parentExcerpt = children.length ? '' : makeSnippet(g.pageText, query, 160);
      const crumbHtml = (g.breadcrumbs && g.breadcrumbs.length)
        ? `<div class="ls-docs-search-crumb">${g.breadcrumbs.map(c => `<span>${c}</span>`).join('<span class="ls-docs-search-crumb-sep">›</span>')}</div>`
        : '';

      const parent = createElement(`
        <li class="ls-docs-search-group">
          <a data-index="${dataIdx}" href="${g.route}" class="${dataIdx === 0 ? 'hextra-search-active ls-docs-search-group-link' : 'ls-docs-search-group-link'}">
            ${crumbHtml}
            <div class="ls-docs-search-page-title">${highlightMatches(g.pageTitle, query)}</div>` +
        (parentExcerpt ? `<div class="hextra-search-excerpt">${highlightMatches(parentExcerpt, query)}</div>` : '') + `
          </a>
        </li>`);
      wire(parent);
      fragment.appendChild(parent);
      dataIdx++;

      for (const c of children) {
        const child = createElement(`
          <li class="ls-docs-search-child">
            <a data-index="${dataIdx}" href="${c.route}" class="ls-docs-search-child-link">` +
          (c.title ? `<div class="ls-docs-search-child-title">${highlightMatches(c.title, query)}</div>` : '') +
          (c.content ? `<div class="hextra-search-excerpt">${highlightMatches(c.content, query)}</div>` : '') + `
            </a>
          </li>`);
        wire(child);
        fragment.appendChild(child);
        dataIdx++;
      }
    }

    resultsElement.appendChild(fragment);
    resultsElement.dataset.count = dataIdx;
  }
})();
