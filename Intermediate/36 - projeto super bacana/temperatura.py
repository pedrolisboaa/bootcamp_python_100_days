"""
Script para buscar da temperatura atual na cidade informado, no caso pela latitude (lat) e longitude (lon).
Nosso script está aplicando para Brasília/DF - Brasil.
"""

import requests
import math

API_ENDPOINT = 'https://api.openweathermap.org/data/2.5/weather?'
PARAMETROS = {
      'appid': "",
      'lat': -15.826691,
      'lon': -47.921822,
      'lang': 'pt_br'
}

# Requisições
resposta = requests.get(API_ENDPOINT, params=PARAMETROS)
dados_meteorologicos = resposta.json()


# Tratamento dos dados
ceu = dados_meteorologicos['weather'][0]['description']
temperatura_atual = math.trunc(float(dados_meteorologicos['main']['temp']) - 273.15)

mensagem_clima = f'{temperatura_atual}C{ceu}.'
