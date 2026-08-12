import plyer


estoque = []

def menu():
    print(
        "O que deseja fazer?\n"
        "1 - Adicionar produto\n"
        "2 - Listar produtos\n"
        "3 - Somar total\n"
        "4 - Checar produtos com qtd abaixo\n"
        "5 - Finalizar sessão"
    )

    opcao = int(input("Escolha uma opção: "))
    return opcao

def cadastrar_produto ():
    try:
        produto = {
        "tipo": input("Digite o nome do produto: "),
        "preco": float(input("Digite o preço do produto: ")),
        "quantidade": int(input("Digite a quantidade do produto: "))
    }
    except:
        print("Algo deu errado. Tente novamente")

    estoque.append(produto)
    notificacao_produto()
    
def listar_produto ():
    for produto in estoque:
        print(produto)


def somar_quantidade_total():
    total_geral = 0

    for produto in estoque:
        total_geral += produto["quantidade"]

    for produto in estoque:
        print(f"{produto["tipo"]} - {produto["quantidade"]}")
    
    print(f"Total geral do estoque: {total_geral} ")

def produtos_abaixo_minimo():
    for produto in estoque:
        if produto["quantidade"] < 50:
            print(f"{produto['tipo']} está abaixo do mínimo do estoque.")
        
def notificacao_produto():
    plyer.notification.notify(
        title = "Novo produto",
        message = "Um novo produto foi adicionado ao estoque!",
        timeout = 5
    )
    
while True:
    opcao = menu()
    print(f"Voce escolheu {opcao}")

    if opcao == 1:
        cadastrar_produto()
    
    elif opcao == 2:
        listar_produto()
    
    elif opcao == 3:
        somar_quantidade_total()
    
    elif opcao == 4:
        produtos_abaixo_minimo()

    elif opcao == 5:
        print("Encerrando o programa...")
        break

        







        