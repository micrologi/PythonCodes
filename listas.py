numbers = [10, 5, 7, 2, 1]
print("Conteúdos originais da lista:", numbers)  # Imprimindo o conteúdo original da lista.
 
numbers[0] = 111
print("Novo conteúdo da lista: ", numbers)  # Conteúdo atual da lista.

print(len(numbers))

del numbers[1]
print(numbers)

numbers = [111, 7, 2, 1]
print(numbers[-1])