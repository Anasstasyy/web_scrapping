import bs4
import requests
from bs4 import BeautifulSoup


KEYWORDS = ['дизайн', 'фото', 'web', 'python']


response = requests.get('https://habr.com/ru/articles/')
soup = BeautifulSoup(response.text, features = 'lxml')

articles_list = soup.findAll('div', class_="tm-articles-list" )

parsed_data = []
for article in articles_list:
    link = f'https://habr.com/ru/{article.find('a', class_="tm-title__link")['href']}'
    print(link)
    response = requests.get(link)
    response = bs4.BeautifulSoup(response.text, features = 'lxml')
    title = soup.find('h2').text.strip()
    time = soup.find('time')['datetime']

    parsed_data.append({
        'title': title,
        'link': link,
        'time': time
    })


