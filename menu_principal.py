
from web_scrapping import *
from aula1502 import*
from aula1602 import*
from aula2202 import*
from aula2302 import*

def caso_1():
    inicio=1000
    fim=1150
    site="http://www.nos.uminho.pt/History.aspx?id="
    web_scrapping(site, inicio, fim)
    print("Download de arquivos completado.\n\n")
    menu()

def caso_2():
    converte_md("www.nos.uminho.pt","MDs")
    print("Arquivos convertidos em *.md.\n\n")
    menu()

def caso_aula_15_02():
    aula1502()
    print("Textos extraídos dos htmls.\n\n")
    menu()

def caso_aula_16_02():
    aula1602()
    print("Metadados extraídos dos htmls.\n\n")
    menu()

def caso_aula_16_02_b():
    aula1602_b("aula1602","aula1602_b", "aula1502")
    print("Arquivos unificados em um único *.txt.\n\n")
    menu()

def caso_aula_22_02():
    aula2202()
    print("Imagens de slides extraídas e adicionadas ao cabeçalho\n\n")
    menu()

def caso_aula_23_02():
    aula2302()
    aula1602_b("aula2202","aula2302_b","aula2302")
    print("Textos extraídos dos htmls com alterações nas tags.\n\n")
    menu()

def caso_aula_23_02_b():
    aula2302_b()
    menu()

def sair():
    print("Até a próxima!")

switch={
    1: caso_1,
    2: caso_2,
    3: caso_aula_15_02,
    4: caso_aula_16_02,
    5: caso_aula_16_02_b,
    6: caso_aula_22_02,
    7: caso_aula_23_02,
    8: caso_aula_23_02_b,
    0: sair,
}

def menu():
    opcao = int(input("""Opções:\n
                      1: para baixar todos os arquivos do site NOS\n
                      2: Converter os arquivos baixados em *.md\n
                      3: Aula_15_02 - Extrair o texto dos artigos dos htmls\n
                      4: Aula_16_02 - Extrair metadados dos artigos dos htmls\n
                      5: Aula_16_02b - Juntar os arquivos de cabeçalho e artigo\n
                      6: Aula_22_02 - Extrair os nomes das imagens dos htmls e adicionar ao cabeçalho\n
                      7: Aula_23_02 - Extrair o texto dos artigos dos htmls com alterações nas Tags\n
                      8: Aula_23_02b - Testes adicionais\n
                      0: Sair\n\n
                      Digite o número da opção desejada: """))

    if opcao in switch:
        switch[opcao]()
    else:
        print("Opção inválida. Escolha uma opção")
        menu()
