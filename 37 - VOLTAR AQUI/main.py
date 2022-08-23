import requests

#https://pixe.la/@pedrinhomataporco
TOKEN = 'baleiaelimao123'
USERNAME = 'pedrinhomataporco'

pixela_endpoint = 'https://pixe.la/v1/users'

meus_parametros = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": 'yes',
    "notMinor": 'yes'
}

# resposta = requests.post(url=pixela_endpoint, json=meus_parametros)
# print(resposta.text)

grafico_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'
grafico_configuracao = {
    "id": "pm1",
    "name": "Matando Porcos",
    "unit": "unidade",
    "type": "int",
    "color": "shibafu",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

resposta = requests.post(url=grafico_endpoint, json=grafico_configuracao, headers=headers)
print(resposta.text)