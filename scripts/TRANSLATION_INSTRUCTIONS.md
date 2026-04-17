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
- DO NOT translate: `aliases`, `date`, `draft`, `layout`, `headless`, `appStoreUrl`, `appStoreId`, `screenshots`, or any other technical frontmatter fields

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

### Special Cases
- `EVERAPPZ` headline — keep as-is (brand name)
- App Store review shortcode — keep as-is (reviews are in original language)
- `press-carousel` shortcode — keep as-is
- `social-cards` shortcode — keep as-is
- `lottie` animations — keep as-is

### Page Bundle Images (IMPORTANT)
Hugo page bundles are language-scoped. Images stored alongside `_index.md` (e.g., `heroimage/`, `screenshots/`) are only served for the English page. Translated pages cannot access them via relative paths.

**Rule:** In translated files, convert all relative image paths to absolute paths:
- `./heroimage/hero_1600.webp` → `/products/<product>/heroimage/hero_1600.webp`
- `./screenshots/1.png` → `/products/<product>/screenshots/1.png`

This applies to any `image="./..."` parameter in shortcodes like `hextra/hero-container`, `hextra/hero-badge`, `card`, etc. The absolute path resolves to the English page bundle's resources, which are shared across all locales.

## Character Encoding Rules

- ALWAYS use proper UTF-8 characters, NEVER HTML entities
- Correct: `à`, `é`, `ñ`, `ü`, `ö`
- Wrong: `&agrave;`, `&eacute;`, `&ntilde;`, `&uuml;`, `&ouml;`
- Exception: `&nbsp;` in layout HTML is OK (it's intentional for spacing)

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

## Pages Pending Translation

- `content/about/_index.md`
- `content/support/_index.md`
- `content/contact/_index.md`
- `content/docs/_index.md`
- `content/docs/faq/_index.md`
- `content/docs/guide/_index.md`
- `content/docs/howto/_index.md`
- `content/legal/_index.md`
- `content/products/_index.md`
- `content/products/evermusic/_index.md`
- `content/products/evervideo/_index.md`
- `content/products/flacbox/_index.md`
- `content/products/evertag/_index.md`
- `content/products/soundy/_index.md`
- `content/subscribe/_index.md`

Skip: `content/blog/_index.md` (no translatable content), `content/auth/` (skip entirely)
