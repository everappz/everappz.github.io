import os
import csv
import requests
import xml.etree.ElementTree as ET
from urllib.parse import urlparse, urljoin

HEADERS = {'User-Agent': 'Mozilla/5.0'}
TIMEOUT = 10
HTML_DIR = 'html'
CSV_FILE = 'url_results.csv'

visited_sitemaps = set()
all_urls = set()

def fetch_xml(url):
    print(f'Loading sitemap: {url}')
    try:
        response = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
        response.raise_for_status()
        return ET.fromstring(response.text)
    except Exception as e:
        print(f'Failed to load XML: {url} | Error: {e}')
        return None

def is_sitemap_xml(xml_root):
    return xml_root.tag.endswith('urlset') or xml_root.tag.endswith('sitemapindex')

def parse_sitemap(url):
    if url in visited_sitemaps:
        return
    visited_sitemaps.add(url)

    xml_root = fetch_xml(url)
    if xml_root is None or not is_sitemap_xml(xml_root):
        return

    if xml_root.tag.endswith('urlset'):
        for url_node in xml_root.findall(".//{*}url/{*}loc"):
            page_url = url_node.text.strip()
            if page_url:
                print(f'Found URL: {page_url}')
                all_urls.add(page_url)

    elif xml_root.tag.endswith('sitemapindex'):
        for sitemap_node in xml_root.findall(".//{*}sitemap/{*}loc"):
            nested_url = sitemap_node.text.strip()
            if nested_url:
                parse_sitemap(nested_url)

def test_and_save_url(old_url, new_domain):
    parsed = urlparse(old_url)
    new_url = urljoin(new_domain, parsed.path.lstrip('/'))

    try:
        print(f'Testing: {new_url}')
        response = requests.get(new_url, headers=HEADERS, timeout=TIMEOUT, allow_redirects=True)
        if response.status_code == 200:
            local_path = os.path.join(HTML_DIR, parsed.path.lstrip('/'))
            os.makedirs(os.path.dirname(local_path), exist_ok=True)
            with open(local_path + '.html', 'w', encoding='utf-8') as f:
                f.write(response.text)
            print(f'SUCCESS: {new_url}')
            return old_url, new_url, 'success'
        else:
            print(f'FAILURE ({response.status_code}): {new_url}')
            return old_url, new_url, f'failure ({response.status_code})'
    except Exception as e:
        print(f'FAILURE: {new_url} | Error: {e}')
        return old_url, new_url, 'failure'

def main():
    os.makedirs(HTML_DIR, exist_ok=True)
    root_sitemap = 'https://www.everappz.com/sitemap.xml'
    new_domain = 'https://everappz.github.io/'

    # Step 1: Crawl sitemap(s)
    parse_sitemap(root_sitemap)
    print(f'\nTotal URLs found: {len(all_urls)}\n')

    # Step 2: Test each URL and save results
    results = []
    for old_url in sorted(all_urls):
        results.append(test_and_save_url(old_url, new_domain))

    # Step 3: Save results to CSV
    with open(CSV_FILE, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Old URL', 'New URL', 'Test Result'])
        writer.writerows(results)

    print(f'\nResults saved to {CSV_FILE}')
    print(f'HTML saved under ./{HTML_DIR}/')

if __name__ == '__main__':
    main()