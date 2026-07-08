segundos = int(input("Digite o tempo em segundos: "))

horas = segundos//3600
resto_segundos = segundos%3600
minutos = resto_segundos//60
segundos_faltando = resto_segundos%60

print("O valor de ", segundos, "em horas é de: ", horas, "horas", minutos, "minutos ", "e ", segundos_faltando, "segundos." )


