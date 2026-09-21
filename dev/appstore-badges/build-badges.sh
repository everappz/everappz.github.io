#!/usr/bin/env bash
#
# build-badges.sh — download Apple's official localized App Store / Mac App Store
# badges (black + white) for every site language into
# static/images/appstore-badges/<lang>/.
#
# Languages Apple does NOT provide a badge for (ar, hi) are skipped; the site
# falls back to the English badges in static/images/.
#
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
OUT_ROOT="$SCRIPT_DIR/../../static/images/appstore-badges"
API="https://toolbox.marketingtools.apple.com/api/v2/badges"

# site-lang : apple-locale  (ar and hi omitted — no Apple badge)
PAIRS="
en:en-us ca:ca-es cs:cs-cz da:da-dk de:de-de el:el-gr es:es-es fi:fi-fi
fr:fr-fr he:he-il hr:hr-hr hu:hu-hu id:id-id it:it-it ja:ja-jp ko:ko-kr
ms:ms-my nl:nl-nl no:no-no pl:pl-pl pt:pt-br ro:ro-ro ru:ru-ru sk:sk-sk
sv:sv-se th:th-th tr:tr-tr uk:uk-ua vi:vi-vn zh-cn:zh-cn zh-tw:zh-tw
"

BADGES="download-on-the-app-store download-on-the-mac-app-store"

# Download one badge file; skip (no file) if Apple has no localized version.
fetch() { # url outfile
  if curl -fsSL "$1" -o "$2" 2>/dev/null; then echo "ok"; else rm -f "$2"; echo "miss"; fi
}

count=0; miss=0
for pair in $PAIRS; do
  lang="${pair%%:*}"; loc="${pair##*:}"
  dir="$OUT_ROOT/$lang"
  mkdir -p "$dir"
  for b in $BADGES; do
    for c in "black:$b.svg" "white:$b-white.svg"; do
      color="${c%%:*}"; file="${c##*:}"
      if [ "$(fetch "$API/$b/$color/$loc" "$dir/$file")" = ok ]; then
        count=$((count + 1))
      else
        miss=$((miss + 1))
      fi
    done
  done
  # drop empty language dir (nothing localized)
  rmdir "$dir" 2>/dev/null || true
  echo "  $lang ($loc)"
done
echo "Downloaded $count badge files (skipped $miss unavailable) into $OUT_ROOT"
