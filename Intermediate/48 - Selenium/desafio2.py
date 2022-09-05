from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

navegador.get('https://en.wikipedia.org/wiki/Main_Page')
sleep(1)
navegador.find_element(By.XPATH, '/html/body/div[3]/div[3]/div[5]/div[1]/div[1]/div/div[3]/a[1]').click()


