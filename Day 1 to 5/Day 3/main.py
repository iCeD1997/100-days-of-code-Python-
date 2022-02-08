#Treasure Island
import os
from picture import module

again = True

while again == True:
    print(module)

    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.") 
    
    x = input("Please choose 'left' or 'right': ").lower()
    if x != 'left':
        print("You fell into a hole. Game over!")
    else:
        y = input("Correct choice! Please choose to 'swim' or 'wait' for the boat to arrive: ").lower()
        if y != 'wait':
            print("You were attacked by trout. Game over!")
        else:
            z = input("Correct choice! Please choose the 'red', 'yellow' or 'blue' door: ").lower()
            if z == 'red':
                print("You were burned by fire. Game over!")
            elif z == 'blue':
                print("You were eaten by beasts. Game over!")
            elif z == 'yellow':
                print("You won 1 million dollars! Game over!")
            else:
                print("You lost game over")
    restart = input("Do you want to restart the game? 'y' or 'n': ")
    if restart == 'n':
        again = False
    os.system("cls")