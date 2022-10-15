from turtle import tilt
from urllib import response
import requests
from bs4 import BeautifulSoup
import pandas as pd

response = requests.get("https://www.globo.com")
content = response.content

#convertendo conteudo do site para html
site = BeautifulSoup(content, 'html.parser')
#print(site.prettify()) #organizando impressão 

#encontrando noticia especifica a partir da tag e do seu atributo.
notice = site.find('div', attrs={'class':"has-image theme-jornalismo"})

#encontrando titulo da noticia
titulo = notice.find("h2", attrs={"class":"post__title" })
#print(titulo.prettify())

#obtendo string do titulo da noticia
texto_titulo = titulo.text 
noticiass = []
response2 = requests.get("https://g1.globo.com")
conteudo2 = response2.content
site2 = BeautifulSoup(conteudo2, "html.parser")
#pegando varias noticias ao mesmo tempo
noticias = site2.find_all("div", attrs={"class": "feed-post-body"})
#extraindo titulo de varias noticias 
for noticia in noticias:
    titulo = noticia.find('div',attrs = {"class": "_evt"})
    texto = titulo.find('a', attrs = {"class": "feed-post-link gui-color-primary gui-color-hover"})
    noticiass.append([texto, texto['href']])
tabela = pd.DataFrame(noticiass, columns=['Titulo' , 'link'])
print(tabela)
    
