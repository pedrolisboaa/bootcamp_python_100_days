from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)


navegador.get('https://www.amazon.com.br/Apple-iPhone-Pro-Max-512-GB/dp/B09L1Q86R8/ref=sr_1_1_sspa?keywords=iphone+13+pro+max&qid=1661522581&sprefix=ip%2Caps%2C223&sr=8-1-spons&ufe=app_do%3Aamzn1.fos.25548f35-0de7-44b3-b28e-0f56f3f96147&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFGN0JBS0VHMDkzVlImZW5jcnlwdGVkSWQ9QTAwODY5MzMyVjdYOTFUWUgxMEpNJmVuY3J5cHRlZEFkSWQ9QTA5MjA0MjQxTDhEVFlJSVpYVThRJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==')

sleep(5)
preco = navegador.find_element(By.CLASS_NAME, 'a-price-whole')
link = navegador.find_element(By.CSS_SELECTOR, '#averageCustomerReviews a')
print(preco.text)
print(link.text)

navegador.quit()