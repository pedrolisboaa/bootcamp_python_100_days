from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

CONTA_TWITTER = 'pedronascimentolisboa@yahoo.com'
SENHA_TWITTER = 'Chopp123@'


class Twitter:
    def __init__(self):
        self.servico = Service(ChromeDriverManager().install())
        self.navegador = webdriver.Chrome(service=self.servico)
        self.navegador.maximize_window()
        self.download = 0
        self.upload = 0

    def resultado_internet(self):
        try:
            # Acessando o site
            self.navegador.get('https://www.speedtest.net/')
            sleep(5)

            # Fechando COOKIES
            self.navegador.find_element(By.XPATH, '/html/body/div[7]/div[2]/div/div/div[3]/button').click()
            sleep(5)

            # Clicando no botão GO
            self.navegador.find_element(By.XPATH,
                                        '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]').click()
            sleep(60)

            self.download = self.navegador.find_element(By.XPATH,
                                                        '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
            self.upload = self.navegador.find_element(By.XPATH,
                                                      '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

            print(self.download)
            print(self.upload)

        except Exception as e:
            print(e)



