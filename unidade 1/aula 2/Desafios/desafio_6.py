nota_1 = float(input("Digite sua primeira nota "))
nota_2 = float(input("Digite sua segunda nota "))

media_notas = (nota_1 + nota_2) / 2

if media_notas >= 7:
    print("Aluno aprovado direto")
if media_notas < 4:
    print("Aluno reprovado")
if media_notas > 4 and media_notas < 7:
    print("Aluno em recuperacao")
    nota_recuperacao = float(input("Digite a nota da sua recuperacao: "))
    if nota_recuperacao < 5:
        print("Reprovado na recuperacao")
    else:
        print("Aprovado na recuperacao")  



