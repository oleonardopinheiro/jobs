import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib
import pyperclip


contatos_df = pd.read_excel("emailsSerrana.xlsx")
navegador = webdriver.Chrome()
navegador.get("https://web.whatsapp.com/")

time.sleep(30)

for i, mensagem in enumerate(contatos_df['mensagem']):
    try:
        pessoa = contatos_df.loc[i, "pessoa"]
        numero = contatos_df.loc[i, "número"]
        texto = urllib.parse.quote(f"Oi {pessoa}! {mensagem}")
        link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
        navegador.get(link)

        time.sleep(10)

        # Clica no botão de anexar
        anexar_btn = navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/span')
        anexar_btn.click()

        time.sleep(10)

        # Seleciona a opção de enviar imagem
        #documento_btn = navegador.find_element(By.XPATH, '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/div/ul/li[1]/button/span')
        #documento_btn.click()


        time.sleep(30)

        navegador.find_element(By.XPATH, '//input[@type="file"]').send_keys(r"C:\toptvanuncio.png")

        # Espera o upload da imagem
        time.sleep(5)

        navegador.find_element(By.XPATH, '//*[@id="app"]/div/div/div[3]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div/p/span').send_keys(Keys.ENTER)
        time.sleep(5400)
    except:
        print('Error')

print('Mensagens enviada com sucesso!')
