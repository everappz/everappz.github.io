#!/usr/bin/env python3
# Requires Python 3.6+ (uses f-strings)
"""
Translate Hugo content and i18n files using OpenAI API (gpt-4o-mini).

Usage:
  python scripts/translate_content.py --lang es              # Translate all content to Spanish
  python scripts/translate_content.py --lang es,fr,de        # Multiple languages
  python scripts/translate_content.py --lang all             # All 32 languages
  python scripts/translate_content.py --lang es --tier 1     # Only tier 1 pages
  python scripts/translate_content.py --lang es --file content/blog/post/_index.md
  python scripts/translate_content.py --lang es --overwrite  # Force retranslate
  python scripts/translate_content.py --i18n --lang all      # Generate i18n/*.yaml files
  python scripts/translate_content.py --lang all --dry-run   # Show what would be translated
"""

import argparse
import glob
import json
import os
import random
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

# --- Configuration ---

LANGUAGES = {
    "ar": "Arabic", "ca": "Catalan", "cs": "Czech", "da": "Danish",
    "de": "German", "el": "Greek", "es": "Spanish", "fi": "Finnish",
    "fr": "French", "he": "Hebrew", "hi": "Hindi", "hr": "Croatian",
    "hu": "Hungarian", "id": "Indonesian", "it": "Italian", "ja": "Japanese",
    "ko": "Korean", "ms": "Malay", "nl": "Dutch", "no": "Norwegian",
    "pl": "Polish", "pt": "Portuguese", "ro": "Romanian", "ru": "Russian",
    "sk": "Slovak", "sv": "Swedish", "th": "Thai", "tr": "Turkish",
    "uk": "Ukrainian", "vi": "Vietnamese", "zh-cn": "Simplified Chinese",
    "zh-tw": "Traditional Chinese",
}

PRESERVE_NAMES = ["Evermusic", "Flacbox", "Evertag", "Evervideo", "Soundy", "Everappz"]

EXCLUDE_PATTERNS = [
    "content/auth/**",
    "content/tags/_index.md",
]

TIERS = {
    1: [
        "content/_index.md",
        "content/products/_index.md",
        "content/products/evermusic/_index.md",
        "content/products/evervideo/_index.md",
        "content/products/flacbox/_index.md",
        "content/products/evertag/_index.md",
        "content/products/soundy/_index.md",
        "content/about/_index.md",
        "content/contact/_index.md",
        "content/support/_index.md",
        "content/subscribe/_index.md",
        "content/blog/_index.md",
        "content/docs/_index.md",
        "content/legal/_index.md",
        "content/docs/howto/_index.md",
    ],
    2: [
        "content/legal/privacy-policy.md",
        "content/legal/cookie-policy.md",
        "content/legal/terms-and-conditions.md",
        "content/legal/license-agreement.md",
        "content/legal/legal-notice.md",
    ],
    3: ["content/docs/*/_index.md"],
    4: ["content/docs/howto/**/*.md", "content/docs/faq/**/*.md"],
    5: ["content/docs/guide/**/*.md", "content/blog/**/*.md"],
}

# Hextra theme UI keys that some languages may need
HEXTRA_THEME_KEYS = {
    "backToTop": "Scroll to top",
    "changeLanguage": "Change language",
    "copyCode": "Copy code",
    "codeCopied": "Copied!",
    "dark": "Dark",
    "editThisPage": "Edit this page on GitHub",
    "lastUpdated": "Last updated on",
    "light": "Light",
    "menu": "Menu",
    "readMore": "Read More",
    "searchPlaceholder": "Search...",
    "sidebar": "Sidebar",
    "tags": "Tags",
    "toc": "On this page",
    "returnToTop": "Return to top",
    "system": "System",
    "pageNavigationNext": "Next",
    "pageNavigationPrevious": "Previous",
}

# Languages that already have theme i18n files (no need to include theme keys)
THEME_HAS_I18N = {
    "cs", "de", "es", "fr", "he", "it", "ja", "ko",
    "nl", "pt", "ro", "ru", "uk", "vi", "zh-cn", "zh-tw",
}

