import pyfiglet

frase = input("Digite uma frase: ")
frase_formatada = pyfiglet.figlet_format(frase)

print(frase_formatada)