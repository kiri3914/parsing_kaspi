import requests
from bs4 import BeautifulSoup
from pprint import pprint

HEADERS = {
    'User-Agent':'1 Firefox/100.0',
    "accept": "text/html, on/xml;q=0.9, */*;q=0.8" 
}

DOMEN = "https://kaspi.kz"
URL = "https://kaspi.kz/shop/search/?text=%D1%82%D0%B5%D0%BB%D0%B5%D1%84%D0%BE%D0%BD&qs=suggestion"



def get_html(URL, headers=HEADERS, params=' '):
    html = requests.get(URL, headers=headers, params=params)
    soup = BeautifulSoup(html.text, 'html.parser')
    return soup


def get_content(soup):
    items = soup.find_all('div', class_='item-card')
    data = []

    for item in items:
        title = item.find('div', class_='item-card__info').find('a').get_text()
        link = DOMEN + item.find('div', class_='item-card__info').find('a').get('href')
        
        local_data = get_html(link)
        img = local_data.find_all('meta')[12].get('content')
        data.append(
            {
                'title': title,
                'link': link,
                'img': img
            }
        )
    return data


soup = get_html(URL)
data = get_content(soup)

pprint(data)

# def parse():
#     conts = []
#     for i in range(1, 3):
#         soup = get_html(URL, params={'page': i})
#         data = get_content(soup)
#         conts.extend(data)
#         print(f'page {i} is ready!')

#     pprint(conts)

# parse()



