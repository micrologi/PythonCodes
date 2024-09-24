horas = int(input("Horas: "))
minutos = int(input("Minutos: "))
minadd = int(input("Minutos Adicionais: "))

qtdhoras = (minutos + minadd) // 60
restminutos = (minutos + minadd) % 60

somahoras = (horas + qtdhoras) % 24

print(somahoras, restminutos, sep=":")