SITE_I18N_KEYS = {
    "copyright": "\u00a9 2023 - 2026 EVERAPPZ SL",
    "home": "Home",
    "products": "Products",
    "blog": "Blog",
    "docs": "Documentation",
    "support": "Support",
    "legal": "Legal",
    "contact": "Contact",
    "about": "About",
    "footerProducts": "Products",
    "footerHelp": "Help",
    "footerLegal": "Legal",
    "footerCompany": "Company",
    "footerFAQ": "FAQ",
    "footerHowTo": "How-To",
    "footerUserGuide": "User Guide",
    "footerContactSupport": "Contact support",
    "footerLegalNotice": "Legal Notice",
    "footerPrivacyPolicy": "Privacy Policy",
    "footerCookiePolicy": "Cookie Policy",
    "footerTerms": "Terms and Conditions",
    "footerLicense": "License Agreement",
    "footerAbout": "About",
    "footerBlog": "Blog",
    "footerContact": "Contact",
    "cookieText": "We use essential cookies to keep this site working properly.",
    "cookieLearnMore": "Learn More",
    "cookieOK": "OK",
    "breadcrumbHome": "Home",
}

# Keys where the value should NOT be translated (brand names, legal entities)
NO_TRANSLATE_KEYS = {"copyright"}

API_URL = "https://api.openai.com/v1/chat/completions"
MODEL = "gpt-4.1"

FRONTMATTER_SEP = "[[FRONTMATTER_SEP]]"
BODY_SEP = "[[BODY_SEP]]"


# --- Helpers ---

def get_api_key():
    """Read OpenAI API key from dev/OPENAI_API_KEY.TXT."""
    key_path = os.path.join(get_project_root(), "dev", "OPENAI_API_KEY.TXT")
    if not os.path.exists(key_path):
        print(f"Error: API key file not found at {key_path}")
        print("Create the file with your OpenAI API key.")
        sys.exit(1)
    with open(key_path) as f:
        return f.read().strip()


def get_project_root():
    """Return the project root (parent of scripts/)."""
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def call_openai(api_key, system_prompt, user_content, max_retries=3):
    """Call OpenAI API with retry logic."""
    payload = json.dumps({
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_content},
        ],
        "temperature": 0.3,
    }).encode("utf-8")

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }

    for attempt in range(max_retries):
        try:
            req = urllib.request.Request(API_URL, data=payload, headers=headers)
            with urllib.request.urlopen(req, timeout=120) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                return data["choices"][0]["message"]["content"].strip()
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", errors="replace")
            if e.code == 429 or e.code >= 500:
                wait = (attempt + 1) * 5
                print(f"  API error {e.code}, retrying in {wait}s... ({body[:200]})")
                time.sleep(wait)
            else:
                print(f"  API error {e.code}: {body[:300]}")
                return None
        except Exception as e:
            print(f"  Request error: {e}")
            if attempt < max_retries - 1:
                time.sleep(3)
            else:
                return None
    return None


def parse_frontmatter(content):
    """Split markdown into (frontmatter_dict, frontmatter_raw, body).
    Handles multiline YAML arrays (e.g., keywords: [\n  "val1",\n  "val2"\n]).
    Returns (None, None, content) if no frontmatter found.
    """
    if not content.startswith("---"):
        return None, None, content

    end = content.find("---", 3)
    if end == -1:
        return None, None, content

    fm_raw = content[3:end].strip()
    body = content[end + 3:].strip()

    fm = {}
    lines = fm_raw.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            i += 1
            continue

        if ":" not in stripped:
            i += 1
            continue

        # Only parse top-level keys (not indented)
        if line and line[0].isspace():
            i += 1
            continue

        key, _, val = stripped.partition(":")
        key = key.strip()
        val = val.strip()

        # Handle inline array: key: ["val1", "val2"]
        if val.startswith("[") and val.endswith("]"):
            fm[key] = _parse_yaml_array(val)
            i += 1
            continue

        # Handle multiline array: key: [\n  "val1",\n  ...\n]
        if val.startswith("[") and not val.endswith("]"):
            array_lines = [val]
            i += 1
            while i < len(lines):
                array_lines.append(lines[i].strip())
                if lines[i].strip().endswith("]"):
                    break
                i += 1
            fm[key] = _parse_yaml_array(" ".join(array_lines))
            i += 1
            continue

        # Handle dash-style list: key:\n  - val1\n  - val2
        if val == "":
            list_items = []
            j = i + 1
            while j < len(lines) and lines[j].strip().startswith("- "):
                item = lines[j].strip()[2:].strip().strip('"').strip("'")
                list_items.append(item)
                j += 1
            if list_items:
                fm[key] = list_items
                i = j
                continue

        # Simple scalar value
        fm[key] = val.strip('"').strip("'")
        i += 1

    return fm, fm_raw, body


