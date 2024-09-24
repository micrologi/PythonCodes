secret_number = 777

numero = 0
while numero != secret_number:
   numero = int(input("Informe o numero: "))
   if numero == secret_number:
      print("Muito bem, trouxa! Você está livre agora.")
   else:
      print("Você está preso no meu loop!")
