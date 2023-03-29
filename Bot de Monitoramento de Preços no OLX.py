from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
from time import sleep


def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=1300,1000', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,

    })
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()), options=chrome_options)

    return driver


driver = iniciar_driver()

# Navegar até o site
driver.get('https://sc.olx.com.br/norte-de-santa-catarina/regiao-de-joinville-e-norte-do-estado?q=monitor')
while True:
    # Carregar todos elementos da tela movendo até o final da página e depois ao topo
    sleep(20)
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    sleep(2)
    # Encontrar os títulos
    titulos = driver.find_elements(
        By.XPATH, "//div[@class='sc-12rk7z2-5 fXzBqN']//h2")
    # Encontrar os preços
    precos = driver.find_elements(
        By.XPATH, "//span[@class='m7nrfa-0 cjhQnm sc-bdVaJa cpfGxa']")
    # Encontrar os links
    links = driver.find_elements(
        By.XPATH, "//a[@data-lurker-detail='list_id']")
    # Guardar isso em um arquivo .csv
    for titulo, preco, link in zip(titulos, precos, links):
        with open('precos.csv', 'a', encoding='utf-8', newline='') as arquivo:
            link_processado = link.get_attribute('href')
            arquivo.write(
                f'{titulo.text};{preco.text};{link_processado}{os.linesep}')
    # Fazer isso para todas as páginas existentes
    try:
        botao_proxima_pagina = driver.find_element(
            By.XPATH, "//span[text()='Próxima pagina']")
        sleep(2)
        botao_proxima_pagina.click()
    except:
        print('Chegamos na última página')
        break

input('')
driver.close()