def _parse_yaml_array(text):
    """Parse a YAML inline array like '["val1", "val2"]' into a list of strings."""
    text = text.strip()
    if text.startswith("["):
        text = text[1:]
    if text.endswith("]"):
        text = text[:-1]
    items = []
    for item in text.split(","):
        item = item.strip().strip('"').strip("'")
        if item:
            items.append(item)
    return items


def get_file_mtime_iso(filepath):
    """Get file modification time as ISO 8601 string."""
    mtime = os.path.getmtime(filepath)
    dt = datetime.fromtimestamp(mtime, tz=timezone.utc)
    return dt.strftime("%Y-%m-%dT%H:%M:%S")


def read_translation_source_modified(translated_path):
    """Read translationSourceModified from a translated file's frontmatter."""
    if not os.path.exists(translated_path):
        return None
    try:
        with open(translated_path, "r", encoding="utf-8") as f:
            content = f.read()
        fm, _, _ = parse_frontmatter(content)
        if fm and "translationSourceModified" in fm:
            return fm["translationSourceModified"]
    except Exception:
        pass
    return None


def build_translated_path(source_path, lang):
    """Convert content/foo/_index.md -> content/foo/_index.{lang}.md
    or content/foo/bar.md -> content/foo/bar.{lang}.md
    """
    p = Path(source_path)
    return str(p.with_suffix(f".{lang}.md"))


def reconstruct_frontmatter(original_fm_raw, translated_fields, source_mtime, lang):
    """Rebuild frontmatter with translated fields and metadata.
    Handles multiline YAML arrays and aliases removal.
    """
    lines = []
    translated_keys = set(translated_fields.keys())
    used_keys = set()
    skip_block = None  # Track multiline blocks to skip/replace

    src_lines = original_fm_raw.split("\n")
    i = 0
    while i < len(src_lines):
        line = src_lines[i]
        stripped = line.strip()

        if not stripped or stripped.startswith("#"):
            lines.append(line)
            i += 1
            continue

        # Detect top-level key (must start at column 0, not indented)
        is_top_level = line and not line[0].isspace()
        if is_top_level and ":" in stripped and not stripped.startswith("- "):
            key = stripped.split(":")[0].strip()
            val_part = stripped.partition(":")[2].strip()

            # Skip aliases entirely (only English owns redirects)
            if key == "aliases":
                i += 1
                # Skip the array content
                if val_part.startswith("[") and not val_part.endswith("]"):
                    while i < len(src_lines) and not src_lines[i].strip().endswith("]"):
                        i += 1
                    i += 1  # skip closing ]
                elif val_part == "":
                    while i < len(src_lines) and src_lines[i].strip().startswith("- "):
                        i += 1
                continue

            # Handle translated keys
            if key in translated_keys:
                val = translated_fields[key]
                used_keys.add(key)

                # Check if original was an array (multiline or inline)
                is_array = val_part.startswith("[")
                if not is_array and val_part == "":
                    # Check if next lines are dash-style list
                    j = i + 1
                    if j < len(src_lines) and src_lines[j].strip().startswith("- "):
                        is_array = True

                if is_array:
                    # Convert comma-separated translated string back to YAML array
                    items = [item.strip() for item in val.split(",") if item.strip()]
                    quoted = ", ".join(f'"{item}"' for item in items)
                    # Short arrays go inline, long ones use multiline
                    inline = f"{key}: [{quoted}]"
                    if len(inline) <= 120:
                        lines.append(inline)
                    else:
                        lines.append(f"{key}: [")
                        for idx, item in enumerate(items):
                            comma = "," if idx < len(items) - 1 else ""
                            lines.append(f'  "{item}"{comma}')
                        lines.append("]")
                    # Skip original array lines
                    i += 1
                    if val_part.startswith("[") and not val_part.endswith("]"):
                        while i < len(src_lines) and not src_lines[i].strip().endswith("]"):
                            i += 1
                        i += 1  # skip closing ]
                    elif val_part.startswith("[") and val_part.endswith("]"):
                        pass  # inline array, already consumed
                    else:
                        # dash-style list
                        while i < len(src_lines) and src_lines[i].strip().startswith("- "):
                            i += 1
                    continue
                else:
                    # Scalar value
                    if any(c in val for c in ':#{}[]|>&*!%@`"'):
                        val = '"' + val.replace('"', '\\"') + '"'
                    elif "'" in val:
                        val = f'"{val}"'
                    lines.append(f"{key}: {val}")
                    i += 1
                    continue

            # Non-translated key with multiline array — keep as-is
            if val_part.startswith("[") and not val_part.endswith("]"):
                lines.append(line)
                i += 1
                while i < len(src_lines) and not src_lines[i].strip().endswith("]"):
                    lines.append(src_lines[i])
                    i += 1
                if i < len(src_lines):
                    lines.append(src_lines[i])
                    i += 1
                continue

        lines.append(line)
        i += 1

    # Add translationSourceModified
    lines.append(f'translationSourceModified: "{source_mtime}"')

    return "\n".join(lines)


