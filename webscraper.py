import requests
from bs4 import BeautifulSoup

URL = input("Digite aqui seu link: ")

resposta = requests.get(URL)
status_requisição = resposta.status_code
conteudo_pagina = resposta.content

# Verifica se a requisição deu certo (código 200)
if status_requisição == 200:
    
    # CRIA A "SOPA": Analisa o conteúdo HTML da página
    sopa = BeautifulSoup(conteudo_pagina, 'html.parser')
    # procura o titulo da página
    titulo = sopa.title
    print(titulo.text)
    titulo_artigo = sopa.find('h2', class_="elementor-heading-title elementor-size-default")
    print(f"o título do artigo é: {titulo_artigo.text}")


else:
    print(f"Erro ao acessar a página. Código de status: {status_requisição}")