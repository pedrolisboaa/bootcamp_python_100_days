from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

navegador.get('https://www.python.org/')
sleep(3)

todas_datas = navegador.find_elements(By.CSS_SELECTOR, 'div.event-widget ul.menu time')
todos_eventos = navegador.find_elements(By.CSS_SELECTOR, 'div.event-widget ul.menu a')

datas = [x.text for x in todas_datas]
event = [x.text for x in todos_eventos]


eventos = {}

for i in range(len(todas_datas)):
    eventos[i] = {
        "data": datas[i],
        'nome': event[i],
    }

print(eventos)





navegador.quit()


