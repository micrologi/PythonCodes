for i in range(10):
   print("O valor de i é atualmente", i)

print()

for i in range(2, 8):
    print("O valor de i é atualmente", i)
    
    
print()

for i in range(2, 8, 3):
  print("O valor de i é atualmente", i)
  


#Sem saida:
for i in range(1, 1):
    print("O valor de i é atualmente", i)
    
    
# break - exemplo

print("The break instrução:")
for i in range(1, 6):
    if i == 3:
        break
    print("Dentro do laço.", i)
print("Fora do loop.")


# continue - exemplo

print("The continue instrução:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Dentro do laço.", i)
print("Fora do loop.")    