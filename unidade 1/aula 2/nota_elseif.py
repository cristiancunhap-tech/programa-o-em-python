nota_final = int(input("Digite sua nota final"))

if nota_final >=90:
    print("Aprovado, Parabens pela nota!")
elif nota_final >=60:
    print("Aprovado")
elif nota_final > 60:
    print("Recuperação")
else:
    print("Reprovado")
