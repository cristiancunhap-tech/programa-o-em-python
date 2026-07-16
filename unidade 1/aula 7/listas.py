lista_de_compras = ["Maçã", "Uva"]

lista_de_compras.append("Café")


lista_de_compras.insert(0,"Pão")

segunda_lista = ["Manteiga"]
lista_de_compras.extend(segunda_lista)
print(lista_de_compras)

lista_de_compras.remove("Café")
print(lista_de_compras)

lista_de_compras.pop(0)
print(lista_de_compras)

lista_de_compras.clear()
print(lista_de_compras)


lista_numeros = [5, 4, 3, 2, 1]
len(lista_numeros)
print(len (lista_numeros))

lista_numeros.sort()
print(lista_numeros)

lista_numeros.reverse()
print(lista_numeros)