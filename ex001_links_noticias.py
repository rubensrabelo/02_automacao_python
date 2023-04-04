import requests
from bs4 import BeautifulSoup

url = 'https://noticias.uol.com.br/'

solicitacao = requests.get(url).content

site = BeautifulSoup(solicitacao, 'html.parser')

noticias = site.find_all('div', attrs={'class': 'thumbnails-item'})

lista_noticias = []
cont = 0

for noticia in noticias:
    tituloNoticia = noticia.find('a')

    if(tituloNoticia['href']):
        linkNoticia = tituloNoticia['href']
        lista_noticias.append([tituloNoticia.text, linkNoticia])
    else:
        lista_noticias.append([tituloNoticia.text, ''])

    if cont > 8:
        break
    cont = cont + 1

import pandas as pd

df = pd.DataFrame(lista_noticias, columns=['Titulo', 'Link_Noticia'])

df.to_excel('10_noticias.xlsx', index=False)