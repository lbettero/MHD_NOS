from jjcli import *
from bs4 import BeautifulSoup as bs
from grava_resultados import *
import requests
from le_arquivos import*
import os

def aula1602():
    
    ats= glob("www.nos.uminho.pt/Article.aspx*")

    #BUSCA PELOS METADADOS NOS ARQUIVOS ORIGINAIS
    def busca_meta_dados(html):
        a=bs(html) # cria uma árvore documental
        cabecalho=""
        for meta in a.find_all("meta"):
            atributo = meta.get("property")
            if atributo is None:
                continue
            atributo = atributo.replace("og:","") #para remover a o pedaço de texto indesejado
            cabecalho+= f"{atributo}: {meta.get('content')}\n"
        arquivo_origem = file.split(".")
        arquivo_destino = arquivo_origem[3][3:]+"-"+arquivo_origem[-1][-4:]
        grava_resultado(cabecalho,arquivo_destino,"aula1602")


    for file in ats:
        with open(file, encoding="utf-8") as f:
            html= f.read() 
        busca_meta_dados(html)

def aula1602_b():
    fonte_cabecalho="aula1602"
    fonte_artigo="aula1502"
    arquivos=os.listdir(fonte_cabecalho)
    for arquivo in arquivos:
        with open (fonte_cabecalho+"/"+arquivo, encoding="utf-8") as cabecalho_in:
            texto=cabecalho_in.read()
            texto_completo=texto.splitlines()
            texto_completo.append("---")
            with open (fonte_artigo+"/"+arquivo, encoding="utf-8") as artigo_in:
                texto=artigo_in.read()
                artigo=texto.splitlines()
                for linha in artigo:
                    if linha != "" and "voltar à página anterior" not in linha and len(linha)>3:
                        texto_completo.append(linha)
        grava_resultado(texto_completo,arquivo,"aula1602_b")