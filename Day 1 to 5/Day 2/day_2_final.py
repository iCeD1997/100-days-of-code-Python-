#Tip Calculator
import os

print("Welcome to the tip calculator!")
amount = float(input("What was the total bill? Rs."))
tip = int(input("What percentage time would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

if tip == 10:
    calculated = ((amount* 1.10)/people).__round__(2)
elif tip == 12:
    calculated = ((amount* 1.12)/people).__round__(2)
elif tip == 15:
    calculated = ((amount* 1.5)/people).__round__(2)



print(f"Each person should pay Rs.{calculated} each")

