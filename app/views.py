from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas as pd
import time
import os
from django.views.decorators.csrf import requires_csrf_token
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

def  load_driver():
	options = webdriver.FirefoxOptions()
	
	# enable trace level for debugging 
	options.log.level = "trace"

	options.add_argument("-remote-debugging-port=9224")
	options.add_argument("-headless")
	options.add_argument("-disable-gpu")
	options.add_argument("-no-sandbox")

	binary = FirefoxBinary(os.environ.get('FIREFOX_BIN'))

	firefox_driver = webdriver.Firefox(
		firefox_binary=binary,
		executable_path=os.environ.get('GECKODRIVER_PATH'),
		options=options)

	return firefox_driver



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

            
            navegador = load_driver()
            navegador.get("https://scratch.mit.edu/accounts/login/")
            time.sleep(6)
            
            textLogin = navegador.find_element(By.XPATH, '//*[@id="id_username"]').send_keys(row["login"])
            time.sleep(2)

            textSenha = navegador.find_element(By.XPATH, '//*[@id="id_password"]').send_keys(row["senha"])
            time.sleep(2)

            navegador.find_element(By.XPATH, '//*[@id="content"]/form/button').click()
        
            while True:
                time.sleep(1)
        else:
            return render(request, 'logado.html')
