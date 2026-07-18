vetor = []
soma = 0

for i in range(10):
    numero = float(input(f"Digite o {i + 1}º número: "))
    vetor.append(numero)
    soma += numero

media = soma / len(vetor)

print(f"Soma dos números foi de {soma}")
print(f"Média dos números foi de {media}")