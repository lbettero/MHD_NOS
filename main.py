from web_scrapping import *
from aula1502 import*

def caso_1():
    inicio=1000
    fim=1150
    site="http://www.nos.uminho.pt/History.aspx?id="
    web_scrapping(site, inicio, fim)

def caso_2():
    converte_md("www.nos.uminho.pt","MDs")

def caso_aula_15_02():
    aula1502()

switch={
    1: caso_1,
    2: caso_2,
    3: caso_aula_15_02,
}

opcao = int(input("Opções:\n1: para baixar todos os arquivos do site NOS\n2: para converter os arquivos baixados em *.md\n3: caso_aula_15_02 - Extrai o texto dos artigos dos htmls"))

if opcao in switch:
    switch[opcao]()
else:
    print("Opção inválida")
