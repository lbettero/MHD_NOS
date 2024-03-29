import os
import re

def le_arquivos_fonte(arquivo):
    with open (arquivo, "r", encoding="utf-8") as entrada:
        return(entrada.read())
