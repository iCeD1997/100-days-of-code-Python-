#Password Generator Project

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P


import random
import os

again = True

while again:
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Welcome to the PyPassword Generator!")
    nr_letters= int(input("How many letters would you like in your password?\n")) 
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))

    new_password = []
    for x in range(nr_letters):
        let = random.choice(letters)
        new_password.append(let)
    for x in range(nr_symbols):
        sym = random.choice(symbols)
        new_password.append(sym)
    for x in range(nr_numbers):
        num = random.choice(numbers)
        new_password.append(num)

    hard_new_password = new_password
    random.shuffle(hard_new_password)
    
    level = input("Do you want an 'easy' password or a 'hard' password: ")
    
    final = ("")

    if level == 'easy':
        for x in new_password:
            final += x
        print(f"Your easy password could be {final}")
    elif level == 'hard':
        for x in hard_new_password:
            final += x
        print(f"Your hard password could be {final}")
    
    restart = input("Do you want to try again? Type 'y' or 'n': ")
    if restart == 'n':
        again = False
    os.system("cls")

