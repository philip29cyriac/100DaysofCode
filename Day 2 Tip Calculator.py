print("Welcome to the tip calculator!")
bill = float(input("What is the total bill: "))
tip = float(input("What is the tip amount: 10%, 12% or 15% "))
people = int(input("How many people to split the bill: "))
total = bill + (bill * tip/100)
per_person = total / people
print("Bill: ", total)
print("Each person should pay: $" + str(per_person))