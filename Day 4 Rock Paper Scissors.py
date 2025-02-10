import random

user_input = input("What do you choose? Type 0 for Rock, 1 for Paper  or 2 for Scissors")

print(f"You chose: {user_input}")

scissors = "2"
rock = "0"
paper = "1"

choice_list = [scissors,rock,paper]

ai_choice = random.choice(choice_list)

print(f"The AI Chose: {ai_choice}")

if user_input == ai_choice:
    print("Its a draw")
elif user_input == rock and ai_choice == scissors:
    print("You win")
elif user_input == scissors and ai_choice == rock:
    print("You lose")
elif user_input == scissors and ai_choice == paper:
    print("You win")
elif user_input == paper and ai_choice == scissors:
    print("You lose")
elif user_input == paper and ai_choice == rock:
    print("You win")
elif user_input == rock and ai_choice == paper:
    print("You lose")
else:
    print("Invalid Input")