def collect_files_for_tier(tier_num, project_root):
    """Resolve tier definition to a list of file paths."""
    tier_def = TIERS.get(tier_num)
    if tier_def is None:
        return []

    if isinstance(tier_def, str):
        tier_def = [tier_def]

    files = []
    for pattern in tier_def:
        if "*" in pattern:
            matches = glob.glob(os.path.join(project_root, pattern), recursive=True)
            files.extend(sorted(matches))
        else:
            full = os.path.join(project_root, pattern)
            if os.path.exists(full):
                files.append(full)

    return files


def collect_all_content_files(project_root):
    """Collect all English .md content files, excluding patterns."""
    content_dir = os.path.join(project_root, "content")
    all_files = []
    for root, _, filenames in os.walk(content_dir):
        for fn in filenames:
            if not fn.endswith(".md"):
                continue
            # Skip existing translations (files with language suffix)
            parts = fn.rsplit(".", 2)
            if len(parts) == 3 and parts[1] in LANGUAGES:
                continue
            full = os.path.join(root, fn)
            rel = os.path.relpath(full, project_root)
            all_files.append(full)

    return sorted(all_files)


def is_excluded(filepath, project_root):
    """Check if file matches any exclusion pattern."""
    rel = os.path.relpath(filepath, project_root)
    for pattern in EXCLUDE_PATTERNS:
        if glob.fnmatch.fnmatch(rel, pattern):
            return True
        # Also check with glob for ** patterns
        matches = glob.glob(os.path.join(project_root, pattern), recursive=True)
        if filepath in matches:
            return True
    return False


# --- Translation functions ---

