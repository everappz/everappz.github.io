import os
import csv
import requests
import xml.etree.ElementTree as ET
from urllib.parse import urlparse, urljoin

OLD_DOMAIN = 'https://www.everappz.com'
# NEW_DOMAIN = 'https://everappz.github.io'
NEW_DOMAIN = 'http://localhost:1313'
SITEMAP_URL = f'{OLD_DOMAIN}/sitemap.xml'
CSV_FILE = 'results.csv'


def is_xml(content):
    return content.strip().startswith('<?xml')


def fetch(url):
    try:
        print(f'🔄 Loading: {url}')
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.text
        else:
            print(f'⚠️ Error: {url} returned {response.status_code}')
            return None
    except Exception as e:
        print(f'❌ Exception for {url}: {e}')
        return None


def parse_sitemap(xml, base_url):
    urls = []
    try:
        root = ET.fromstring(xml)
        for elem in root.iter():
            if elem.tag.endswith('loc'):
                loc = elem.text.strip()
                if loc.endswith('.xml'):
                    # Probably a nested sitemap
                    nested = fetch(loc)
                    if nested and is_xml(nested):
                        urls.extend(parse_sitemap(nested, loc))
                    else:
                        print(f'❌ Invalid nested sitemap: {loc}')
                else:
                    urls.append(loc)
        return urls
    except Exception as e:
        print(f'❌ Failed to parse XML from {base_url}: {e}')
        return []


def check_response_code(old_url, new_url):
    try:
        response = requests.get(new_url, timeout=10, allow_redirects=True)
        if response.status_code == 200:
            return 'success'
        else:
            return f'failed ({response.status_code})'
    except Exception as e:
        return f'failed ({e})'


def main():
    print('📥 Fetching sitemap...')
    sitemap_xml = fetch(SITEMAP_URL)
    if not sitemap_xml:
        print('❌ Failed to load main sitemap.')
        return

    print('🔍 Parsing URLs...')
    urls = parse_sitemap(sitemap_xml, SITEMAP_URL)
    urls = sorted(set(urls))  # deduplicate
    print(f'✅ Total URLs found: {len(urls)}\n')

    with open(CSV_FILE, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Old URL', 'New URL', 'Test Result'])

        for old_url in urls:
            if not old_url.startswith(OLD_DOMAIN):
                continue
            new_url = old_url.replace(OLD_DOMAIN, NEW_DOMAIN, 1)
            print(f'🌐 Testing: {new_url}')
            result = check_response_code(old_url, new_url)
            writer.writerow([old_url, new_url, result])
            print(f'✅ Result: {result}\n')


if __name__ == '__main__':
    main()