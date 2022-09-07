from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
import constantes


class Imovel:
    def __init__(self):
        self.servico = Service(ChromeDriverManager().install())
        self.navegador = webdriver.Chrome(service=self.servico)
        self.navegador.maximize_window()
        self.navegador.implicitly_wait(10)


    def acessar_site(self):
        self.navegador.get(constantes.WIMOVEIS)

    def filtrar(self):
        """
        Selecionar os filtro: ALUGAR
        """
        self.navegador.find_element(By.LINK_TEXT, 'Aluguel').click()

        sleep(2)
        # Selecionando Apartamento
        select_element_apartamento = self.navegador.find_element(By.ID, 'tipos')
        select_object_apartamento = Select(select_element_apartamento)
        select_object_apartamento.select_by_value('APARTAMENTO')

        sleep(2)
        # Selecionando Aguas Claras
        seleciona_cidade = self.navegador.find_element(By.ID, 'cidades')
        selecione_objeto_cidade = Select(seleciona_cidade)
        selecione_objeto_cidade.select_by_value('AGUAS CLARAS')

        sleep(2)
        # Valor médio
        self.navegador.find_element(By.ID, 'valorMedio').send_keys(1500)

        sleep(2)
        # Buscar
        self.navegador.find_element(By.ID, 'botaoDeBusca').click()

    def retornar_url(self):
        return self.navegador.current_url

    def fechar_navegador(self):
        self.navegador.quit()