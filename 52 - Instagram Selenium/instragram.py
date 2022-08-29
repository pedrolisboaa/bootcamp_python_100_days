from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from random import randint


class Instagram:
    def __init__(self, login, senha):
        self.servico = Service(ChromeDriverManager().install())
        self.navegador = webdriver.Chrome(service=self.servico)
        self.navegador.maximize_window()
        self.navegador.implicitly_wait(10)
        self.login = login
        self.senha = senha

    def acessar_site(self):
        self.navegador.get('https://www.instagram.com/')

    def realizar_login(self):
        self.navegador.find_element(By.NAME, 'username').send_keys(self.login)
        self.navegador.find_element(By.NAME, 'password').send_keys(self.senha)
        self.navegador.find_element(By.XPATH, '/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/'
                                              'div[3]/button').click()

        # AGORA NÃO
        self.navegador.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/div/div/button').click()

        # NOTIFICAÇÕES
        self.navegador.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/'
                                              'div/div/div/div/div[2]/div/div/div[3]/button[2]').click()

    def realizar_pesquisa(self):
        self.navegador.find_element(By.CLASS_NAME, '_aauy').send_keys('Chopp')
        sleep(2)
        self.navegador.find_element(By.CLASS_NAME, '_aauy').send_keys(Keys.ENTER)
        sleep(2)
        self.navegador.find_element(By.CLASS_NAME, '_aauy').send_keys(Keys.ENTER)

    def seguir_usuarios(self):
        self.navegador.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/'
                                              'section/main/div/header/section/ul/li[3]/a/div').click()
        sleep(2)

        # AQUI COMEÇOU A SEGUIR
        for x in range(100):
            self.navegador.find_element(By.XPATH, f'/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]'
                                                  f'/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[{x + 1}]'
                                                  f'/div[3]/button/div').click()
            sleep(randint(1, 3))

            print(f'SEGUINDO {x + 1}')

    def sair_site(self):
        self.navegador.quit()
