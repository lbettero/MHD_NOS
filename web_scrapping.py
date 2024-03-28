from jjcli import *

def web_scrapping(site, inicio, fim):
    indisponiveis=[]
    for n in range(inicio,fim):
        try:
            comando = f'wget -r -c -l 2 "{site}{n}"'
            qxsystem(comando)
        except Exception as e:
            pass