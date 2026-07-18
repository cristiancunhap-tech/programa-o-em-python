vetor = []

for i in range(6):
    numero = int(input(f"Digite o {i + 1}o número: "))
    vetor.append(numero)

print("Os números digitados foram:")

for numero in vetor:
    print(numero)