# In[]:
#c6bank
#https://boards.greenhouse.io/c6bank
import csv
import time
import requests
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError

cond=True 
conteudo = None
URL = 'https://boards.greenhouse.io/c6bank'
cont=0
lista_vagas_inicial = []
lista_vagas_1 = []
lista_vagas_2 = []
lista_final= []


#Função para extração dos dados HTML
def crawl_website(url: str) -> str:
  try:
    resposta = requests.get(url)
    resposta.raise_for_status()
  except HTTPError as exc:
    print(exc)
  else:
    return resposta.text

#Extração dos dados HTML
conteudo=crawl_website(url=URL)
pagina = BeautifulSoup(conteudo, 'html.parser')
vagas = pagina.find_all('section', {'class': 'level-0'})

#Extrai o que interessa, cria e da uma pré tratada nas listas
def criador_de_listas(lista_vaga: list):
  for item in vagas:
    vaga=item.get_text().strip().split('\n')
    lista_vaga.append(list(filter(lambda x: x!='',vaga)))
  return lista_vaga

#Compara listas e devolve vagas do dia
def comparar_listas(lista1, lista2):
    lista_diferenca = []
    for item in lista2:
        if item not in lista1:
            lista_diferenca.append(item)
    return lista_diferenca

#Criação da lista inicial
if cond==True:
    lista_vagas_inicial=criador_de_listas(lista_vaga=lista_vagas_inicial)
    cond=False
    print("Este é o numero inicial de vagas",len(lista_vagas_inicial))

#Criação da lista 1
lista_vagas_1=criador_de_listas(lista_vaga=lista_vagas_1)

while cont<=6:
    # Aguarda 10 minutos (600 segundos)
    time.sleep(10*60)
    #Criação da lista 2
    lista_vagas_2=criador_de_listas(lista_vaga=lista_vagas_2)
    print("Numero de vagas da segunda lista",len(lista_vagas_inicial))
    vagas_do_dia=comparar_listas(lista1=lista_vagas_1,lista2=lista_vagas_2)
    lista_final.append(vagas_do_dia)
    cont+=1
    print(lista_final)



#print(vagas_do_dia)
 
 
 
 
# In[]: 
 
#BTG
#https://carreiras.btgpactual.com/vagas


#PicPay
#https://picpay.com/oportunidades-de-emprego-e-carreiras/central-de-vagas


#XP
#https://boards.greenhouse.io/xpinc/
import csv
import time
import requests
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError

conteudo = None
URL = 'https://boards.greenhouse.io/xpinc/'
cont=0
lista_vagas_inicial = []
lista_vagas_1 = []
lista_vagas_2 = []

#Função para extração dos dados HTML
def crawl_website(url: str) -> str:
  try:
    resposta = requests.get(url)
    resposta.raise_for_status()
  except HTTPError as exc:
    print(exc)
  else:
    return resposta.text

#Extração dos dados HTML
conteudo=crawl_website(url=URL)
pagina = BeautifulSoup(conteudo, 'html.parser')
vagas = pagina.find_all('section', {'class': 'child level-1'})

#Extrai o que interessa, cria e da uma pré tratada nas listas
def criador_de_listas(lista_vaga: list):
  for item in vagas:
    vaga=item.get_text().strip().split('\n')
    lista_vaga.append(list(filter(lambda x: x!='',vaga)))
  return lista_vaga

#Compara listas e devolve vagas do dia
def comparar_listas(lista1, lista2):
    lista_diferenca = []
    for item in lista2:
        if item not in lista1:
            lista_diferenca.append(item)
    return lista_diferenca

#Criação da lista inicial
lista_vagas_inicial=criador_de_listas(lista_vaga=lista_vagas_inicial)

#Criação da lista 1
lista_vagas_1=criador_de_listas(lista_vaga=lista_vagas_1)

#print(lista_vagas_1)
# Aguarda 10 minutos (600 segundos)
time.sleep(10*60)

#Criação da lista 2
lista_vagas_2=criador_de_listas(lista_vaga=lista_vagas_2)
#print(lista_vagas_2)
vagas_do_dia=comparar_listas(lista1=lista_vagas_1,lista2=lista_vagas_2)

print(vagas_do_dia)
 
 
# In[]: 

 
 #Banco Pan
 #https://boards.greenhouse.io/bancopan
import csv
import time
import requests
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError

conteudo = None
URL = 'https://boards.greenhouse.io/bancopan'
cont=0
lista_vagas_inicial = []
lista_vagas_1 = []
lista_vagas_2 = []

#Função para extração dos dados HTML
def crawl_website(url: str) -> str:
  try:
    resposta = requests.get(url)
    resposta.raise_for_status()
  except HTTPError as exc:
    print(exc)
  else:
    return resposta.text

#Extração dos dados HTML
conteudo=crawl_website(url=URL)
pagina = BeautifulSoup(conteudo, 'html.parser')
vagas = pagina.find_all('section', {'class': 'child level-1'})

#Extrai o que interessa, cria e da uma pré trgatada nas listas
def criador_de_listas(lista_vaga: list):
  for item in vagas:
    vaga=item.get_text().strip().split('\n')
    lista_vaga.append(list(filter(lambda x: x!='',vaga)))
  return lista_vaga

#Compara listas e devolve vagas do dia
def comparar_listas(lista1, lista2):
    lista_diferenca = []
    for item in lista2:
        if item not in lista1:
            lista_diferenca.append(item)
    return lista_diferenca

#Criação da lista inicial
lista_vagas_inicial=criador_de_listas(lista_vaga=lista_vagas_inicial)

#Criação da lista 1
lista_vagas_1=criador_de_listas(lista_vaga=lista_vagas_1)

#print(lista_vagas_1)
# Aguarda 10 minutos (600 segundos)
time.sleep(10*60)

#Criação da lista 2
lista_vagas_2=criador_de_listas(lista_vaga=lista_vagas_2)
#print(lista_vagas_2)
vagas_do_dia=comparar_listas(lista1=lista_vagas_1,lista2=lista_vagas_2)

print(vagas_do_dia) 
 
 
 
 
 
 
 
 
 
 