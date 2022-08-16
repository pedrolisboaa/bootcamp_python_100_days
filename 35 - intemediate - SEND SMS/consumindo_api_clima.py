import math
import requests
from twilio.rest import Client


API_ENDPOINT = 'https://api.openweathermap.org/data/2.5/weather?'
PARAMETROS = {
      'appid': "API DO OPENWEATHER",
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

mensagem_clima = f'Hoje está fazendo {temperatura_atual}ºC, o céu está {ceu}.'

# Enviando mensagem
account_sid = "SID DO TWILIO"
auth_token = "TOKEN DO TWILIO"
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body=mensagem_clima,
                     from_='SEU TELEFONE DO TWILIO',
                     to='TELEFONE REGISTRADO NO TWILIO'
                 )

print(message.sid)
print(message.status)
print('Mensagem enviada com sucesso!')








