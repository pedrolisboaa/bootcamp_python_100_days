from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)


navegador.get('https://orteil.dashnet.org/cookieclicker/')
sleep(5)

navegador.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[12]/div/div[1]/div[1]/div[10]').click()
sleep(5)

for i in range(100000):
    navegador.find_element(By.ID, 'bigCookie').click()
    if i == 1000:
        sleep(10)
    if i == 2000:
        sleep(10)
    if i == 3000:
        sleep(10)
    if i == 4000:
        sleep(10)
    if i == 5000:
        sleep(10)
    if i == 6000:
        sleep(10)
    if i == 7000:
        sleep(10)
