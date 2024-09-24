
user_word = input("Digite a palavra: ")
user_word = user_word.upper()

for letter in user_word:
   if (letter not in 'AEIOU'):
      print(letter,end="")