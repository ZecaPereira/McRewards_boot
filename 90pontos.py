#IMPORTANDO BIBLIOTECAS
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#ABRIR O NAVEGADOR
site = webdriver.Edge()
site.get("https://www.bing.com")
time.sleep(3)
#FAZENDO TODAS AS PESQUISAS DA LISTA
for i in range(30):
    caixa_de_pesquisa = site.find_element(By.XPATH, '//*[@id="sb_form_q"]')
    caixa_de_pesquisa.click()
    caixa_de_pesquisa.send_keys(i, Keys.ENTER)
    time.sleep(5)
    site.back()
    time.sleep(2)
#FECHA TUDO
site.quit()