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
        cabecalho+=f"---\n"




        arquivo_origem = file.split(".")
        arquivo_destino = arquivo_origem[3][3:]+"-"+arquivo_origem[-1][-4:]
        grava_resultado(cabecalho,arquivo_destino,"aula1602")

    for file in ats:
        with open(file, encoding="utf-8") as f:
            html= f.read() 
        busca_meta_dados(html)

#ECERCÍCIO 1: PROCURAR AS DATAS, COLOCANDO-AS NO CABEÇALHO
#Obs. Adicionalmente foram encontrados os nomes dos autores das entrevistas/entrevistadores,
#que também foram colocados no cabeçalho

def aula1602_b():
    fonte_cabecalho="aula1602"
    fonte_artigo="aula1502"
    arquivos=os.listdir(fonte_cabecalho)
    for arquivo in arquivos:
        with open (fonte_cabecalho+"/"+arquivo, encoding="utf-8") as cabecalho_in:
            texto=cabecalho_in.read()
            texto_completo=texto.splitlines()
            try:
                with open (fonte_artigo+"/"+arquivo, encoding="utf-8") as artigo_in:
                    texto=artigo_in.read()
                    artigo=texto.splitlines()
                    #BLOCO DESATIVADO AO ADICIONAR A VERSÃO FEITA NA AULA DE 22 DE FEVEREIRO
                    #for linha in artigo:
                    #    if "|" in linha:
                    #        autor=linha.split(" | ")
                    #        texto_completo.append("data: "+autor[0][:])
                    #        texto_completo.append("autor: "+autor[-1][:])
                    #texto_completo.append("---")
                    for linha in artigo:
                        if linha != "" and "voltar à página anterior" not in linha and len(linha)>3:
                            texto_completo.append(linha)
            except Exception as e:
                pass
        grava_resultado(texto_completo,arquivo,"aula1602_b")