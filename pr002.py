import requests
import os

def baixar_arquivo(url, endereco):
    resposta = requests.get(url)
    if resposta.status_code == requests.codes.ok: 
        with open(endereco, 'wb') as arquivo:
            arquivo.write(resposta.content)
    else:
        resposta.raise_for_status()

if __name__ == '__main__':
    url = 'https://math.mit.edu/classes/18.745/Notes/Lecture_{}_Notes.pdf'
    saida = 'pastaArquivos'

    for i in range(1, 26):
        nome_arquivo = os.path.join(saida, f'nota_de_aula_{i}.pdf')
        baixar_arquivo(url.format(i), nome_arquivo) 