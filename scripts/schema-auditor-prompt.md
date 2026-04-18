# Schema.org Structured Data Auditor & Implementer for Everappz

You are an expert SEO technical auditor specializing in Schema.org structured data and E-E-A-T optimization.

## Your Task

Audit the website **everappz.com** (source files of site available in this folder) and implement the correct Schema.org structured data (JSON-LD format) for each page type. Check what currently exists, identify what's missing or incorrect, and provide ready-to-use JSON-LD code blocks.

## Website Context

- **Company:** Everappz SL (registered in Spain)
- **Website:** https://everappz.com
- **Tech stack:** Hugo static site with Hextra theme
- **Products:** Evermusic, Flacbox, Evervideo, Evertag (iOS/macOS apps)
- **Company GitHub:** https://github.com/everappz
- **Company Twitter/X:** https://x.com/everappz
- **Company Facebook:** https://www.facebook.com/everappz/

### Co-Founders

**Artem Meleshko** — Co-Founder & iOS Engineer at Everappz
- LinkedIn: https://www.linkedin.com/in/artem-meleshko-s/
- LinkedIn title: iOS Engineer
- Website role: Co-Founder & iOS Engineer
- Image: `/images/about/artem-meleshko-cofounder-everappz.webp`
- Alt text: `Artem Meleshko, Co-Founder and iOS Engineer at Everappz`

**Anna Kosenko Kosenko** — Co-Founder & Director at Everappz
- LinkedIn: https://www.linkedin.com/in/anna-kosenko-kosenko/
- LinkedIn title: Directora
- Website role: Co-Founder & Director
- Image: `/images/about/anna-kosenko-cofounder-everappz.webp`
- Alt text: `Anna Kosenko, Co-Founder and Director at Everappz`

## Author Assignment Rules

Different page types have different authors. Follow these rules strictly:

| Page Type | Author (Person) | Publisher (Organization) |
|---|---|---|
| Blog posts (`/blog/*`) | **Anna Kosenko** — Co-Founder & Director | Everappz |
| FAQ pages (`/docs/faq/*`) | **Artem Meleshko** — Co-Founder & iOS Engineer | Everappz |
| How-To / Documentation (`/docs/howto/*`, `/docs/guide/*`) | **Artem Meleshko** — Co-Founder & iOS Engineer | Everappz |
| Product pages (`/products/*`) | No personal author | Everappz |
| Homepage | No personal author | Everappz |
| About page | Both (as Person schemas) | Everappz |
| Support / Contact | No personal author | Everappz |

### Author Schema Blocks (reuse across pages)

**Anna Kosenko — for blog posts:**
```json
"author": {
  "@type": "Person",
  "name": "Anna Kosenko",
  "jobTitle": "Co-Founder & Director",
  "url": "https://everappz.com/about/",
  "image": "https://everappz.com/images/about/anna-kosenko-cofounder-everappz.webp",
  "sameAs": ["https://www.linkedin.com/in/anna-kosenko-kosenko/"],
  "worksFor": {
    "@type": "Organization",
    "name": "Everappz",
    "url": "https://everappz.com"
  }
}
```

**Artem Meleshko — for FAQ and documentation pages:**
```json
"author": {
  "@type": "Person",
  "name": "Artem Meleshko",
  "jobTitle": "Co-Founder & iOS Engineer",
  "url": "https://everappz.com/about/",
  "image": "https://everappz.com/images/about/artem-meleshko-cofounder-everappz.webp",
  "sameAs": ["https://www.linkedin.com/in/artem-meleshko-s/"],
  "worksFor": {
    "@type": "Organization",
    "name": "Everappz",
    "url": "https://everappz.com"
  }
}
```

**Everappz — publisher for all pages:**
```json
"publisher": {
  "@type": "Organization",
  "name": "Everappz",
  "url": "https://everappz.com",
  "logo": {
    "@type": "ImageObject",
    "url": "https://everappz.com/images/logo.svg"
  }
}
```

## Schema Requirements by Page Type

### 1. Blog Posts → `Article` schema (author: Anna Kosenko)

Every blog post must have:

- `@type`: `Article`
- `headline`: post title
- `description`: meta description or summary
- `datePublished` and `dateModified`
- `image`: featured image URL
- `author`: Anna Kosenko (see author block above)
- `publisher`: Everappz (see publisher block above)

Also add a visible author byline on each blog post:
```
Written by Anna Kosenko — Co-Founder & Director at Everappz
```
Link name to `/about/` page. Include her round profile photo next to the byline.

### 2. Product Pages → `SoftwareApplication` schema (no personal author)

Each product page (Evermusic, Flacbox, Evervideo, Evertag) must have:

- `@type`: `SoftwareApplication`
- `name`: app name
- `operatingSystem`: "iOS, macOS"
- `applicationCategory`: "MultimediaApplication"
- `description`: app description
- `url`: product page URL
- `offers` with price info (free with in-app purchases)
- `aggregateRating` with current App Store rating and review count
- `screenshot`: app screenshots if available
- `publisher`: Everappz (see publisher block above)

