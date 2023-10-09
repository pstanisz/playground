#!/usr/bin/python3

import random
import os
import sys
from getopt import getopt
from resources import logo, stages, win, win_text, lose_text, welcome_text, guess_text
from words import word_list

# EN by default
lang_opt = "en"

opts, args = getopt(sys.argv[1:],'l:',['language='])
for option, argument in opts:
    if option == '-l':
        lang_opt = argument.lower()

if lang_opt == "pl":
    lang = 1
else:
    lang = 0

print(logo[lang])
print(input(welcome_text[lang]))
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
    
    guess = input(guess_text[lang]).lower()
    
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
    print(win_text[lang])
else:
    print(stages[0])
    print(lose_text[lang])
