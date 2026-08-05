import random

mapa_jogador = [
    ["~","~","~"],
    ["~","~","~"],
    ["~","~","~"]
]

mapa_computador = [
    ["~","~","~"],
    ["~","~","~"],
    ["~","~","~"]
]

print("Onde colocar o barquinho?")
LINHA_INICIAL_JOGADOR = int(input("Escolha uma linha: "))
COLUNA_INICIAL_JOGADOR = int(input("Escolha uma coluna: "))

mapa_jogador[LINHA_INICIAL_JOGADOR][COLUNA_INICIAL_JOGADOR] = "O"

escolha_linha_computador = random.randint(0,2)
escolha_coluna_computador = random.randint(0,2)

while True:
    print("\nSua vez de atacar!")

    while True:
        escolha_linha_jogador = int(input("Escolha uma linha: "))
        escolha_coluna_jogador = int(input("Escolha uma coluna: "))

        if mapa_computador[escolha_linha_jogador][escolha_coluna_jogador] == "X":
            print("Você já atacou essa posição! Escolha outra.")
        else:
            break

    if (escolha_linha_jogador == escolha_linha_computador) and (escolha_coluna_jogador == escolha_coluna_computador):
        print("Você ganhou!")
        break
    else:
        print("Você errou!")
        mapa_computador[escolha_linha_jogador][escolha_coluna_jogador] = "X"

        print("\nMapa do computador:")
        print("   0  1  2")
        for i, linha in enumerate(mapa_computador):
            print(f"{i}  " + "  ".join(linha))

    print("\nÉ a vez do computador!")
    escolha_linha_computador = random.randint(0,2)
    escolha_coluna_computador = random.randint(0,2)

    if escolha_linha_computador == LINHA_INICIAL_JOGADOR and escolha_coluna_computador == COLUNA_INICIAL_JOGADOR:
        print("Você perdeu!")
        break
    else:
        mapa_jogador[escolha_linha_computador][escolha_coluna_computador] = "X"

        print("\nMapa do jogador:")
        print("   0  1  2")
        for i, linha in enumerate(mapa_jogador):
            print(f"{i}  " + "  ".join(linha))