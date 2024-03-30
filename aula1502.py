from jjcli import *
from bs4 import BeautifulSoup as bs
from grava_resultados import *

def aula1502():
    ats= glob("www.nos.uminho.pt/Article.aspx*")
    #print (ats)

    def proc_article(html):
        a=bs(html) # cria uma árvore documental
        #print(a)
        art= a.find("div", id="artigo") #procura no html
        try:
            texto=(art.get_text())
            #print (texto)
            arquivo_origem = file.split(".")
            arquivo_destino = arquivo_origem[3][3:]+"-"+arquivo_origem[-1][-4:]
            grava_resultado(texto,arquivo_destino,"aula1502")
        except Exception as e:
            pass

    for file in ats:
        with open(file, encoding="utf-8") as f:
            html= f.read() 
        proc_article (html)