import random

word_list = ["apple", "banana", "python", "hangman", "programming"]

chosen_word = random.choice(word_list).lower()
print(chosen_word)

guess = input("Enter a letter to guess").__str__().lower()

for guess in chosen_word:
    if guess in chosen_word:
        print("Right")
    else:
        print("Wrong")

placeholder = ""

word_length = len(chosen_word)

for position in range(word_length):
    placeholder += "_"
print(placeholder)

display = ""

for letter in chosen_word:
    if guess in chosen_word:
        placeholder = str.replace(chosen_word[])