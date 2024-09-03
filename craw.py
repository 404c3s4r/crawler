import requests
from bs4 import BeautifulSoup
import sys
import argparse

def request(url, headers):
    try:
        req = requests.get(url, headers=headers)
        html = req.text
        return html
    except requests.RequestException as error:
        print(f"Error during request: {error}")
        return None

def parse_links(html):
    if not html:
        return []

    soup = BeautifulSoup(html, 'html.parser')
    tags_a = soup.find_all('a')
    links = []

    for tag in tags_a:
        if 'href' in tag.attrs:
            link = tag['href']
            if link.startswith('http'):
                links.append(link)
    
    return links

def main():
    parser = argparse.ArgumentParser(description="Simple web crawler.")
    parser.add_argument("url", help="URL to start crawling from.")
    parser.add_argument("--header", action="append", help="Custom header(s) for the request in 'Key: Value' format.", default=[])
    parser.add_argument("--cookie", action="append", help="Custom cookie(s) for the request in 'Key=Value' format.", default=[])

    args = parser.parse_args()

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:129.0) Gecko/20100101 Firefox/129.0'
    }

    # Adding custom headers
    for header in args.header:
        key, value = header.split(": ", 1)
        headers[key] = value

    # Adding cookies
    if args.cookie:
        cookies = "; ".join(args.cookie)
        headers['Cookie'] = cookies

    to_crawler = [args.url]
    crawler = set()

    try:
        while to_crawler:
            url = to_crawler.pop(0)
            if url in crawler:
                continue
            
            print(f"Crawling: {url}")
            html = request(url, headers)
            if html:
                links = parse_links(html)
                crawler.add(url)

                for link in links:
                    if link not in to_crawler and link not in crawler:
                        to_crawler.append(link)
    except KeyboardInterrupt:
        print("\nCrawling interrupted by user.")
        sys.exit(0)

if __name__ == "__main__":
    main()
