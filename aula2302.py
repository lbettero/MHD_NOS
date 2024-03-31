from jjcli import *
from bs4 import BeautifulSoup as bs
from grava_resultados import *
import os

def aula2302():
    ats= glob("www.nos.uminho.pt/Article.aspx*")
    #print (ats)

    def proc_article(html):
        a=bs(html) # cria uma árvore documental
        #print(a)
        art= a.find("div", id="artigo") #procura no html
        for tag in art.find_all("div", class_="voltar"): tag.extract()
        for tag in art.find_all("div", id="slidesjs-log"): tag.decompose()
        for tag in art.find_all("ul", class_="socialcount"): tag.decompose()
        for tag in art.find_all("div", id="slides"):
            slides = tag.extract()
        for tag in art.find_all("table"):
            tag.insert(0, "\n## TABELA")
        for tag in art.find_all("strong"):
            tag.name = "b"
        try:
            texto=(art.get_text())
            #print (texto)
            arquivo_origem = file.split(".")
            arquivo_destino = arquivo_origem[3][3:]+"-"+arquivo_origem[-1][-4:]
            grava_resultado(texto,arquivo_destino,"aula2302")
        except Exception as e:
            pass

    for file in ats:
        with open(file, encoding="utf-8") as f:
            html= f.read() 
        proc_article (html)

def aula2302_b():
    arquivos=os.listdir("aula2302_b")
    for arquivo in arquivos:
        with open ("aula2302_b/"+arquivo,"r", encoding="utf-8") as f:
            texto=f.read()
        linhas_texto=texto.splitlines()
        fim_cabeçalho=linhas_texto.index("---")
        inicio_materia=fim_cabeçalho+4
        caracteres_totais=sum(len(caracter) for caracter in linhas_texto[inicio_materia:])
        palavras_totais=0
        for linha in linhas_texto[inicio_materia:]:
            linha_quebrada=linha.split(" ")
            palavras_totais+=len(linha_quebrada)
        linhas_texto.insert(fim_cabeçalho,"Caracteres Totais: "+str(caracteres_totais))
        linhas_texto.insert(fim_cabeçalho,"Palavras Totais: "+str(palavras_totais))

        grava_resultado(linhas_texto,arquivo,"aula2302_c")

