tem_idade = input("Você tem 18 anos ou mais? (Sim ou Não): ")
tem_habilitacao = input("Você possui habilitação? (Sim ou Não): ")

pode_dirigir = tem_idade == "Sim" and tem_habilitacao == "Sim"

if pode_dirigir:
    print("Você pode dirigir.")
else:
    print("Você não pode dirigir.")

