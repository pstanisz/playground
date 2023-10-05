#!/usr/bin/python3

import random
import os
from resources import logo, stages, win
from words import word_list

print(logo)
print(input("Press any key to start..."))
os.system('clear')

word = random.choice(word_list)
word_len = len(word)

hidden_word = []
for _ in range(word_len):
    hidden_word += "_"

guess_count = len(stages) - 1
all_letters_known = False

while guess_count > 0 and not all_letters_known:
    print(hidden_word)
    print("\n")
    print(stages[guess_count])
    
    guess = input("Guess a letter: ").lower()
    
    os.system('clear')

    for position in range(word_len):
        letter = word[position]
        if letter.lower() == guess:
            hidden_word[position] = letter

    if guess not in word.lower():
        guess_count -= 1

    if hidden_word.count("_") == 0:
        all_letters_known = True

print(hidden_word)
print("\n")

if all_letters_known:
    print(win)
    print("You win :)")
else:
    print(stages[0])
    print("You lose :(")
