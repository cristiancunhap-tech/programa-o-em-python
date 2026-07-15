import os

numero_tentativas = 3
login_sucesso = False

while True:
    login_usuario = input("Digite o nome de usuario: ")
    login_senha = input("Digite a senha para o login: ")

    if (login_usuario == "Cristian") and (login_senha == "1234"):
        print("Login efetuado com sucesso!")
        login_sucesso = True
        break

    else:
        numero_tentativas -= 1

        if numero_tentativas == 0:
            print("Número máximo de tentativas atingido. Conta bloqueada.")
            break

        print(f"Usuário ou senha incorretos. Você tem {numero_tentativas} tentativas restantes.")

saldo_inicial = 0

def limpar():
    os.system("cls")

def saque(saldo):
    valor = int(input("Digite o valor desejado\n"))
    saldo -= valor
    return saldo

def deposito(saldo):
    valor = int(input("Digite o valor desejado\n"))
    saldo += valor
    return saldo

if login_sucesso:
    while True:
        escolha_usuario = int(input(
            "Menu\n"
            "1-Saldo\n"
            "2-Saque\n"
            "3-Deposito\n"
            "4-Sair\n"
        ))

        if escolha_usuario == 1:
            limpar()
            print(f"Saldo atual: R${saldo_inicial}")

        elif escolha_usuario == 2:
            saldo_inicial = saque(saldo_inicial)
            limpar()

        elif escolha_usuario == 3:
            saldo_inicial = deposito(saldo_inicial)
            limpar()

        elif escolha_usuario == 4:
            limpar()
            print("Obrigado por usar o nosso sistema.")
            break

        else:
            print("Opção inválida.")