import os
os.system('cls')

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

for iCont in range(len(my_list)-1):
   for iCont2 in range(iCont,len(my_list)-1-iCont):
      print(iCont2)
      if my_list[iCont2] == my_list[iCont]:
         del my_list[iCont2]
      
print("A lista com os elementos exclusivos aqui")
print(my_list)
