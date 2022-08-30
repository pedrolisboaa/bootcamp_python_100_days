import requests
from bs4 import BeautifulSoup


def raspagem(url):
    url_teste = url
    response = requests.get(url_teste)
    sopa = BeautifulSoup(response.text, 'html.parser')

    # PEGANDO OS LINKS
    links = [f"https://www.dfimoveis.com.br/{x.get('href')}" for x in
             sopa.select('div.property__info h3.hide-mobile a')]

    # PEGANDO OS ENDEREÇOS
    informacoes = [x.text.strip() for x in sopa.select('div.property__info-content p.property__text ')]

    # PEGANDO OS PREÇOS
    precos = []
    precos_nao_tratados = [x.text for x in sopa.select('div.property__info h4.hide-mobile span.price')]
    for x in precos_nao_tratados:
        if not len(x) < 3:
            precos.append(x)

    return [links, informacoes, precos]
