import requests 
from bs4 import BeautifulSoup
import sys 

header = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:129.0) Gecko/20100101 Firefox/129.0',
    'Cookie': 'gcl_au=1.1.1034739110.1725158291; cookie-banner-consent-accepted=false; glb_uid="iYixGr__Ii-wfPD0SJcL_3aKe1zKcTMmb_qSxljQ2d0="; kppid=27180431362359917133; gpixel_uid=iYixGr__Ii-wfPD0SJcL_3aKe1zKcTMmb_qSxljQ2d0=; _ga=GA1.1.2116010815.1725158295; _ga_P4F3TC8HVE=GS1.1.1725331949.4.1.1725332578.53.0.0; pbjs_sharedId=1831d1e3-d35a-4384-803a-950f32464683; pbjs_sharedId_cst=zix7LPQsHA%3D%3D; permutive-id=e9d938a0-9934-43fd-889a-f4f3dc125b24; ___nrbi_3838=%7B%22firstVisit%22%3A1725158297%2C%22userId%22%3A%220c926949-e156-4c73-87c2-e0e0583c8b29%22%2C%22userVars%22%3A%5B%5B%22mrfExperiment_destaque_test%22%2C%221%22%5D%5D%2C%22futurePreviousVisit%22%3A1725331950%2C%22timesVisited%22%3A2%7D; compass_uid=0c926949-e156-4c73-87c2-e0e0583c8b29; __gads=ID=5e469dedaf03881c:T=1725158297:RT=1725332571:S=ALNI_MYkjkfBTK1YPztd3rjvn8hcANCY_w; __gpi=UID=00000a4ed16391d8:T=1725158297:RT=1725332571:S=ALNI_MYiv92i7pLqtlAgFrOboDSuZEjqqQ; __eoi=ID=f7821fa797c32c8c:T=1725158297:RT=1725332571:S=AA-AfjYTpIbdefZN_pKtn343CDOU; _cc_id=13502d3e4317b625e86b3b7ce3e84aae; panoramaId_expiry=1725763099848; panoramaId=8bbee59a025fb1d764b477bfc1bb185ca02cf364ed9bcb5d4bd42a7bed8616ab; panoramaIdType=panoDevice; cto_bundle=BinDnl9xOHVLUjF0R202R2gxVmtUR01MWm1SNDZQZWtsUml5NkxrMUhNSkdsM3ZRWnF4b2FGMkRGazNXdE1WWjFNRmQ4WTA1M0Jva1NHcm5WeCUyQk1Pc3NGUmVVTmc0eXFZdW5pWHlrdHBDbHIwRHBiZnhiMHpUbjcyMEIlMkJOV1BMdzZzQlduYVR4UG9FcXRmNktuTWQ5UTR5Y1lnJTNEJTNE; GLBEXP=xJxUXD6N+al6PvlgNrZ8wilRDyMhVTfh2wL2MSfo9N8=; ___nrbic_3838=%7B%22previousVisit%22%3A1725158297%2C%22currentVisitStarted%22%3A1725331950%2C%22sessionId%22%3A%22876fd215-f83f-4876-8e1b-c3fb3d2a0573%22%2C%22sessionVars%22%3A%5B%5D%2C%22visitedInThisSession%22%3Atrue%2C%22pagesViewed%22%3A3%2C%22landingPage%22%3A%22https%3A//www.globo.com/%22%2C%22referrer%22%3A%22%22%7D; hsid=5eae71e3-0931-49df-9d9b-0ea1391723f7; _gid=GA1.2.1065983867.1725331950; _hzt.interval=20000; _gat_h_gcom=1; glbExpIdToken=iYixGr__Ii-wfPD0SJcL_9A6AYzKkbRaw0lBUOuhA2k=; FCNEC=%5B%5B%22AKsRol9QrWUOYDfCQpv_BJo58wR83nd1lvsX7sbwZNwLF5tJy2hyo-lA4Mgf6aDfKQ1Vcl233xw_4r6V2QFljdf3PStoAurakvcLUUF2YXEbq0fTZnieA4EV_dCfrxg_iz7Xcf87AKBWnUcO0h1fmYQj8XUkVg-eGw%3D%3D%22%5D%5D' 
}

def request(url):
    try:
        req = requests.get(url, headers=header)
        html = req.text
        return html
    except Exception as error:
        print(f"Error during request: {error}")
        return None

def parser(html):
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
    if len(sys.argv) > 1:
        url = sys.argv[1]
        to_crawler = [url] 
        crawler = set()

        try:
            while to_crawler:
                url = to_crawler.pop(0)
                if url in crawler:
                    continue
                
                print(f"Crawling: {url}")
                html = request(url)
                if html:
                    links = parser(html)
                    crawler.add(url)

                    for link in links:
                        if link not in to_crawler and link not in crawler:
                            to_crawler.append(link)
        except KeyboardInterrupt:
            print("\nCrawling interrupted by user.")
            sys.exit(0)
    else:
        print("Usage: python3 craw.py url")

if __name__ == "__main__":
    main()
