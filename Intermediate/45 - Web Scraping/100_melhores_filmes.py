import requests
from bs4 import BeautifulSoup

response = requests.get('https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/')
sopa = BeautifulSoup(response.text, 'html.parser')

todos_titulos_de_filmes = sopa.select('h3.title')

with open('filmes.txt', 'w+', encoding='utf-8') as arquivo:
    for titulo in todos_titulos_de_filmes:
        arquivo.write(f'{titulo.string}\n')

print('FIM')
