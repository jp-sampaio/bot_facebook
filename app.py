'''
    Bot que vai fazer uma postagem no facebook

    Passos necessários:
    Passo 1: Entrar na página;
    Passo 2: Encontrar o campo de e-mail e digitar o e-mail;
    Passo 3: Encontrar o campo de senha e digitar a minha senha;
    Passo 4: Encontrar o campo de entrar e clicar;
    Passo 5: Encontrar o campo de escrever no feed;
    Passo 6: Escrever o que estou pensando;
    Passo 7: Clicar no botão de enviar pensamento;
'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from random import randint

def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=1000, 800', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,
    })
    
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

    return driver


def escrever_texto(texto, elemento):
    for letra in texto:
        elemento.send_keys(letra)
        sleep(randint(1, 5) / 30)


driver = iniciar_driver()

# Passo 1: Entrar na página;
driver.get('https://facebook.com')
sleep(5)

driver.maximize_window()
sleep(2)

# Passo 2: Encontrar o campo de e-mail e digitar o e-mail;
email_field = driver.find_element(By.XPATH, '//input[@id="email"]')
sleep(4)
email_field.click()
sleep(1.3)
escrever_texto('endereço email', email_field)
sleep(5)

# Passo 3: Encontrar o campo de senha e digitar a minha senha;
password_field = driver.find_element(By.XPATH, '//input[@id="pass"]')
sleep(3)
password_field.click()
sleep(2)
escrever_texto('senha', password_field)
sleep(4.7)

# Passo 4: Encontrar o campo de entrar e clicar;
enter_button = driver.find_element(By.NAME, 'login')
sleep(2)
enter_button.click()
sleep(10)

# Extra: Carregar a página
home_page = driver.find_element(By.XPATH, '//a[@aria-label="Página inicial"]')
sleep(1)
home_page.click()
sleep(5)

# Passo 5: Encontrar o campo de escrever no feed;
status_field = driver.find_element(By.XPATH, '//div[@class="xi81zsa x1lkfr7t xkjl1po x1mzt3pk xh8yej3 x13faqbe"]')
sleep(3)
status_field.click()
sleep(4)

# Passo 6: Encontrar o campo e escrever o que estou pensando;
thought_field = driver.find_element(By.XPATH, '//p[@class="xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8"]')
sleep(2)
thought_field.click()
sleep(1)
escrever_texto('Olá a todos do meu facebook!', thought_field)
sleep(3)

# Passo 7: Clicar no botão de enviar pensamento;
publish = driver.find_element(By.XPATH, '//div[@class="x1n2onr6 x1ja2u2z x78zum5 x2lah0s xl56j7k x6s0dn4 xozqiw3 x1q0g3np xi112ho x17zwfj4 x585lrc x1403ito x972fbf xcfux6l x1qhh985 xm0m39n x9f619 xn6708d x1ye3gou xtvsq51 x1r1pt67"]')
sleep(3)
publish.click()

input('Finalizado!!!')
driver.close()
