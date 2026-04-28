# Translation Instructions for Content MD Files

## File Structure

Hugo uses filename-based translations:
- `_index.md` — English (default)
- `_index.es.md` — Spanish
- `_index.fr.md` — French
- etc.

Files go in the SAME folder as the English original.

## Supported Languages (32)

ar, ca, cs, da, de, el, es, fi, fr, he, hi, hr, hu, id, it, ja, ko, ms, nl, no, pl, pt, ro, ru, sk, sv, th, tr, uk, vi, zh-cn, zh-tw

## What to Translate

Each translated file is an EXACT copy of the English original with ONLY these text strings translated:

### Frontmatter
- `title:` — translate the value
- `description:` — translate the value
- `keywords:` — translate all keyword values for local SEO
- `tags:` — translate all tag values for local SEO
- `features:` — translate the feature descriptions
- `aliases:` — **REMOVE entirely** from translated files (do not keep, do not translate). Aliases in translations cause duplicate route conflicts in Hugo.
- DO NOT translate: `date`, `draft`, `layout`, `headless`, `appStoreUrl`, `appStoreId`, `screenshots`, or any other technical frontmatter fields

### Body Text
- Hero badge `<span>` text (e.g., "14 Million Downloads")
- Hero subtitle text inside `<strong>` tags
- Hero paragraph bullet points (the text, not the `•` bullets)
- Feature card `title="..."` and `subtitle=`...`` values
- Section headline text (inside `{{< hextra/section-headline >}}...{{< /hextra/section-headline >}}`)
- Product card `tag="..."` and `subtitle="..."` values
- Info paragraph text (inside `{{< hextra/info-paragraph >}}...{{< /hextra/info-paragraph >}}`)
- FAQ detail `title="..."` values and FAQ content text
- Guide card `title="..."` and `subtitle="..."` values
- Subscribe/contact paragraph text (keep markdown links intact)
- Form `placeholder="..."` values
- Button visible text (e.g., `>Subscribe</button>`)
- Markdown headings (`## Heading Text`)
- Markdown paragraphs and list items

### What to Keep in Markdown Links
When translating text with markdown links like:
```
By subscribing, you agree to our [Privacy Policy](/legal/privacy-policy) and accept the [Terms and Conditions](/legal/terms-and-conditions/).
```
- Translate the visible text: "By subscribing...", "Privacy Policy", "Terms and Conditions"
- Keep the URL paths unchanged: `/legal/privacy-policy`, `/legal/terms-and-conditions/`

## What NOT to Translate or Modify

### Never Change
- ALL `{{< rawhtml >}}...{{< /rawhtml >}}` blocks (CSS, JavaScript)
- ALL `<style>...</style>` and `<script>...</script>` blocks
- Shortcode names: `hextra/feature-card`, `hextra/hero-badge`, `hextra/section-headline`, `card`, `cards`, `lottie`, `force-dark`, `appstore-reviews`, `social-cards`, etc.
- Shortcode parameter NAMES: `title=`, `subtitle=`, `icon=`, `style=`, `link=`, `image=`, `method=`, `options=`, `imageStyle=`, `lottie=`, `lottieWidth=`, `apps=`, `stars=`, `cols=`, `border=`
- Product names: EVERAPPZ, Evervideo, Evermusic, Flacbox, Evertag, Soundy
- CSS classes (anything with `hx:`, `hextra-`, etc.)
- HTML structure: `<div>`, `<span>`, `<br>`, `<a>` tags and their attributes
- HTML entities in layout: `&nbsp;`, `<br class="hx:sm:block hx:hidden" />`
- URLs: all `href`, `link`, `src` values
- Icon names: `icon="code"`, `icon="shield-check"`, etc.
- Image paths and processing options
- Form `action=` URL, `method=`, `name=`, `class=`, `id=` attributes
- The honeypot div (`position: absolute; width: 0; height: 0; overflow: hidden;`)

### App UI Menu Items (IMPORTANT)

When the post references app menu items (e.g., **Settings**, **Connections**, **Music Library**, **Audio Player**, **Local Files**, **Equalizer**, **More actions**, etc.), use the official translated UI strings from the app's localization files.

**Localization files location:** `/Users/artem/Documents/Projects/myproject/MyApp/Localization/all/{lang}.lproj/Localizable.strings`

**Pre-extracted reference:** `scripts/ui_translations.json` — contains key UI term translations for all 32 languages in JSON format. Use this file first for quick lookup and update it if needed.

**Language folder mapping:**
- Most languages use their code directly: `es.lproj`, `fr.lproj`, `de.lproj`, etc.
- Exceptions: `no` → `nb.lproj`, `pt` → `pt-PT.lproj`, `zh-cn` → `zh-Hans.lproj`, `zh-tw` → `zh-Hant.lproj`

**How to use:** When you encounter a UI term like **Settings > Audio Player > General** in the English post, look up "Settings", "Audio Player", and "General" in the localization reference and replace with their translated equivalents. If a term is not found in the localization files, translate it naturally.

### Special Cases
- `EVERAPPZ` headline — keep as-is (brand name)
- App Store review shortcode — keep as-is (reviews are in original language)
- `press-carousel` shortcode — keep as-is
- `social-cards` shortcode — keep as-is
- `lottie` animations — keep as-is

