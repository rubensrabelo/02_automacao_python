import requests
from bs4 import BeautifulSoup

url = 'https://www.estantevirtual.com.br/livros-mais-vendidos'
solicitacao = requests.get(url).content

site = BeautifulSoup(solicitacao, 'html.parser')

livro = site.find('a', attrs={'class': 'info'})

titulo = livro.find('h2', attrs={'class': 'titulo-livro'}).text.strip()
autor = livro.find('h3', attrs={'class': 'autor-livro'}).text.strip()
preco = livro.find('span', attrs={'class': 'preco'}).text.strip()

print(f'O livro {titulo} foi escrito por {autor}, e o seu preço atual é {preco[12:]}.')
