peso_atual = float(input("Digite o seu peso aqui: "))
altura_atual = float(input("Digite a sua altura aqui: "))

imc_atual = peso_atual / (altura_atual ** 2)

if imc_atual >25:
    print("Voce esta acima do peso")
else:
    print("Voce nao esta acima do peso")