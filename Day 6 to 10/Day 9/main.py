# Blind auction bid using dictionary
from art import logo                 # importing logo
import os                            # importing os for clearing screen


def finding_winner(biding_list):
    winning_bid = 0                  # initialising winning_bid variable with 0 value
    winning_name = ("")              # initialising winning_name variable with empty string
    for key in bids:                 # using for loop to loop through bids and find the highest bid
        if bids[key] > winning_bid:
            winning_bid = bids[key]
            winning_name = key
    print(f"The winner is {winning_name} with a bid of Rs.{winning_bid}")

again = True

while again:
    print(logo)

    bids = {}


    while True:
        name = input("What is your name?: ").title()
        price = int(input("What is your bid? : Rs."))
        bids[name] = price
        more_bids = input("Are there any other bidders? Type 'y' or 'n'.\n").lower()
        if more_bids == 'y':
            os.system('cls')
        if more_bids == 'n':
            os.system('cls')
            break

    finding_winner(bids)

    restart = input("\n\nDo you want to host another auction? Type'y' or 'n': ").lower()
    if restart == 'n':
        again = False
    else:
        os.system('cls')
