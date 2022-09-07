import requests

requisicao = requests.get(' https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
dados = requisicao.json()

for chaves, valore in dados.items():
    for chave in chaves.keys():
        print(chave['code'])


print(dados['USDBRL']['code'])
print(dados['USDBRL']['bid'])