import requests
from bs4 import BeautifulSoup


HEADERS = {
    'User-Agent':'1 Firefox/100.0',
    "accept": "text/html, on/xml;q=0.9, */*;q=0.8" 
}

DOMEN = "https://kolesa.kz/"
URL = "https://kolesa.kz/cars/almaty/"


def get_html(url, params=''):   
    return requests.get(url, headers=HEADERS, params=params)

def get_content(html):
    soup = BeautifulSoup(html.text, 'html.parser')
    items = soup.find_all('div', class_='a-list__item')
    data = []
    for item in items:
        try:
            title = item.find('div', class_='a-card__info').find('h5').get_text(strip=True)
        except:
            title = None

        try:
            price = item.find('span', class_='a-card__price').get_text(strip=True).replace('\xa0', '').replace('₸', '')
            price = int(price)
        except:
            price =  None
        data.append(
            [title, price]
        )
    return data


def save(content):
    with open('data.txt', 'a') as f:
        for num, item in enumerate(content, 1):
            f.write(f"№ {num} - Название {item['title']}\n")
            f.write(f"        - Цена {item['price']}\n")


# html = get_html(URL)
# content = get_content(html)
# save(content)



def parse(page):
    contents = []
    for i in range(1 , page+1):
        html = get_html(URL, params={'page': i})
        if html.status_code == 200:
            content = get_content(html)
            contents.extend(content)
            print(f"Страница {i} готово!")
    print('Парсинг готов!')
    save(contents)
    print('Save готов')
    


# page = int(input("Введите количество страниц! \n >> "))

# parse(page)



