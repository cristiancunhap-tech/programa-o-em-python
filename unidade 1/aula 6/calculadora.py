def calculadora():

    numero_selecionado = float(input("Digite um número: "))
    operacao_selecionada = input("Digite a operação que deseja usar: ")

    PI = 3.14159

    if operacao_selecionada == "raiz":
        print(f"√{numero_selecionado} = {numero_selecionado ** 0.5}")

    elif operacao_selecionada == "radianos":
        print(f"{numero_selecionado}° = {numero_selecionado * PI / 180} rad")

    elif operacao_selecionada == "graus":
        print(f"{numero_selecionado} rad = {numero_selecionado * 180 / PI}°")

    else:
        numero_selecionado2 = float(input("Digite outro número: "))

        if operacao_selecionada == "+":
            print(f"{numero_selecionado} + {numero_selecionado2} = {numero_selecionado + numero_selecionado2}")

        elif operacao_selecionada == "-":
            print(f"{numero_selecionado} - {numero_selecionado2} = {numero_selecionado - numero_selecionado2}")

        elif operacao_selecionada == "*":
            print(f"{numero_selecionado} * {numero_selecionado2} = {numero_selecionado * numero_selecionado2}")

        elif operacao_selecionada == "/":
            print(f"{numero_selecionado} / {numero_selecionado2} = {numero_selecionado / numero_selecionado2}")

        elif operacao_selecionada == "potencia":
            print(f"{numero_selecionado} ** {numero_selecionado2} = {numero_selecionado ** numero_selecionado2}")

        else:
            print("Operação inválida.")


calculadora()



    
