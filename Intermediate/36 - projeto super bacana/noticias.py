from bs4 import BeautifulSoup
import pyshorteners
import requests

# Iniciando encurtado de link
short_link = pyshorteners.Shortener()

# Requisições e raspagem
# Metropoles
request_metropoles = requests.get('https://www.metropoles.com/')
sopa_metropoles = BeautifulSoup(request_metropoles.content, 'html.parser')

principal_noticia_texto_metropoles = sopa_metropoles.find('h2').string
principal_noticia_link_metropoles = sopa_metropoles.select_one('h2.m-title a').attrs['href']

# GLOBO
request_globo = requests.get('https://www.globo.com/')
sopa_globo = BeautifulSoup(request_globo.content, 'html.parser')

principal_noticia_texto_globo = sopa_globo.select_one('h3.post__title').string
principal_noticia_link_globo = sopa_globo.select_one('a.post__link').attrs['href']

# UOL NOTÍCIAS
request_uol = requests.get('https://noticias.uol.com.br/')
sopa_uol = BeautifulSoup(request_uol.content, 'html.parser')

principal_noticia_texto_uol = sopa_uol.select_one('h2').string
principal_noticia_link_uol = sopa_uol.select_one('div.super-highlights a').attrs['href']

# NOMES E LINKS NOTICIAS
noticia_principais = {
    principal_noticia_texto_metropoles: short_link.tinyurl.short(principal_noticia_link_metropoles),
    principal_noticia_texto_globo: short_link.tinyurl.short(principal_noticia_link_globo),
    principal_noticia_texto_uol: short_link.tinyurl.short(principal_noticia_link_uol)
}






