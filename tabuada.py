'''
Para debugar código Python, podemos seguir as etapas:
   - Adicione um breakpoint clicando no lado esquerdo da linha
   - Clique F5 para iniciar o debug
   - Clique F10 para ir executando linha por linha
'''

tabuada = 2
valor = 1
for iCont in range(0,11,1):
   valor = tabuada * iCont
   print(tabuada, ' x ', iCont, ' = ', valor)