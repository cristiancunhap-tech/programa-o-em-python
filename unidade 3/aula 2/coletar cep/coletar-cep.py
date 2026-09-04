import requests

cep_usuario = input("Digite o seu CEP: ")

url = f"https://viacep.com.br/ws/{cep_usuario}/json/"

resposta = requests.get(url)

dados = resposta.json()

print(dados)

