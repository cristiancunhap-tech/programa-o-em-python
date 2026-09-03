import os
import shutil

pastas_e_arquivos = {
    "Imagens": ["png", "jpeg", "jpg", "webp"],
    "Planilhas": ["xls", "csv", "xlsx"],
    "Documentos": ["docx", "pdf", "txt"]
}

pasta_alvo = "./Bagunça/"
lista_arquivos = os.listdir(pasta_alvo)

for chave in pastas_e_arquivos.keys():
    caminho_pasta = os.path.join(pasta_alvo, chave)

    if not os.path.exists(caminho_pasta):
        os.makedirs(caminho_pasta)

for arquivo in lista_arquivos:
    extensao = arquivo.split(".")[-1]

    for chave in pastas_e_arquivos.keys():

        if extensao in pastas_e_arquivos[chave]:
            path_origem = os.path.join(pasta_alvo, arquivo)
            path_destino = os.path.join(pasta_alvo, chave)
            shutil.move(path_origem, path_destino)