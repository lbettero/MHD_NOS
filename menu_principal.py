
from web_scrapping import *
from aula1502 import*
from aula1602 import*

def caso_1():
    inicio=1000
    fim=1150
    site="http://www.nos.uminho.pt/History.aspx?id="
    web_scrapping(site, inicio, fim)
    menu()

def caso_2():
    converte_md("www.nos.uminho.pt","MDs")
    menu()

def caso_aula_15_02():
    aula1502()
    menu()

def caso_aula_16_02():
    aula1602()
    menu()

def caso_aula_16_02_b():
    aula1602_b()
    menu()

def sair():
    print("Até a próxima!")

switch={
    1: caso_1,
    2: caso_2,
    3: caso_aula_15_02,
    4: caso_aula_16_02,
    5: caso_aula_16_02_b,
    0: sair,
}

def menu():
    opcao = int(input("""Opções:\n1: para baixar todos os arquivos do site NOS\n
                      2: Converter os arquivos baixados em *.md\n
                      3: Aula_15_02 - Extrair o texto dos artigos dos htmls\n
                      4: Aula_16_02 - Extrair o texto dos artigos dos htmls\n
                      5: Aula_16_02b - Juntar os aruqivos de cabeçalho e artigo\n
                      0: Sair\n\n
                      Digite o número da opção desejada: """))

    if opcao in switch:
        switch[opcao]()
    else:
        print("Opção inválida. Escolha uma opção")
        menu()
