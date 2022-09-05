from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

navegador.get('http://secure-retreat-92358.herokuapp.com/')
sleep(1)

navegador.find_element(By.NAME, 'fName').send_keys('Pedro')
navegador.find_element(By.NAME, 'lName').send_keys('Lisboa')
navegador.find_element(By.NAME, 'email').send_keys('pedrolisboa@gmail.com')

navegador.find_element(By.CSS_SELECTOR, 'form.form-signin button').click()
sleep(3)