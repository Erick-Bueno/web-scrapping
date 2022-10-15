from turtle import tilt
from urllib import response
import requests
from bs4 import BeautifulSoup
response = requests.get("https://www.globo.com")
content = response.content

site = BeautifulSoup(content, 'html.parser')#convertendo conteudo do site para html
#print(site.prettify()) #organizando impressão 
notice = site.find('div', attrs={'class':"has-image theme-jornalismo"})#encontrando noticia especifica a partir da tag e do seu atributo class.
titulo = notice.find("h2", attrs={"class":"post__title" })
#print(titulo.prettify()) #buscando titulo da noticia
texto_titulo = titulo.text #obtendo string do titulo da noticia
print(notice.prettify())