from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
import constantes


class Formulario:
    def __init__(self):
        self.servico = Service(ChromeDriverManager().install())
        self.navegador = webdriver.Chrome(service=self.servico)
        self.navegador.maximize_window()
        self.navegador.implicitly_wait(10)


    def acessar_site(self):
        self.navegador.get(constantes.FORMULARIO)

    def inserir_dados(self, dado1, dado2, dado3):

        self.navegador.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(dado1)
        sleep(1)
        self.navegador.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(dado2)
        sleep(1)
        self.navegador.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(dado3)
        sleep(1)
        self.navegador.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div').click()
        sleep(1)
        self.navegador.find_element(By.PARTIAL_LINK_TEXT, 'Enviar outra resposta').click()
        sleep(1)

    def fechar_navegador(self):
        self.navegador.quit()