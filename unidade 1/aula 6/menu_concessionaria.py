idade_cliente = int(input("Digite a sua idade: "))

def exibir_menu_infantil():
    menu_infantil = [ "Relampago Marquinhos", "Hotwheels", "Patrulha Canina", "Thomas e seus amigos" ]
    for item in menu_infantil:
        print(item)


def exibir_menu_normal():
    menu_normal = [ "Toyota -> a partir de R$ 180.000", "Mercedes -> A partir de R$ 300.000", "Fiat -> A partir de R$ 70.000"]
    for item in menu_normal:
        print(item)
   

def checar_idade(idade_cliente):
    if idade_cliente < 18:
        exibir_menu_infantil()
    else:
        exibir_menu_normal()


checar_idade(idade_cliente)


