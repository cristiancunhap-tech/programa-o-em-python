
def calculadora():

    PI = 3.14159

    while True:

        try:
            numero_selecionado = float(input("Digite um numero: "))
        except ValueError:
            print("Erro, Digite apenas numeros.")
            continue

        operacao_selecionada = input(
            "Digite a operação (+, -, *, /, potencia, raiz, radianos, graus): "
        ).lower()

        operacoes_validas = [
            "+", "-", "*", "/", "potencia", "raiz", "radianos", "graus"
        ]

        if operacao_selecionada not in operacoes_validas:
            print("Digite apenas as operações validas")
            continue
        
        if operacao_selecionada == "raiz":
            print(f"√{numero_selecionado} = {numero_selecionado ** 0.5}")

        elif operacao_selecionada == "radianos":
            print(f"{numero_selecionado}° = {numero_selecionado * PI / 180} rad")

        elif operacao_selecionada == "graus":
            print(f"{numero_selecionado} rad = {numero_selecionado * 180 / PI}°")

        else:
            
            try:
                numero_selecionado2 = float(input("Digite outro número: "))
            except ValueError:
                print("Erro, Digite apenas numeros.")
                continue

            if operacao_selecionada == "+":
                print(f"{numero_selecionado} + {numero_selecionado2} = {numero_selecionado + numero_selecionado2}")

            elif operacao_selecionada == "-":
                print(f"{numero_selecionado} - {numero_selecionado2} = {numero_selecionado - numero_selecionado2}")

            elif operacao_selecionada == "*":
                print(f"{numero_selecionado} * {numero_selecionado2} = {numero_selecionado * numero_selecionado2}")

            elif operacao_selecionada == "/":
                if numero_selecionado2 == 0:
                    print("Erro: não é possível dividir por zero.")
                else:
                    print(f"{numero_selecionado} / {numero_selecionado2} = {numero_selecionado / numero_selecionado2}")

            elif operacao_selecionada == "potencia":
                print(f"{numero_selecionado} ** {numero_selecionado2} = {numero_selecionado ** numero_selecionado2}")

            else:
                print("Operação inválida.")

        continuar = input("\nDeseja fazer outro cálculo? (sim/sair): ").lower()

        if continuar == "sair":
            print("Calculadora encerrada.")
            break


calculadora()


    
