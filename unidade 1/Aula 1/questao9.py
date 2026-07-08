salario = float(input("Digite o seu salário: "))
desconto_vale_transporte = salario * 0.06 
desconto_plano_saude = salario * 0.03

salario_final = salario - desconto_plano_saude - desconto_vale_transporte


print("Seu desconto de transporte é de: ", desconto_vale_transporte)
print("=====")
print("Seu desconto de saúde é de: ", desconto_plano_saude)
print("=====")
print("Seu salario e de: ", salario_final)