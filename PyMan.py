import random
import re

# Mulige ord
words = "gravhund zebra æble leverpostej postmand regn skole aarhus letbane computer supporter datatekniker".split()

# Vælg ord
secret_word = random.choice(words)

# Variabler
incorrect_guesses = 0
guessed_letters = []
guess = ""

#Hangman fra https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# Spil loop
while True:

    # Viser ordets status
    current_state = ""
    for bogstav in secret_word:
        if bogstav in guessed_letters:
            current_state += bogstav
        else:
            current_state += "_"
    print(current_state)

    # enkelt bogstav input
    while guess == "" or len(guess) > 1 or not re.match("[a-zæøå]", guess, re.IGNORECASE):
        guess = input("Gæt et bogstav: ").lower()
        if guess == "" or len(guess) > 1 or not re.match("[a-zæøå]", guess, re.IGNORECASE):
            print("Prøv igen")
        else:
            break
    
    #tjek om bogstavet er i ordet
    if guess in secret_word:
        if guess in guessed_letters:
            print("Du har allerede gættet på det bogstav")
        
        else:
            guessed_letters.append(guess)
    else:
        if guess in guessed_letters:
            print("Du har allerede gættet på det bogstav")
        else:
            incorrect_guesses += 1
            guessed_letters.append(guess)
    guess = ""
    #print hangman figur
    print (HANGMANPICS[incorrect_guesses])
    
    
    
    #vis gættede bogstaver        
    print("Du har gættet på: ", guessed_letters)
    
    if all(letter in guessed_letters for letter in secret_word):
        print("Tillykke! Du vandt")
        print("Ordet var:", secret_word)
        break
    elif incorrect_guesses == 6:
        print("Han er død, ordet var:", secret_word)
        break
