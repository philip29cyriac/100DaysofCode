print("Welcome to python pizza deliveries")
size = input("What size pizza do you want? S, M, or L:")
pepperoni = input("Do you want pepperoni on your pizza? Y or  N:")
extra_cheese = input("Do you want extra cheese? Y or N:")

pizza  = 0

# Working out the price of pizzas by assigning values
if size == "S":
    pizza = 15
elif size == "M":
    pizza = 20
elif size == "L":
    var = pizza == 25
else:
    print("Invalid Input")

# working out additional values

if pepperoni == "Y":
        pizza += 3
elif pepperoni == "N":
        pizza += 0
else:
        print("Invalid Input")


if extra_cheese == "Y":
        pizza += 1
elif extra_cheese == "N":
        pizza += 0
print(f"Your final bill is: ${pizza}")
