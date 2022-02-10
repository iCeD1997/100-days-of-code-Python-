# Blind auction bid without using dictionary
from art import logo    
import os               

host_again = True       

while host_again:
    more_bidders = True

    print(logo)
    highest_bid = 0
    highest_bidder = ("")

    while more_bidders:
        name = input("What is your name?: ").title()
        bid = int(input("What is your bid? : Rs."))
        if bid > highest_bid:
            highest_bid = bid
            highest_bidder = name
        again = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
        os.system('cls')
        if again == 'no':
            break

    print(f"The winner is {highest_bidder} with a bid of Rs.{highest_bid}")

    restart = input("\n\nDo you want to host another auction? Type'y' or 'n': ").lower()
    if restart == 'n':
        host_again = False