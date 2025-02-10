print("Welcome to Treasure Hunt. Your goal is to find the treasure!")

treasure_response = input("You're at a cross road. Where do you want to go? type left or right")

if treasure_response == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    lake_response = input("Type wait to wait for a boat. Type swim to swim across")
    if lake_response == "wait":
        print("You arrive at the island unharmed.")
        door_response = input("There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?")
        if door_response == "red":
            print("Burned by fire. Game Over.")
        elif door_response == "blue":
            print("Eaten by beasts. Game Over.")
        elif door_response == "yellow":
            print("You Win!")
        else:
            print("Game Over. :(")
    else:
        print("Attacked by trout. Game Over.")

else:
    print("Fall into a hole. Game Over.")