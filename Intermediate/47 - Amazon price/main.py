import requests
import smtplib
from bs4 import BeautifulSoup

response = requests.get(
    'https://www.mercadolivre.com.br/apple-iphone-13-pro-max-512-gb-grafite/p/MLB18494237?product_trigger_id=MLB18494241&pdp_filters=category%3AMLB1055&applied_product_filters=MLB18494233&quantity=1')

sopa = BeautifulSoup(response.text, 'html.parser')

preco_iphone_site = str(sopa.select_one('div.ui-pdp-price__second-line').text)
nome_produto = sopa.find('h1').getText()
preco_tratado = float(preco_iphone_site.split('R$')[1])

my_email = 'pedronascimentolisboa@yahoo.com'
senha = 'ntlzrglzgzezcjmi'
with smtplib.SMTP('smtp.mail.yahoo.com', port=587) as connection:
    connection.starttls()
    connection.login(
        user=my_email,
        password=senha
    )

    if preco_tratado < 18000:
        connection.sendmail(
            from_addr=my_email,
            to_addrs='phlisboa2000@gmail.com',
            msg=f'Subject:Preco do {nome_produto}!\n\n{preco_tratado}'
        )