def translate_content_file(api_key, source_path, lang, lang_name, project_root, overwrite=False, dry_run=False):
    """Translate a single content file to the target language."""
    rel_path = os.path.relpath(source_path, project_root)
    target_path = build_translated_path(source_path, lang)
    source_mtime = get_file_mtime_iso(source_path)

    # Check if translation is needed
    if not overwrite and os.path.exists(target_path):
        existing_mtime = read_translation_source_modified(target_path)
        if existing_mtime == source_mtime:
            return "up-to-date"

    status = "STALE" if os.path.exists(target_path) else "NEW"

    if dry_run:
        return status.lower()

    print(f"  {rel_path} -> {lang}: {status} (translating...)")

    # Read source
    with open(source_path, "r", encoding="utf-8") as f:
        content = f.read()

    fm, fm_raw, body = parse_frontmatter(content)
    if fm is None:
        print(f"  Warning: no frontmatter in {rel_path}, skipping")
        return "error"

    # Build translation payload
    translatable_fm = {}
    for key in ("title", "description", "keywords", "tags"):
        if key in fm and fm[key]:
            val = fm[key]
            # Convert lists to comma-separated string for translation
            if isinstance(val, list):
                translatable_fm[key] = ", ".join(val)
            else:
                translatable_fm[key] = val

    # Combine into single payload
    parts = []
    if translatable_fm:
        fm_text = "\n".join(f"{k}: {v}" for k, v in translatable_fm.items())
        parts.append(f"{FRONTMATTER_SEP}\n{fm_text}\n{FRONTMATTER_SEP}")
    if body.strip():
        parts.append(f"{BODY_SEP}\n{body}\n{BODY_SEP}")

    if not parts:
        print(f"  Warning: nothing to translate in {rel_path}")
        return "error"

    payload = "\n\n".join(parts)

    system_prompt = (
        f"Translate the following Hugo website content to {lang_name}.\n"
        "You MUST preserve the Markdown file structure exactly. Only translate human-readable text.\n"
        "\n"
        "DO NOT modify any of these — return them byte-for-byte identical:\n"
        "- Hugo shortcodes: {{< ... >}}, {{< /... >}}, {{%  ... %}}\n"
        "- HTML tags, CSS, JavaScript code blocks\n"
        "- Markdown structure: heading levels (#, ##, ###), link syntax [text](url), image syntax ![alt](path), list markers (-, *, 1.)\n"
        "- Image paths, URLs, anchor links\n"
        "- Code blocks (``` fenced and indented) and inline code (`...`)\n"
        "- YAML frontmatter keys (only translate the values)\n"
        f"- Separator markers: {FRONTMATTER_SEP} and {BODY_SEP}\n"
        f"- Product names: {', '.join(PRESERVE_NAMES)}\n"
        "\n"
        "ONLY translate:\n"
        "- Paragraph text, heading text, list item text\n"
        "- Link display text (inside [ ]), image alt text (inside ![ ])\n"
        "- YAML frontmatter values for title, description, keywords\n"
        "\n"
        "Additional rules:\n"
        "- Use formal language consistently\n"
        "- Do not add or remove any Markdown formatting, blank lines, or structural elements\n"
        "- Do not translate filenames, CSS class names, or technical identifiers\n"
        "- Only return the translated content, no explanations or commentary"
    )

    result = call_openai(api_key, system_prompt, payload)
    if result is None:
        return "error"

    # Parse result
    translated_fm_fields = {}
    translated_body = body  # fallback

    # Extract frontmatter fields
    fm_match = re.search(
        rf"{re.escape(FRONTMATTER_SEP)}\s*(.*?)\s*{re.escape(FRONTMATTER_SEP)}",
        result, re.DOTALL
    )
    if fm_match:
        for line in fm_match.group(1).strip().split("\n"):
            if ":" in line:
                key, _, val = line.partition(":")
                key = key.strip()
                val = val.strip().strip('"').strip("'")
                if key in ("title", "description", "keywords", "tags"):
                    translated_fm_fields[key] = val

    # Extract body
    body_match = re.search(
        rf"{re.escape(BODY_SEP)}\s*(.*?)\s*{re.escape(BODY_SEP)}",
        result, re.DOTALL
    )
    if body_match:
        translated_body = body_match.group(1).strip()

    # Fix relative image/resource paths for translated pages.
    # Hugo page bundle resources are only served at the default language path,
    # so ./image.webp in /es/products/foo/ would 404. Convert to absolute paths.
    rel_dir = os.path.dirname(os.path.relpath(source_path, os.path.join(project_root, "content")))
    if rel_dir:
        abs_prefix = "/" + rel_dir.replace(os.sep, "/") + "/"
    else:
        abs_prefix = "/"
    # Replace ./ references in shortcode params and markdown
    translated_body = re.sub(r'(?<=["\(])\./', abs_prefix, translated_body)

    # Reconstruct file
    new_fm = reconstruct_frontmatter(fm_raw, translated_fm_fields, source_mtime, lang)
    output = f"---\n{new_fm}\n---\n\n{translated_body}\n"

    # Write
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(output)

    char_count = len(output)
    print(f"  -> wrote {os.path.relpath(target_path, project_root)} ({char_count} chars)")

    # Rate limiting
    time.sleep(random.uniform(1.0, 2.0))
    return "translated"


