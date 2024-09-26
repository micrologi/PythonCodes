dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}
phone_numbers = {'chefe': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}
 
print(dictionary)
print(phone_numbers)
print(empty_dictionary)

print(phone_numbers['Suzy'])


#Percorrendo um dicionário
dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}
 
for key in dictionary.keys():
    print(key, "->", dictionary[key])
    
    
for english, french in dictionary.items():
    print(english, "->", french)    
    
    
dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}
 
dictionary['gato'] = 'minou'
print(dictionary)    



