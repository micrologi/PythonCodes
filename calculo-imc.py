from click import clear
from math import pow
 
clear()
peso = float(input("Peso: "))
altura = float(input("Altura (Metros): "))

imc = peso / (altura ** 2)
#imc = peso / pow(altura,2)

#Arredondando o valor
print(f"Seu IMC é {round(imc,2)}.")