### Page Bundle Images (IMPORTANT)
Hugo page bundles are language-scoped. Images stored alongside `_index.md` (e.g., `heroimage/`, `screenshots/`) are only served for the English page. Translated pages cannot access them via relative paths.

**Rule:** Move images from the page bundle to `static/` and use absolute paths in BOTH the English source and all translations:
1. Move `content/<section>/<page>/image.png` → `static/<section>/<page>/image.png`
2. Update the English `_index.md` to use the absolute path: `![](/section/page/image.png)`
3. All translated `_index.XX.md` files use the same absolute path

This applies to:
- Markdown images: `![](image.png)` → `![](/section/page/image.png)`
- Shortcode `image="./..."` parameters → `image="/section/page/..."`
- Any `image="./..."` in shortcodes like `hextra/hero-container`, `hextra/hero-badge`, `card`, etc.

**Example (blog post):**
- Move: `content/blog/my-post/diagram.png` → `static/blog/my-post/diagram.png`
- English & all translations use: `![](/blog/my-post/diagram.png)`

For product pages with `heroimage/` and `screenshots/` subdirectories:
- Move: `content/products/evermusic/heroimage/` → `static/products/evermusic/heroimage/`
- English & all translations use: `image="/products/evermusic/heroimage/hero_1600.webp"`

## Character Encoding Rules

- ALWAYS use proper UTF-8 characters, NEVER HTML entities
- Correct: `à`, `é`, `ñ`, `ü`, `ö`
- Wrong: `&agrave;`, `&eacute;`, `&ntilde;`, `&uuml;`, `&ouml;`
- Exception: `&nbsp;` in layout HTML is OK (it's intentional for spacing)

## Quoting Rules (CRITICAL)

Hugo shortcode parameters and YAML frontmatter use ASCII double quotes `"` as delimiters. **Never place unescaped ASCII double quotes inside these values.** This causes Hugo build errors like `got positional parameter ... Cannot mix named and positional parameters`.

### In shortcode parameters (`title="..."`, `subtitle="..."`, `alt="..."`, `caption="..."`)
- **NEVER** use ASCII double quotes `"` inside the value
- Use single quotes `'`, angle brackets `«»`, corner brackets `「」`, or rephrase to avoid inner quotes
- Wrong: `title="My SanDisk shows "busy" error"`
- Correct: `title="My SanDisk shows 'busy' error"`
- Correct (CJK): `title="我的SanDisk显示「忙碌」错误"`
- Correct (Cyrillic): `title="Мой SanDisk показывает ошибку «занят»"`

### In YAML frontmatter (`title: "..."`, `description: "..."`)
- Same rule: **no ASCII double quotes inside the value**
- Wrong: `title: "How to fix "error" on iPhone"`
- Correct: `title: "How to fix 'error' on iPhone"`

### In keywords and tags arrays
- Each value is already wrapped in `["..."]` — no inner double quotes allowed
- Wrong: `keywords: ["fix "busy" error"]`
- Correct: `keywords: ["fix busy error"]`

## Example: Feature Card Translation

English:
```
{{< hextra/feature-card
    title="Built for You. Improved by You."
    subtitle=`We read all reviews and use your feedback to improve every update.`
    icon="code"
    style="background: radial-gradient(circle at 50% 80%, rgba(99,102,241,0.15), transparent);"
>}}
```

Spanish:
```
{{< hextra/feature-card
    title="Hecho para ti. Mejorado por ti."
    subtitle=`Leemos todas las reseñas y usamos tus comentarios para mejorar cada actualización.`
    icon="code"
    style="background: radial-gradient(circle at 50% 80%, rgba(99,102,241,0.15), transparent);"
>}}
```

Only `title` and `subtitle` VALUES changed. Everything else identical.

## Example: Hero Subtitle Translation

English:
```
{{< hextra/hero-subtitle >}}
<strong>Discover our apps that boost productivity,&nbsp;<br class="hx:sm:block hx:hidden" />and make daily tasks easier and more enjoyable.</strong>
{{< /hextra/hero-subtitle >}}
```

German:
```
{{< hextra/hero-subtitle >}}
<strong>Entdecken Sie unsere Apps, die die Produktivität steigern&nbsp;<br class="hx:sm:block hx:hidden" />und den Alltag einfacher und angenehmer machen.</strong>
{{< /hextra/hero-subtitle >}}
```

The `<strong>`, `&nbsp;`, `<br class="...">` tags stay exactly in place.

## Validation After Translation

1. Check YAML validity: `ruby -ryaml -e 'YAML.load_file("i18n/XX.yaml")'`
2. Build site: `hugo --quiet`
3. Check for HTML entities: `grep -oh '&[a-z]\{2,\};' content/_index.XX.md | grep -v 'nbsp\|amp'`
4. Check for broken shortcodes: `grep -rl 'HAHAHUGOSHORTCODE' public/`

## Current i18n Architecture

- `i18n/*.yaml` — 32 files, 60 keys each (theme UI + site-specific)
- `layouts/partials/custom/footer.html` — uses `{{ T "key" }}` for footer/cookie/legal strings
- `layouts/_shortcodes/social-cards.html` — reusable social media cards
- Content files use standard Hugo shortcodes with inline text (no i18n shortcodes in content)
- The `{{< t >}}` and `{{< tp >}}` shortcodes were REMOVED — they don't work reliably in Hugo (can't nest inside other shortcodes, break in headings)


Skip: `content/auth/` (skip entirely)
