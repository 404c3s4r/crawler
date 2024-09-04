import requests
from bs4 import BeautifulSoup
import argparse
import sys
import re


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

def get_emails(html):
    emails = re.findall(r'\w[\w\.]+@\w[\w\.]+\w', html)
    return emails

def main():
    parser = argparse.ArgumentParser(description="Simple web crawler.")
    parser.add_argument("url", help="URL to start crawling from.")
    parser.add_argument("--header", action="append", help="Custom header(s) for the request in 'Key: Value' format.", default=[])
    parser.add_argument("--cookie", action="append", help="Custom cookie(s) for the request in 'Key=Value' format.", default=[])
    parser.add_argument("--emails", action="store_true", help="Crawl and extract emails.")
    parser.add_argument("--urls", action="store_true", help="Crawl and extract URLs.")

    args = parser.parse_args()

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:129.0) Gecko/20100101 Firefox/129.0'
    }

    for header in args.header:
        key, value = header.split(": ", 1)
        headers[key] = value

    if args.cookie:
        cookies = "; ".join(args.cookie)
        headers['Cookie'] = cookies

    to_crawler = [args.url]
    crawler = set()
    found_emails = set() 
    found_urls = set()    
    try:
        while to_crawler:
            url = to_crawler.pop(0)
            if url in crawler:
                continue

            html = request(url, headers)
            
            if html:
                if args.emails:
                    emails = get_emails(html)
                    for email in emails:
                        if email not in found_emails:
                            found_emails.add(email)
                            print(f"Crawling Emails: {email}")

                if args.urls:
                    links = parse_links(html)
                    for link in links:
                        if link not in found_urls:
                            found_urls.add(link)
                            print(f"Crawling URL: {link}")
                    
                    crawler.add(url)
                    for link in links:
                        if link not in to_crawler and link not in crawler:
                            to_crawler.append(link)

    except KeyboardInterrupt:
        print("\nCrawling interrupted by user.")
        sys.exit(0)

if __name__ == "__main__":
    main()
