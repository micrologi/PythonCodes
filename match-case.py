dia = int(input("Informe um nº entre 1 e 7: "))

match dia:
   case 1:
      print("Domingo")
   case 2:
      print("Segunda")      
   case 3:
      print("Terça")      
   case 4:
      print("Quarta")                  
   case 5 | 6 | 7:
      print("Depois de quarta")
   case _:
      print("Opção inválida")

                  