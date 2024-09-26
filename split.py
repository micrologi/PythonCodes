import os
os.system('cls')

notas = [float(i) for i in input('Nota (Trabalho,Prova): ').split(',')]

print(notas)

soma = 0
for nota in notas:
    soma += nota
    
print(soma / len(notas))