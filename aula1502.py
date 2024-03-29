from jjcli import *
from bs4 import BeautifulSoup as bs

def aula1502():
    ats= glob("www.nos.uminho.pt/Article.aspx*")
    print (ats)

    def proc_article(html):
        a=bs(html) # cria uma árvore documental
        print(a)
        art= a.find("div", id="artigo") #procura no html
        print ("=========\n", art.get_text()) #get_text - Retira apenas o texto mesmo, sem html
        
    for file in ats:
        with open(file, encoding="utf-8") as f:
            html= f.read() 
        proc_article (html)