def translate_i18n(api_key, target_langs, project_root, overwrite=False, dry_run=False):
    """Generate i18n YAML files for target languages."""
    i18n_dir = os.path.join(project_root, "i18n")

    for lang in target_langs:
        lang_name = LANGUAGES[lang]
        target_file = os.path.join(i18n_dir, f"{lang}.yaml")

        if not overwrite and os.path.exists(target_file):
            print(f"  i18n/{lang}.yaml: exists (skip, use --overwrite to regenerate)")
            continue

        if dry_run:
            status = "exists" if os.path.exists(target_file) else "NEW"
            print(f"  i18n/{lang}.yaml: {status}")
            continue

        print(f"  Translating i18n keys to {lang_name}...")

        # Build keys to translate
        keys_to_translate = {}
        for k, v in SITE_I18N_KEYS.items():
            if k not in NO_TRANSLATE_KEYS:
                keys_to_translate[k] = v

        # For languages without theme i18n, also include theme keys
        include_theme_keys = lang not in THEME_HAS_I18N
        if include_theme_keys:
            for k, v in HEXTRA_THEME_KEYS.items():
                keys_to_translate[k] = v

        # Build payload as YAML-like text
        payload_lines = []
        for k, v in keys_to_translate.items():
            payload_lines.append(f'{k}: "{v}"')
        payload = "\n".join(payload_lines)

        system_prompt = (
            f"Translate the following YAML key-value pairs to {lang_name}.\n"
            "Rules:\n"
            "- Keep the YAML keys exactly as they are (only translate the values)\n"
            "- Keep the exact YAML format: key: \"value\"\n"
            f"- Keep product names unchanged: {', '.join(PRESERVE_NAMES)}\n"
            "- Use formal language consistently\n"
            "- Only return the translated YAML, no explanations or extra text"
        )

        result = call_openai(api_key, system_prompt, payload)
        if result is None:
            print(f"  Error translating i18n/{lang}.yaml")
            continue

        # Build output file
        output_lines = []

        # Add copyright (not translated)
        output_lines.append(f'copyright: "{SITE_I18N_KEYS["copyright"]}"')

        # Parse translated result and add
        for line in result.strip().split("\n"):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if ":" in line:
                key = line.split(":")[0].strip()
                if key == "copyright":
                    continue  # Already added
                output_lines.append(line)

        output = "\n".join(output_lines) + "\n"

        with open(target_file, "w", encoding="utf-8") as f:
            f.write(output)

        print(f"  -> wrote i18n/{lang}.yaml")
        time.sleep(random.uniform(1.0, 2.0))


def parse_yaml_file(filepath):
    """Parse a YAML file into a dict of key: value, handling | block scalars."""
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    result = {}
    current_key = None
    current_value_lines = []
    in_block = False

    for line in lines:
        raw = line.rstrip("\n")
        stripped = raw.strip()

        # Skip comments and empty lines at top level
        if not in_block:
            if not stripped or stripped.startswith("#"):
                continue

            # Check for block scalar start: key: |
            if ":" in stripped and not raw[0].isspace():
                # Save previous key if any
                if current_key is not None:
                    result[current_key] = "\n".join(current_value_lines)

                key, _, val = stripped.partition(":")
                key = key.strip()
                val = val.strip()

                if val == "|" or val == "|+":
                    current_key = key
                    current_value_lines = []
                    in_block = True
                else:
                    current_key = None
                    current_value_lines = []
                    result[key] = val.strip('"').strip("'")
            continue

        # Inside block scalar — indented lines belong to current key
        if raw and raw[0].isspace():
            # Strip exactly 2 spaces of indentation (YAML block indent)
            content = raw[2:] if raw.startswith("  ") else raw.lstrip()
            current_value_lines.append(content)
        else:
            # End of block — save and process this line as new key
            if current_key is not None:
                result[current_key] = "\n".join(current_value_lines)
                current_key = None
                current_value_lines = []
            in_block = False

            if stripped and ":" in stripped and not stripped.startswith("#"):
                key, _, val = stripped.partition(":")
                key = key.strip()
                val = val.strip()
                if val == "|" or val == "|+":
                    current_key = key
                    current_value_lines = []
                    in_block = True
                else:
                    result[key] = val.strip('"').strip("'")

    # Save last key if file ends in block scalar
    if current_key is not None:
        result[current_key] = "\n".join(current_value_lines)

    return result


