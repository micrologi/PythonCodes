blocos = int(input("Numero de blocos: "))

qtd_linha = 1
altura = 0
while blocos > 0:

   if (blocos >= qtd_linha):
      altura+=1
   
   blocos-=qtd_linha
   qtd_linha+=1
   
print(altura)