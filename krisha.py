import requests
from bs4 import BeautifulSoup

HEADERS = {
    'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0',
    "accept": "text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8" 
}

URL = "https://krisha.kz/arenda/kvartiry/almaty/?das[live.rooms][]=2&das[live.rooms][]=3&das[price][from]=100000&das[price][to]=500000"
DOMEN = "https://krisha.kz"


def get_html(URL, headers=HEADERS, params=' '):
    html = requests.get(URL, headers=headers, params=params).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup


def get_data(soup):
    items = soup.find_all('div', class_="a-card")
    
    for item in items:
        try:
            title = item.find('div', class_="a-card__header-left").find('a').get_text(strip=True)
        except:
            title = "None"
        try:
            link = DOMEN+item.find('a', class_="a-card__title").get('href')
        except:
            link = "None"
        try:
            img = item.find('source').get('srcset')
            text = item.find('img').get('alt')
        except:
            img = "None"


        print(title)
        print(text)


    return items


# soup = 
# data = 
get_data(get_html(URL))





