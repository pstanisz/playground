#!/usr/bin/python3

import random

word_list = ["Angel", "Devil", "Wizard", "Dragon"]

word = random.choice(word_list)
word_len = len(word)

hidden_word = []
for _ in range(word_len):
  hidden_word += "_"
  
print(hidden_word)

guess_count = 10
all_letters_known = False

while guess_count > 0 and not all_letters_known:

    guess  = input("Guess a letter: ").lower()

    for position in range(word_len):
        letter = word[position]
        if letter.lower() == guess:
            hidden_word[position] = letter
            
    print(hidden_word)
    
    if hidden_word.count("_") == 0:
        all_letters_known = True
        
    guess_count -= 1
    
if all_letters_known:
    print("You win :)")
else:
    print("You lose :(")
  