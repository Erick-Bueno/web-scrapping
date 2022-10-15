from math import prod
import requests
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl
prodtuoss = []
pesquisa = str(input("qual produto voce deseja pesquisar:"))
response = requests.get(f"http://lista.mercadolivre.com.br/{pesquisa}")
conteudo = response.content
mercado_livre = BeautifulSoup(conteudo, "html.parser")
produtos = mercado_livre.find_all("div", attrs={"class":"andes-card andes-card--flat andes-card--default ui-search-result shops__cardStyles ui-search-result--core andes-card--padding-default andes-card--animated"})
for produto in produtos:
    buscar_nome = produto.find("h2", attrs = {"class": "ui-search-item__title ui-search-item__group__element shops__items-group-details shops__item-title"})
    produto_nome = buscar_nome.text
    buscar_preço_real = produto.find("span", attrs={"class":"price-tag-fraction"})
    buscar_preço_centavos = produto.find("span", attrs={"class":"price-tag-cents"})
    if(buscar_preço_centavos):
         preço = f"R${buscar_preço_real.text},{buscar_preço_centavos.text}"
    else:
         preço = f"R${buscar_preço_real.text}"

    buscar_link = produto.find("a", attrs={"class": "ui-search-result__content ui-search-link"})
    link = buscar_link['href']
    prodtuoss.append([produto_nome, preço, link])


frame = pd.DataFrame(prodtuoss, columns=["Nome do Produto"," Preço do produto"," link do produto"])
frame.to_excel("produtos.xlsx")



    

   
