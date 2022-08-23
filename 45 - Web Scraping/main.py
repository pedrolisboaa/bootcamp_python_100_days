from bs4 import BeautifulSoup


# with open('website.html', encoding='utf-8') as site:
#     conteudo = site.read()
#
# sopa = BeautifulSoup(conteudo, 'html.parser')
#
# todos_os_p = sopa.find_all('p')
# todos_links = sopa.find_all('a')
#
# for link in todos_links:
#     print(link.getText())
#
# for link in todos_links:
#     print(link.get('href'))
#
# print(sopa.find_all('h1', id='name'))
# print(sopa.select('h1#name'))

import requests

response = requests.get('https://news.ycombinator.com/newest')
sopa = BeautifulSoup(response.text, 'html.parser')

titulo = sopa.find('title').text
todos_pots = sopa.find_all('a', {'class': 'titlelink'})
todos_scores = sopa.find_all(name='span', class_='score')

print(titulo)
for indice, post in enumerate(todos_pots):
    print(post.text, post.get('href'), todos_scores[indice].text)

