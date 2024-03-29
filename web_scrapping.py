from jjcli import *
import subprocess
import os

def web_scrapping(site, inicio, fim):
    indisponiveis=[]
    for n in range(inicio,fim):
        try:
            comando = f'wget -r -c -l 2 "{site}{n}"'
            qxsystem(comando)
        except Exception as e:
            pass

def converte_md(pastaorigem, pastadestino):

    if not os.path.exists(pastadestino):
        os.makedirs(pastadestino)

    arquivos = os.listdir(pastaorigem)

    for arquivo in arquivos:
        print(arquivo)
        origem = os.path.join(pastaorigem, arquivo)
        nomefim = arquivo + ".md"
        caminho_saida = os.path.join(pastadestino, nomefim)
        comando = f"pandoc -f html {origem} -o {caminho_saida}"
        subprocess.run(comando, shell=True)