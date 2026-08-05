time = {
    "Nome": "Vasco da Gama",
    "Sigla": "crvg",
    "Campeonatos": "Serie A",
    "Libertadores": 1,
    "Estrutura": "SAF",
}

print(time.get("Nome"))


time["Lugar"] = "Rio de Janeiro"
time.update({"Campeonatos" : "Sulamericana"})
time.pop("Estrutura")


lista_chaves = time.keys()
for chave in lista_chaves:
    print(chave)


