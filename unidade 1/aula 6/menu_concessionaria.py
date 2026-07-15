idade_cliente = int(input("Digite a sua idade: "))

def exibir_menu_infantil():
    print("Relâmpago Marquinhos")
    print("Hotwheels")
    print("Patrulha Canina")
    print("Thomas e seus amigos")

def exibir_menu_normal():
    print("Toyota -> a partir de R$ 180.000")
    print("Mercedes -> A partir de R$ 300.000")
    print("Fiat -> A partir de R$ 70.000")

def checar_idade(idade_cliente):
    if idade_cliente < 18:
        exibir_menu_infantil()
    else:
        exibir_menu_normal()


checar_idade(idade_cliente)


