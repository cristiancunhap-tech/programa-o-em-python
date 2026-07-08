import random

escolha_jogador = int(input("1- pedra , 2- papel, 3- tesoura"))
escolha_computador = random.randint(1,3)
print("Escolha do jogador: ", escolha_jogador)
print("Escolha do computador: ", escolha_computador)

if escolha_jogador == escolha_computador:
    print("Empate")


  