def sync_i18n_keys(api_key, target_langs, project_root, specific_keys=None, overwrite=False, dry_run=False):
    """Sync changed or specific i18n keys from en.yaml to target languages.

    If specific_keys is provided, only those keys are translated.
    Otherwise, detects changes by comparing en.yaml against a hash file.
    """
    import hashlib

    i18n_dir = os.path.join(project_root, "i18n")
    hash_file = os.path.join(i18n_dir, ".en-hashes.json")

    # Parse English source
    en_path = os.path.join(i18n_dir, "en.yaml")
    en_keys = parse_yaml_file(en_path)

    # Determine which keys to translate
    if specific_keys:
        keys_to_sync = {}
        for k in specific_keys:
            if k in en_keys:
                keys_to_sync[k] = en_keys[k]
            else:
                print(f"  Warning: key '{k}' not found in en.yaml")
    else:
        # Load previous hashes
        prev_hashes = {}
        if os.path.exists(hash_file):
            with open(hash_file, "r") as f:
                prev_hashes = json.load(f)

        # Find changed/new keys
        keys_to_sync = {}
        for k, v in en_keys.items():
            h = hashlib.md5(v.encode("utf-8")).hexdigest()
            if k not in prev_hashes or prev_hashes[k] != h:
                keys_to_sync[k] = v

    if not keys_to_sync:
        print("  All i18n keys are up-to-date. Nothing to sync.")
        # Still update hashes
        if not dry_run and not specific_keys:
            _save_hashes(en_keys, hash_file)
        return

    print(f"  Found {len(keys_to_sync)} key(s) to sync:")
    for k in keys_to_sync:
        val_preview = keys_to_sync[k][:60].replace("\n", " ")
        print(f"    - {k}: {val_preview}...")

    if dry_run:
        return

    # Translate to each target language
    for lang in target_langs:
        lang_name = LANGUAGES[lang]
        target_file = os.path.join(i18n_dir, f"{lang}.yaml")

        if not os.path.exists(target_file):
            print(f"  i18n/{lang}.yaml doesn't exist, skip (use --i18n to create)")
            continue

        print(f"\n  Syncing {len(keys_to_sync)} key(s) to {lang_name}...")

        # Read existing target file
        with open(target_file, "r", encoding="utf-8") as f:
            target_content = f.read()

        target_keys = parse_yaml_file(target_file)

        # Build translation payload — send only changed keys
        payload_lines = []
        for k, v in keys_to_sync.items():
            if k in NO_TRANSLATE_KEYS:
                continue
            # Escape for payload
            escaped = v.replace("\n", "\\n")
            payload_lines.append(f'{k}: "{escaped}"')

        if not payload_lines:
            print(f"  No translatable keys for {lang_name}")
            continue

        payload = "\n".join(payload_lines)

        system_prompt = (
            f"Translate the following key-value pairs to {lang_name}.\n"
            "Rules:\n"
            "- Keep the YAML keys exactly as they are (only translate the values)\n"
            "- Keep the exact format: key: \"value\"\n"
            "- Preserve all HTML tags (<br>, <strong>, <a>, <span>, etc.) unchanged\n"
            "- Preserve all URLs and href values unchanged\n"
            "- Preserve \\n as literal \\n in the output\n"
            f"- Keep product names unchanged: {', '.join(PRESERVE_NAMES)}\n"
            "- Keep technical terms unchanged (FLAC, DSD, ALAC, SMB, WebDAV, DLNA, etc.)\n"
            "- Use formal language consistently\n"
            "- Only return the translated key-value pairs, no explanations"
        )

        result = call_openai(api_key, system_prompt, payload)
        if result is None:
            print(f"  Error translating keys for {lang_name}")
            continue

        # Parse translated results
        translated = {}
        for line in result.strip().split("\n"):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if ":" in line:
                key, _, val = line.partition(":")
                key = key.strip()
                val = val.strip().strip('"').strip("'")
                # Unescape newlines
                val = val.replace("\\n", "\n")
                translated[key] = val

        # Update the target YAML file — replace values for synced keys
        lines = target_content.split("\n")
        new_lines = []
        i = 0
        while i < len(lines):
            line = lines[i]
            raw = line.rstrip()
            stripped = raw.strip()

            # Check if this is a key we translated
            if stripped and ":" in stripped and not stripped.startswith("#") and not raw[0:1].isspace():
                key = stripped.split(":")[0].strip()
                val_part = stripped.partition(":")[2].strip()

                if key in translated:
                    new_val = translated[key]
                    if "\n" in new_val:
                        # Multi-line: use block scalar
                        new_lines.append(f"{key}: |")
                        for vline in new_val.split("\n"):
                            new_lines.append(f"  {vline}")
                    else:
                        # Single line
                        if any(c in new_val for c in ':#{}[]|>&*!%@`'):
                            new_val = '"' + new_val.replace('"', '\\"') + '"'
                        new_lines.append(f"{key}: {new_val}")

                    # Skip old block scalar lines if any
                    if val_part == "|" or val_part == "|+":
                        i += 1
                        while i < len(lines) and lines[i] and lines[i][0:1].isspace():
                            i += 1
                    else:
                        i += 1
                    print(f"    Updated {key}")
                    continue

            new_lines.append(line)
            i += 1

        with open(target_file, "w", encoding="utf-8") as f:
            f.write("\n".join(new_lines))

        print(f"  -> updated i18n/{lang}.yaml ({len(translated)} keys)")
        time.sleep(random.uniform(1.0, 2.0))

    # Save new hashes
    if not specific_keys:
        _save_hashes(en_keys, hash_file)
        print(f"\n  Saved hashes to {os.path.relpath(hash_file, project_root)}")


