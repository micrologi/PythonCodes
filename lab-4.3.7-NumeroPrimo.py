def is_prime(num):
   for iCont in range(2,101,1):
      if (num % iCont == 0) and (iCont != num):
         return False
   return True
      

for i in range(1, 20):
   if is_prime(i + 1):
      print(i + 1, end=" ")

print()