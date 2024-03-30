from jjcli import *
from bs4 import BeautifulSoup as bs
from grava_resultados import *
import requests
from le_arquivos import*
import os
from aula1602 import aula1602_b

def aula2202():
    
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
        #Outro modo de extrair a data e o nome do autor da entrevista / matéria
        #buscando diretamente no HTML em vez do txt extraído.
        try:
            obter_data=a.find("span", id="ctl00_ContentPlaceHolder1_LabelInfo").text #obter o span de id ctl00_ContentPlaceHolder1_LabelInfo
            extrair_data=obter_data[:10]#obter os dez primeiros caracteres, correspondentes à data
            cabecalho+= f"data: {extrair_data}\n"#coloca a data no cabeçalho
            autor=obter_data.split(" | ") #aproveita a ocorrência do nome do autor logo após a data
            obter_autor=autor[-1][:] #retira apenas o nome do autor da string original
            cabecalho+= f"autor: {obter_autor}\n"#adiciona o nome do autor ao cabeçalho
        except Exception as e:
            pass
        
        art= a.find("div", id="artigo") #procura
        obter_slides = art.find("div", {'id':'slides'}) # ir ao div de id slides pois contém todas as imagens que queremos
        if obter_slides is not None: # caso exista div de id slides procurar pelas imagens
            for slide in obter_slides.find_all("div", {'class':'slide'}): # percorrer todos os div class slide pois contém todas as imagens que queremos
                imagem = slide.find('img') # obter a imagem
                cabecalho += f"{imagem['src']}\n" # adicionar imagem ao cabeçalho

        cabecalho+=f"---\n"
        arquivo_origem = file.split(".")
        arquivo_destino = arquivo_origem[3][3:]+"-"+arquivo_origem[-1][-4:]
        grava_resultado(cabecalho,arquivo_destino,"aula2202")

    for file in ats:
        with open(file, encoding="utf-8") as f:
            html= f.read()
        busca_meta_dados(html)

    aula1602_b("aula2202","aula2202_b","aula1502")