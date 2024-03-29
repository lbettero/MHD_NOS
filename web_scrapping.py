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

def converte_md(pasta_origem, pasta_destino):

    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)

    arquivos = os.listdir(pasta_origem)

    for arquivo in arquivos:
        print(arquivo)
        origem = os.path.join(pasta_origem, arquivo)
        nome_fim = arquivo + ".md"
        caminho_saida = os.path.join(pasta_origem, nome_fim)
        comando = f"pandoc -f html {origem} -o {caminho_saida}"
        subprocess.run(comando, shell=True)