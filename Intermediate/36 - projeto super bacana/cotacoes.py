"""
Script que buscar a cotação do dólar, euro e libra utilizando a API awesomeapi
"""
import requests

DOLAR = 'USD-BRL'
EURO = 'EUR-BRL'
LIBRA = 'GBP-BRL'

requisicao = requests.get(f'https://economia.awesomeapi.com.br/json/last/'
                          f'{DOLAR},{EURO},{LIBRA}')
moedas = {
    'dolar': round(float(requisicao.json()['USDBRL']['bid']), 2),
    'euro': round(float(requisicao.json()['EURBRL']['bid']), 2),
    'libra': round(float(requisicao.json()['GBPBRL']['bid']), 2),
}


