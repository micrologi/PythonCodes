def liters_100km_to_miles_gallon(liters):
   milha = 1609.344 
   galao = 3.785411784 

   return ((1000 / liters) * (galao * 100)) / milha
   
 
def miles_gallon_to_liters_100km(miles):
   milha = 1609.344 
   galao = 3.785411784 

   return ((galao * 100) * 1000) / (miles * milha)   


print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))