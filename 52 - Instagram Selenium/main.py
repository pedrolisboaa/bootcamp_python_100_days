from instragram import Instagram
from time import sleep

USUARIO = ''
SENHA = ''

conta = Instagram(login=USUARIO, senha=SENHA)

conta.acessar_site()
sleep(3)

conta.realizar_login()
sleep(3)

conta.realizar_pesquisa()
sleep(3)

conta.seguir_usuarios()



sleep(1000)
conta.sair_site()