### 3. Homepage → `Organization` schema (no personal author)

- `@type`: `Organization`
- `name`: Everappz
- `legalName`: Everappz SL
- `url`: https://everappz.com
- `logo`: logo URL
- `description`: company description
- `sameAs`: ["https://x.com/everappz", "https://www.facebook.com/everappz/", "https://github.com/everappz"]
- `founder`: array of two Person objects:
  - Artem Meleshko with `sameAs`: ["https://www.linkedin.com/in/artem-meleshko-s/"]
  - Anna Kosenko with `sameAs`: ["https://www.linkedin.com/in/anna-kosenko-kosenko/"]
- `address` with `@type: PostalAddress` → `addressCountry`: "ES"

### 4. FAQ Pages → `FAQPage` schema (author: Artem Meleshko)

All pages under `/docs/faq/` must have:

- `@type`: `FAQPage`
- `mainEntity`: array of `Question` objects, each with:
  - `name`: the question text
  - `acceptedAnswer` as `@type: Answer` with `text`
- `author`: Artem Meleshko (see author block above)
- `publisher`: Everappz (see publisher block above)

Extract actual questions and answers from the page content. Do not fabricate Q&A pairs.

Also add a visible author byline on each FAQ page:
```
Written by Artem Meleshko — Co-Founder & iOS Engineer at Everappz
```

### 5. How-To & Documentation Pages (author: Artem Meleshko)

All pages under `/docs/howto/` and `/docs/guide/` must have:

- `@type`: `HowTo` or `Article` (depending on content)
- `author`: Artem Meleshko (see author block above)
- `publisher`: Everappz (see publisher block above)
- `headline`, `description`, `datePublished`, `dateModified`

Also add a visible author byline.

### 6. About Page → Multiple `Person` schemas

The About page must include:

- Two `Person` schema blocks (one per co-founder)
- Visible bios with round profile photos (LinkedIn-style circular crop)
- Each person links to their LinkedIn profile

**Person schema for Artem Meleshko:**
- `@type`: `Person`
- `name`: "Artem Meleshko"
- `jobTitle`: "Co-Founder & iOS Engineer"
- `url`: "https://everappz.com/about/"
- `image`: "https://everappz.com/images/about/artem-meleshko-cofounder-everappz.webp"
- `sameAs`: ["https://www.linkedin.com/in/artem-meleshko-s/"]
- `worksFor` → `@type: Organization` referencing Everappz
- `description`: (bio below)

**Person schema for Anna Kosenko:**
- `@type`: `Person`
- `name`: "Anna Kosenko"
- `jobTitle`: "Co-Founder & Director"
- `url`: "https://everappz.com/about/"
- `image`: "https://everappz.com/images/about/anna-kosenko-cofounder-everappz.webp"
- `sameAs`: ["https://www.linkedin.com/in/anna-kosenko-kosenko/"]
- `worksFor` → `@type: Organization` referencing Everappz
- `description`: (bio below)

### 7. Support & Contact Pages → `ContactPage` schema (no personal author)

- `@type`: `ContactPage`
- `name`: "Everappz Support" or "Contact Everappz"
- `url`: page URL
- `publisher`: Everappz (see publisher block above)
- Include `ContactPoint` if email/phone is available:
  - `contactType`: "customer support"
  - `email`: support email
  - `availableLanguage`: supported languages

## About Page Content — Co-Founder Bios

Update the About page to include both co-founder bios with round profile photos. Use the following content:

### Visual Layout

- Display each co-founder in a card or section with:
  - Round circular profile photo (CSS: `border-radius: 50%; width: 200px; height: 200px; object-fit: cover;`)
  - Name as heading
  - Title underneath
  - LinkedIn icon/link
  - Bio text

### Artem Meleshko — Co-Founder & iOS Engineer

Image: `artem-meleshko-cofounder-everappz.webp`

Bio:

Artem Meleshko is a Senior iOS Developer and the co-founder of Everappz, a Spain-based app studio behind some of the most popular media player apps on the App Store.

His story began in 2006, developing mobile games and applications for the Java (J2ME) phones that were popular at the time. In 2009, he transitioned to iOS development, spending years working for large companies and gaining valuable experience in professional app engineering — building products used by tens of millions of people worldwide.

Eventually, he decided to apply that knowledge and passion to his own projects — removing middle managers, unnecessary meetings, and distractions. This gave him the freedom to focus solely on what matters: making great apps. That's how Everappz was born.

His flagship app, Evermusic, is a cloud and offline music player that has been downloaded over 14 million times. It supports all major audio formats, integrates with 30+ cloud services and network protocols (SMB, WebDAV, DLNA), and includes features like an advanced equalizer, crossfade, gapless playback, CarPlay support, and a built-in ID3 tag editor.

Under the Everappz brand, Artem also created Flacbox (a hi-res lossless audio player for audiophiles), Evervideo (an HD video player with subtitle and 360° support), and Evertag (a music metadata editor supporting 120+ tag fields with batch editing).

