# "What's New" Blog Post Creation Rules (Everappz)

This is the complete, reusable playbook for writing a product update ("What's New")
blog post for Everappz apps (Evermusic, Flacbox, Evervideo, Evertag, Everdisk).
Follow it exactly so every release post looks and reads the same.

The posts are built with Hugo + the Hextra theme. Posts live in
`content/blog/<slug>/_index.md` (English) plus one translated file per language
(`_index.<lang>.md`).

---

## 0. Inputs you need before writing

Gather these first. Do not start writing until you have them.

1. **App Store "What's New" text** for the release (the raw bullet list the user pastes).
2. **The app name and new version number** (e.g. Evermusic 9.0).
3. **Technical context** so the post can be more detailed than the App Store text.
   Best source: the app repo commit history between the previous release tag/commit
   and this release commit. Example:
   ```
   cd /Users/artem/Documents/Projects/myproject
   git log --oneline <prev-release-commit>..<this-release-commit>
   ```
   Use the commits to explain *what a feature is* and *why it helps*, not just that
   it exists. Never invent behavior that is not in the App Store text or the commits.
4. **The release date** (use today's date unless told otherwise).
5. **App Store IDs** from `data/apps.yaml` (already maintained, single source of truth):
   ```
   evermusic:  ios 885367198   pro 905746421   mac 1564384601
   flacbox:    ios 1097564256                  mac 1594027432
   evervideo:  ios 6602897336                  mac 6743504109
   evertag:    ios 1450763230                  mac 1594027661
   everdisk:   ios 6751851132
   ```

### Reference examples (read these before writing)

Study the structure and tone of recent posts:

- `content/blog/evermusic-8-7-true-gapless-playback-audio-effects-equalizer-carplay/_index.md`
- `content/blog/flacbox-7-6-bass-audio-engine-effects-dsp-music-visualizer/_index.md`
- `content/blog/evervideo-1-7-new-cloud-media-servers-playback-gestures-wifi-drive/_index.md`
- `content/blog/evertag-4-2-new-cloud-connections-tag-editor-options-explained/_index.md`

---

## 1. File location, slug, and naming

- Create a new folder: `content/blog/<slug>/` and put the English post at
  `content/blog/<slug>/_index.md`.
- **Slug format:** `<app>-<version-with-dashes>-<3-to-6-keyword-words>`, all lowercase,
  words separated by single dashes. The version dots become dashes.
  - Example: `evermusic-9-0-customizable-tab-bar-sidebar-media-library-sync`
  - Example: `flacbox-7-6-bass-audio-engine-effects-dsp-music-visualizer`
- Keep the slug keyword-rich but readable. It becomes the URL.

---

## 2. Front matter (YAML)

Copy this exact shape. Fill every field.

```yaml
---
title: "<App> <Version>: <Feature One>, <Feature Two>, and <Feature Three>"
date: <YYYY-MM-DD>
description: "<140 to 320 char plain-language summary naming the app, version, the
  main features, and the platforms (iPhone, iPad, Mac). No dashes as separators.>"
keywords: ["<App> <Version>", "<App> update", "<long-tail keyword>", "..."]
tags: ["<App>", "<App> <Version>", "<Feature>", "...", "What's New"]
aliases:
  - /post/<slug>/
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-founder-everappz.webp"
---
```

Rules for front matter:

- **title:** `"<App> <Version>: <Feature list>"`. Clear and keyword-rich. The main
  features separated by commas, with "and" before the last one.
- **description:** One sentence (or two short ones). Name the app, the version, the
  platforms, and the headline features. This is the meta description, so keep it
  natural and specific. Do NOT use em dashes or hyphens as separators here.
- **keywords:** 15 to 25 entries. Mix of: `"<App> <Version>"`, `"<App> update"`,
  feature names, and long-tail search phrases people actually type
  (e.g. `"customizable tab bar iPhone"`, `"exclude app from iCloud backup"`,
  `"best cloud music player iOS 2026"`). Do not keyword-stuff the body; the keywords
  array is where the long tail lives.
- **tags:** Short tag list. Always start with the app name and `"<App> <Version>"`,
  and always end with `"What's New"`.
- **aliases:** Always include `/post/<slug>/` (legacy URL pattern).
- **cascade.type:** Always `docs`.
- **authors:** Always the exact Artem Meleshko block above. Do not change it.

---

## 3. Body structure (in order)

Use this skeleton every time. Keep the section order.

```markdown
{{< ls-author-byline >}}

**TL;DR:** <one dense paragraph summarizing the whole release. Links the app name
to its product page on first mention: [<App> <Version>](/products/<app>).>

---

## Hello everyone!

<2 to 4 sentence intro. What this update is about and who it is for. Do NOT put a
download link or app-store buttons here. There is only ONE download section, at the
end of the post.>

## <Feature Section 1>

<Short intro paragraph explaining the feature in plain words, then a bullet list.>

- **<Lead-in label>.** <Explanation of what it is and why it helps.>
- **<Lead-in label>.** <...>

## <Feature Section 2>
...

## Why This Update Matters

<One intro sentence (plain text, no bold), then a numbered list of 3 to 4 takeaways.>

1. **<Short bold label>.** <One sentence.>
2. **<Short bold label>.** <One sentence.>
3. **<Short bold label>.** <One sentence.>

## Get <App> <Version>

{{< ls-app-details product="<app>" notes="false" >}}

Thank you for using <App>. <1 to 3 closing sentences asking for a rating and pointing
to support@everappz.com for feedback. Plain text, no bold.>

## Frequently Asked Questions

<6 to 10 ls-details Q&A blocks — see section 6.>
```

### Section guidance

- The **feature sections** should mirror the App Store "What's New" groupings, but
  expanded. Each App Store bullet usually becomes one list item with a bold lead-in
  label and a plain explanation that adds the "what it is / why it matters" detail.
- Keep headings as `##` (H2). Use `###` (H3) only if a feature needs named subparts
  (like the individual audio effects in the 8.7 post).
- Always include a **"Why This Update Matters"** section and a **"Get <App> <Version>"**
  section before the FAQ.

---

## 4. Shortcodes (required components)

All custom components use the `ls-` prefix (Hextra namespace rule). Use these:

### Author byline — top of every post

```
{{< ls-author-byline >}}
```

Place it as the very first line of the body, right after the front matter.

### App Store version cards / download buttons — the single download section

```
{{< ls-app-details product="<app>" notes="false" >}}
```

- `product="<app>"` pulls all versions (ios, pro, mac) for that app from
  `data/apps.yaml` and renders the App Store cards with the download badges and the
  PLATFORM / VERSION / PRICE / DOWNLOADS / RATING / UPDATED grid.
- `notes="false"` — **hide the "What's New" / release-notes panel.** Use this on blog
  posts. (Release notes are shown only on `products/` pages.)
- Omit `footer` — the data-source footer is opt-in via `footer="true"`; leave it off
  on blog posts.
- Omit `heading` — `heading="true"` renders an extra "Available Versions" H2. Do NOT
  use it on blog posts; the `## Get <App> <Version>` heading already covers it.
- You can override country with `country="us"` (default is `us`).
- To show specific apps only, pass `ids="885367198, 1564384601"` instead of `product`.

Result on a blog post: cards + download buttons, **no footer, no release notes,
no "Available Versions" header.**

### FAQ accordions

```
{{% ls-details title="<question>" closed="true" %}}
<answer>
{{% /ls-details %}}
```

Note: `ls-details` uses `{{% %}}` (percent, markdown-rendering) NOT `{{< >}}`.
Always `closed="true"` so the FAQ starts collapsed.

---

## 5. Writing style rules (STRICT)

These are the house style rules. Follow all of them.

1. **Simple words, no AI slop.** Write plainly, like a human explaining the update to
   a friend. Short sentences. No filler, no marketing hype, no "unleash / elevate /
   seamless / game-changing" vocabulary.
2. **No dash symbols in prose.** Do NOT use em dashes (`—`), en dashes (`–`), or a
   hyphen used as a sentence separator (` - `). Rephrase with commas, periods, or
   parentheses instead.
   - Compound words that genuinely need a hyphen should also be avoided where easy —
     rephrase (e.g. write "a vehicle or head unit that supports CarPlay" instead of
     "a CarPlay-compatible vehicle").
   - Markdown list bullets use `-` at the start of the line; that is fine (it is
     structure, not prose) and renders as a bullet.
   - Shortcode names (`ls-details`, `ls-author-byline`, `ls-app-details`), the URL
     slug, and App Store URLs contain dashes; that is required and fine.
3. **Bold rules:**
   - **Allowed:** the `**TL;DR:**` label; the bold lead-in label at the START of a
     list item (e.g. `- **Reorder and edit your tabs.** ...`); the short bold label at
     the start of each numbered "Why This Update Matters" item.
   - **NOT allowed:** bold anywhere inside a prose paragraph, and bold in the MIDDLE
     or body of a list item. Only the lead-in label of a list item may be bold; the
     rest of that item is plain text.
   - The closing "Thank you…" paragraph and the "Why This Update Matters" intro
     sentence are plain text (no bold), including the support email.
4. **One download section only.** The App Store cards (`ls-app-details`) appear once,
   in the "Get <App> <Version>" section. Do not add a text download link in the intro
   or anywhere else.
5. **Accurate claims only.** Describe only features present in the App Store text or
   the commit history. Never invent pricing, limits, or behavior. Remember the apps
   are free downloads with optional in-app upgrades; the equalizer/lyrics/bookmarks
   are free, not premium (see `BLOG_SEO_OPTIMIZE_INSTRUCTIONS.md` for pricing facts).
6. **Link the product page** on first mention of the app in the TL;DR:
   `[<App> <Version>](/products/<app>)`.
7. **Platforms:** state iPhone, iPad, and Mac where true. CarPlay requires a vehicle
   or head unit that supports CarPlay.

---

## 6. FAQ rules (GEO / LLM optimization)

- Add **6 to 10** FAQ entries at the end under `## Frequently Asked Questions`.
- Each uses the `ls-details` shortcode with `closed="true"`.
- **First question is always:** `"What's new in <App> <Version>?"` with a full-release
  summary answer.
- **Last question is always:** a free-update + device-support question, e.g.
  `"Is <App> <Version> a free update, and which devices does it support?"`
- The middle questions should be real, specific questions a user or an AI assistant
  would ask about the headline features ("How do I …", "Can <App> …", "What is …",
  "Does <App> support …"). Phrase them in natural language.
- Answers are self-contained (2 to 5 sentences), factual, and repeat the key terms so
  the passage is citable on its own by AI search engines.
- Same style rules apply inside answers: simple words, no dash symbols, bold only if
  genuinely needed (generally avoid bold in answers).

---

## 7. SEO / GEO checklist (why the structure is shaped this way)

- **TL;DR paragraph** gives AI search a clean, extractable summary of the whole post.
- **Descriptive H2 headings** map to search intent and feature names.
- **Bullet lists with bold lead-ins** are scannable for humans and chunkable for LLMs.
- **FAQ accordions** target question-shaped queries and AI Overviews / ChatGPT /
  Perplexity answers; keep each answer standalone.
- **keywords + tags** carry the long-tail; the body stays natural (no stuffing).
- **Single, consistent download section** via `ls-app-details` keeps live App Store
  stats (version, price, downloads, rating) accurate without manual edits.

---

## 8. Translations

After the English `_index.md` is final, translated versions can be generated as
`_index.<lang>.md` for all supported languages. Follow
`scripts/TRANSLATION_INSTRUCTIONS.md` for what to translate vs. keep. Key points:

- Translate the prose, headings, FAQ questions and answers, `title`, and
  `description`.
- Keep unchanged: shortcode names and their parameters (`{{< ls-app-details
  product="evermusic" notes="false" >}}`, `{{% ls-details %}}`), the `aliases` slug,
  front matter keys, URLs, App Store IDs, product names, and feature names that are
  brand terms.
- The `ls-app-details` "Available Versions" label is localized automatically via
  `i18n/<lang>.yaml` (`availableVersions`), so you do not translate it in the post.

---

## 9. Final pre-publish checklist

- [ ] Folder + `_index.md` created at `content/blog/<slug>/`.
- [ ] Front matter complete: title, date, description, keywords, tags, aliases,
      cascade, authors.
- [ ] `{{< ls-author-byline >}}` is the first body line.
- [ ] TL;DR paragraph present and links `[<App> <Version>](/products/<app>)`.
- [ ] Section order: Hello → feature sections → Why This Update Matters → Get <App>
      <Version> → FAQ.
- [ ] Exactly ONE download section: `{{< ls-app-details product="<app>" notes="false" >}}`
      (no footer, no heading, no release notes).
- [ ] No em dashes / en dashes / hyphen separators in prose.
- [ ] Bold only on TL;DR label and list/numbered lead-in labels. No bold inside
      paragraphs or in the middle of list items.
- [ ] 6 to 10 FAQ `ls-details` blocks, first = "What's new in…", last = free-update +
      devices.
- [ ] All feature claims trace back to the App Store text or commit history.
- [ ] Run a quick dash/bold scan before finishing:
      ```
      grep -n "—\|–" content/blog/<slug>/_index.md        # should be empty
      grep -noE '^- \*\*[^*]+\*\*.*' content/blog/<slug>/_index.md | grep -E '\*\*.*\*\*.*\*\*'   # should be empty
      ```
