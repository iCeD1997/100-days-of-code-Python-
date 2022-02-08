#Rock, Paper, Scissors
import os
import random
from ascii import rock, paper, scissors

again = True

while again:

    user_choice = input("What do you choose? 'Rock', 'Paper' or 'Scissors'? \n").lower()
    comp_choice = "xyz"
    computer_choice = random.randint(1,3)
    if computer_choice == 1:
        comp_choice = "rock"
    elif computer_choice == 2:
        comp_choice = "paper"
    elif computer_choice == 3:
        comp_choice = "scissors"

    print("Your choice:")

    if user_choice == "rock":
        print(rock)
    elif user_choice == "paper":
        print(paper)
    elif user_choice == "scissors":
        print(scissors)


    print("Computers choice:")

    if comp_choice == "rock":
        print(rock)
    elif comp_choice == "paper":
        print(paper)
    elif comp_choice == "scissors":
        print(scissors)

    if user_choice == "rock":
        if comp_choice =="rock":
            print("Its a tie")
        elif comp_choice == "paper":
            print("You lose")
        elif comp_choice == "scissors":
            print("You win")

    elif user_choice == "paper":
        if comp_choice =="rock":
            print("You win")
        elif comp_choice == "paper":
            print("Its a tie")
        elif comp_choice == "scissors":
            print("You lose")

    elif user_choice == "scissors":
        if comp_choice =="rock":
            print("You lose")
        elif comp_choice == "paper":
            print("You win")
        elif comp_choice == "scissors":
            print("Its a tie")

    restart = input("Do you want to try again? Type 'y' or 'n': ").lower()
    if restart == 'n':
        again = False
    os.system("cls")