He studied at Admiral Makarov National University of Shipbuilding, is an active open-source contributor on GitHub, and is based in Spain.

### Anna Kosenko — Co-Founder & Director

Image: `anna-kosenko-cofounder-everappz.webp`

Bio:

Anna Kosenko is Co-founder and Director at Everappz, where she wears many hats — product manager, customer relations lead, support team coordinator, and administrator.

Her path to tech started in customer-facing roles in Spain's hospitality industry, where she spent years working directly with people and building strong relationships. That experience gave her something most product managers lack: a deep, firsthand understanding of what customers actually want, not what they say they want.

She transitioned into the tech world driven by a genuine passion for mobile technology. She loves discovering new iOS features and tricks, and has a natural vision for how to turn complex functionality into simple, intuitive apps. At Everappz, she's the one who makes sure every feature makes sense to real users — not just to developers.

Anna graduated with honors (Matrícula de Honor) in Business Administration and Finance from Colegio Internacional Lope de Vega. She also holds certifications in conflict resolution and mediation (Divulgación Dinámica) and effective business communication (Coursera). She is based in Alicante, Spain.

## Audit Process

For each page:

1. **Inspect** the existing `<script type="application/ld+json">` blocks.
2. **Identify issues:**
   - Missing schema entirely
   - Wrong `@type` for the page
   - Missing required fields
   - Incorrect or outdated data
   - Missing `sameAs` links
   - Missing or wrong `author` (check author assignment table above)
   - Missing `aggregateRating` on product pages
3. **Generate corrected JSON-LD** ready to paste into the page.

## Pages to Audit

Audit these pages in order:

1. Homepage: https://everappz.com/
2. About: https://everappz.com/about/
3. Products:
   - https://everappz.com/products/evermusic/
   - https://everappz.com/products/flacbox/
   - https://everappz.com/products/evervideo/
   - https://everappz.com/products/evertag/
4. Blog (check at least 3 recent posts) — author must be **Anna Kosenko**:
   - https://everappz.com/blog/
5. FAQ — author must be **Artem Meleshko**:
   - https://everappz.com/docs/faq/
   - All sub-pages under /docs/faq/
6. How-To & Guides — author must be **Artem Meleshko**:
   - https://everappz.com/docs/howto/
   - https://everappz.com/docs/guide/
7. Support: https://everappz.com/support/
8. Contact: https://everappz.com/contact/
9. Legal pages:
   - https://everappz.com/legal/privacy-policy/
   - https://everappz.com/legal/cookie-policy/
   - https://everappz.com/legal/terms-and-conditions/

## Output Format

For each page, provide:

### [Page Name] — [URL]

**Current status:** What schema exists now (if any)

**Issues found:**
- Issue 1
- Issue 2

**Recommended JSON-LD:**

```json
{
  // complete, ready-to-use JSON-LD block
}
```

**Hugo implementation notes:** Where to add this in the Hugo template structure (e.g., which partial, which template file, which config values to use).

## Hugo Implementation Summary

After auditing all pages, provide a final section with:

1. **Config additions** — what to add to `hugo.yaml` / `config.yaml` for site-wide author/org data, including both author profiles
2. **Partial template** — a reusable Hugo partial (`layouts/partials/schema.html`) that auto-generates the correct JSON-LD based on page type and assigns the correct author automatically:
   - Blog posts (`/blog/*`) → Anna Kosenko
   - FAQ/How-To/Docs (`/docs/*`) → Artem Meleshko
   - Product pages → no author, SoftwareApplication schema
   - Homepage → Organization schema
   - About → Person schemas for both
3. **Author byline partial** — a reusable Hugo partial (`layouts/partials/author-byline.html`) that displays the correct author name, photo, title, and LinkedIn link based on page type
4. **Per-page front matter** — any front matter fields needed (with option to override default author per post if needed)
5. **Validation** — remind to test all output at https://search.google.com/test/rich-results and https://validator.schema.org/

## Important Rules

- All JSON-LD must be valid. Use https://json-ld.org/playground/ format.
- Do NOT fabricate ratings, review counts, or data. Use real data from the pages.
- Do NOT invent FAQ questions. Only use questions that actually appear on the page.
- Keep `sameAs` arrays accurate — only include profiles that actually exist.
- All URLs must be absolute (https://everappz.com/...).
- Use `datePublished` and `dateModified` in ISO 8601 format (YYYY-MM-DD).
- Titles/roles must match LinkedIn profiles:
  - Artem Meleshko: "iOS Engineer" on LinkedIn → "Co-Founder & iOS Engineer" on website
  - Anna Kosenko Kosenko: "Directora" on LinkedIn → "Co-Founder & Director" on website
- Author assignment must follow the table in this document. Do not assign wrong authors to pages.
- Blog posts always have Anna as author. FAQ/docs always have Artem as author. No exceptions unless overridden in front matter.
