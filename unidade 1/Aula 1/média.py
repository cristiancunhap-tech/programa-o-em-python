primeira_nota = float(input("Digite a primeira nota: "))
segunda_nota = float(input("Digite a segunda nota: "))
terceira_nota = float(input("Digite a terceira nota: "))

nota_final = (primeira_nota + segunda_nota + terceira_nota) / 3

if nota_final >= 7:
    print("Aprovado")
else:
    print("Reprovado")