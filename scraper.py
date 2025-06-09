import requests
from bs4 import BeautifulSoup
import time
from fake_useragent import UserAgent
ua = UserAgent()
headers = {
    'User-Agent': ua.random,
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive'
}
def scrape_amazon(search_term, min_price=None, max_price=None):
    base_url = "https://www.amazon.in/s"
    params = {'k': search_term}
    if min_price and max_price:
        params['rh'] = f'p_36:{int(min_price)}00-{int(max_price)}00'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive'
    }
    try:
        response = requests.get(base_url, params=params, headers=headers)
        if response.status_code != 200:
            print(f"Amazon request failed: {response.status_code} - {response.text[:100]}")
            return []
        soup = BeautifulSoup(response.text, 'html.parser')
        if "captcha" in response.text.lower():
            print("Amazon CAPTCHA detected")
            return []
        products = []
        for item in soup.find_all('div', {'data-component-type': 's-search-result'}):
            try:
                title = item.find('h2').text.strip()
                price_whole = item.find('span', {'class': 'a-price-whole'})
                price = float(price_whole.text.replace(',', '').replace('₹', '')) if price_whole else None
                link = 'https://www.amazon.in' + item.find('a', {'class': 'a-link-normal s-no-outline'})['href']
                if price and (not min_price or price >= float(min_price)) and (not max_price or price <= float(max_price)):
                    products.append({'title': title, 'price': price, 'link': link})
            except:
                continue
        time.sleep(2)  # Avoid rapid requests
        return products
    except Exception as e:
        print(f"Amazon scraping error: {e}")
        return []

def scrape_flipkart(search_term, min_price=None, max_price=None):
    base_url = "https://www.flipkart.com/search"
    params = {'q': search_term}
    if min_price and max_price:
        params['p[]'] = f'facets.price_range.from={min_price}&facets.price_range.to={max_price}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive'
    }
    try:
        response = requests.get(base_url, params=params, headers=headers)
        if response.status_code != 200:
            print(f"Flipkart request failed: {response.status_code} - {response.text[:100]}")
            return []
        soup = BeautifulSoup(response.text, 'html.parser')
        if "captcha" in response.text.lower():
            print("Flipkart CAPTCHA detected")
            return []
        products = []
        for item in soup.find_all('div', {'class': '_1AtVbE'}):
            try:
                title = item.find('a', {'class': 's1Q9rs'}) or item.find('div', {'class': '_4rR01T'})
                title = title.text.strip() if title else None
                price_whole = item.find('div', {'class': '_30jeq3'})
                price = float(price_whole.text.replace(',', '').replace('₹', '')) if price_whole else None
                link = 'https://www.flipkart.com' + item.find('a', {'class': 's1Q9rs'})['href'] if item.find('a', {'class': 's1Q9rs'}) else None
                if title and price and link and (not min_price or price >= float(min_price)) and (not max_price or price <= float(max_price)):
                    products.append({'title': title, 'price': price, 'link': link})
            except:
                continue
        time.sleep(15)  # Avoid rapid requests
        return products
    except Exception as e:
        print(f"Flipkart scraping error: {e}")
        return []