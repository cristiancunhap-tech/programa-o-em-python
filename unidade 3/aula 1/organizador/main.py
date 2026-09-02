import os
import shutil

pastas_e_arquivos = {
    "Imagens" : ["png", "jpeg", "jpg", "webp"],
    "Planilhas" : ["xls", "csv", "xlsx"],
    "Documentos" : ["docx", "pdf", "txt"]
}

pasta_alvo = "./Bagunça"
lista_arquivos = (os.listdir(pasta_alvo))

for arquivo in lista_arquivos:
    extensao = arquivo.split(".")[-1]