def _save_hashes(en_keys, hash_file):
    """Save MD5 hashes of all English i18n values."""
    import hashlib
    hashes = {}
    for k, v in en_keys.items():
        hashes[k] = hashlib.md5(v.encode("utf-8")).hexdigest()
    with open(hash_file, "w") as f:
        json.dump(hashes, f, indent=2)


# --- Main ---

def main():
    parser = argparse.ArgumentParser(description="Translate Hugo content using OpenAI API")
    parser.add_argument("--lang", required=True, help="Target language(s): es, es,fr,de, or all")
    parser.add_argument("--tier", type=int, choices=[1, 2, 3, 4, 5], help="Only process specific tier")
    parser.add_argument("--file", help="Translate a specific source file")
    parser.add_argument("--overwrite", action="store_true", help="Force retranslate regardless of timestamps")
    parser.add_argument("--i18n", action="store_true", help="Generate i18n YAML files instead of content")
    parser.add_argument("--i18n-sync", action="store_true", help="Sync changed i18n keys from en.yaml to target languages")
    parser.add_argument("--i18n-key", help="Translate specific i18n key(s), comma-separated")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be translated without API calls")
    args = parser.parse_args()

    project_root = get_project_root()

    # Resolve target languages
    if args.lang == "all":
        target_langs = sorted(LANGUAGES.keys())
    else:
        target_langs = [l.strip() for l in args.lang.split(",")]
        for lang in target_langs:
            if lang not in LANGUAGES:
                print(f"Error: unknown language '{lang}'")
                print(f"Available: {', '.join(sorted(LANGUAGES.keys()))}")
                sys.exit(1)

    # i18n sync mode — translate only changed keys
    if args.i18n_sync or args.i18n_key:
        if not args.dry_run:
            api_key = get_api_key()
        else:
            api_key = None
        specific_keys = None
        if args.i18n_key:
            specific_keys = [k.strip() for k in args.i18n_key.split(",")]
        sync_i18n_keys(api_key, target_langs, project_root, specific_keys, args.overwrite, args.dry_run)
        return

    # i18n mode — generate full i18n files
    if args.i18n:
        if not args.dry_run:
            api_key = get_api_key()
        else:
            api_key = None
        translate_i18n(api_key, target_langs, project_root, args.overwrite, args.dry_run)
        return

    # Content mode - collect files
    if args.file:
        source_file = os.path.join(project_root, args.file)
        if not os.path.exists(source_file):
            print(f"Error: file not found: {args.file}")
            sys.exit(1)
        files = [source_file]
    elif args.tier:
        files = collect_files_for_tier(args.tier, project_root)
    else:
        files = collect_all_content_files(project_root)

    # Filter exclusions and deduplicate
    seen = set()
    filtered = []
    for f in files:
        if f in seen:
            continue
        seen.add(f)
        if is_excluded(f, project_root):
            continue
        filtered.append(f)
    files = filtered

    print(f"Files to process: {len(files)}")
    print(f"Target languages: {', '.join(target_langs)}")
    print()

    if not args.dry_run:
        api_key = get_api_key()
    else:
        api_key = None

    # Track stats
    stats = {"translated": 0, "up-to-date": 0, "stale": 0, "new": 0, "error": 0}

    for source_path in files:
        rel = os.path.relpath(source_path, project_root)
        lang_statuses = []

        for lang in target_langs:
            lang_name = LANGUAGES[lang]
            result = translate_content_file(
                api_key, source_path, lang, lang_name,
                project_root, args.overwrite, args.dry_run
            )
            stats[result] = stats.get(result, 0) + 1
            lang_statuses.append(f"{lang}: {result}")

        if args.dry_run:
            print(f"  {rel} -> {', '.join(lang_statuses)}")

    # Summary
    print()
    print("--- Summary ---")
    if args.dry_run:
        print(f"  New: {stats.get('new', 0)}")
        print(f"  Stale: {stats.get('stale', 0)}")
        print(f"  Up-to-date: {stats.get('up-to-date', 0)}")
    else:
        print(f"  Translated: {stats.get('translated', 0)}")
        print(f"  Up-to-date (skipped): {stats.get('up-to-date', 0)}")
        print(f"  Errors: {stats.get('error', 0)}")


if __name__ == "__main__":
    main()
