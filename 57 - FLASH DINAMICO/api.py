import requests


def retornar_idade(nome):
    requisicao = requests.get(f'https://api.agify.io?name={nome}')
    idade = requisicao.json()['age']
    return idade


def retornar_sexo(nome):
    requisicao = requests.get(f'https://api.genderize.io?name={nome}')
    sexo = requisicao.json()['gender']
    if sexo == 'female':
        return 'mulher'
    return 'homem'


def retornar_todos_post():
    blog_url = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
    todos_post = blog_url.json()
    return todos_post



