beatles = []
print("Etapa 1:", beatles) 

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

print("Etapa 2:", beatles)

for iCont in range(1,3):
   nome = input(f"Informe o Beatle {iCont}: ")
   beatles.append(nome)
   
print("Etapa 3:", beatles)   


del(beatles[-1])
del(beatles[len(beatles)-1])
print("Etapa 4:", beatles)   

beatles.insert(0,"Ringo Starr")
print("Etapa 5:", beatles)   

("o fabuloso", len(beatles))