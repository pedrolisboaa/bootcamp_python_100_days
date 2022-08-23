import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.billboard.com/charts/hot-100/2022-08-24/')
sopa = BeautifulSoup(response.text, 'html.parser')

scraping_musicas = sopa.select('ul.lrv-a-unstyle-list li.o-chart-results-list__item h3')
lista_de_musicas = [x.text.strip() for x in scraping_musicas]

print(lista_de_musicas)


ID_CLIENTE =
SEGREDO_CLIENTE =