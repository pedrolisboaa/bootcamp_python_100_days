from temperatura import mensagem_clima
from cotacoes import moedas
from noticias import *
from datetime import datetime
from twilio.rest import Client
import os

TEXT_ARRUMADINHO = f"""
DIA E CLIMA
{datetime.now().strftime("%d/%m/%Y")}
{mensagem_clima}
Dolar {moedas['dolar']}
Euro {moedas['euro']}
Libra {moedas['libra']}
NOTICIAS
{principal_noticia_texto_metropoles} - {noticia_principais[principal_noticia_texto_metropoles]}
{principal_noticia_texto_globo} - {noticia_principais[principal_noticia_texto_globo]}
{principal_noticia_texto_uol} - {noticia_principais[principal_noticia_texto_uol]}
"""

# Encaminhando o SMS
# Enviando mensagem
account_sid = ""
auth_token = ""
client = Client(account_sid, auth_token)


message = client.messages \
                .create(
                     body=TEXT_ARRUMADINHO,
                     from_='',
                     to=''
                 )


print(message.status)
print('Mensagem enviada com sucesso!')


