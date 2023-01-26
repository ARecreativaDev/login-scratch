from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriver
from selenium.webdriver.chrome.service import Service
import pandas as pd
import time
import os
from django.views.decorators.csrf import requires_csrf_token
# def (request):
#    return (request, '')

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
# driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

dado = "https://www.arecreativa.com.br/scratchLogins.json"
df = pd.read_json(dado)

@requires_csrf_token
def home(request):
    return render(request, 'home.html')

@requires_csrf_token
def dologin(request):
    user = request.POST['nome']

    for index,row in df.iterrows():

    
        if row["login"] == str(user):

            
            navegador = webdriver.Chrome(executable_path= ('/path/to/chromedriver'))
            navegador.get("https://scratch.mit.edu/accounts/login/")
            time.sleep(10)
            
            textLogin = navegador.find_element(By.XPATH, '//*[@id="id_username"]').send_keys(row["login"])
            time.sleep(2)

            textSenha = navegador.find_element(By.XPATH, '//*[@id="id_password"]').send_keys(row["senha"])
            time.sleep(2)

            navegador.find_element(By.XPATH, '//*[@id="content"]/form/button').click()
        
            while True:
                time.sleep(1)
        else:
            return render(request, 'logado.html')
