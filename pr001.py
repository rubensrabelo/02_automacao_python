#link: https://www.youtube.com/watch?v=lVHojLys4l8

import requests
from bs4 import BeautifulSoup

url = 'https://www.google.com/search?q=dolar&oq=dolar&aqs=chrome..69i57j0i131i433i512l6j0i131i433i650j0i131i433i512j0i3.894j0j7&sourceid=chrome&ie=UTF-8'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}

solicitacao = requests.get(url, headers=headers).content

#print(solicitacao)

soup = BeautifulSoup(solicitacao, 'html.parser')

respostas = soup.find('span', attrs={'class': 'DFlfde SwHCTb'})

print(respostas['data-value'])