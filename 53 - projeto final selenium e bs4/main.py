from time import sleep
from imovel import Imovel
from formulario import Formulario
from raspagem import raspagem

wimoveis = Imovel()



"""
1º passo do sistema. 
Fazer o filtro no site.
"""
wimoveis.acessar_site()
sleep(5)
wimoveis.filtrar()
URL_SITE = wimoveis.retornar_url()

"""
2º passo do sistema. 
Raspagem de dados
"""

teste = raspagem(URL_SITE)
links = [*teste[0]]
informacao = [*teste[1]]
preco = [*teste[2]]

sleep(5)
wimoveis.fechar_navegador()

"""
3º passo do sistemas
Preenchendo a planilha do google forms
"""
formulario = Formulario()
formulario.acessar_site()

sleep(3)
for x in range(len(links)):
    formulario.inserir_dados(informacao[x], preco[x], links[x])
    sleep(1)

sleep(3)
formulario.fechar_navegador()

print('FIM DO PROGRAMA - COMPLETO')







