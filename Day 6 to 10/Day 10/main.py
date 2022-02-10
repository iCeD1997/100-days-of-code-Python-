# Calculator Project

from art import logo
import os

# Add
def add(n1, n2):
    return (n1+n2)

# Subtract
def subtract(n1, n2):
    return (n1-n2)

# Multiply
def multiply(n1, n2):
    return (n1*n2)

# Divide
def divide(n1, n2):
    return (n1/n2)

# Creating dictionary of operations
operations = {          
"+": add, 
"-": subtract, 
"*": multiply,
"/": divide
}  

def calculator():
    
    print(logo)

    # Asking the user to enter the 1st number
    num1 = float(input("What's the first number? : "))

    for key in operations:
        print(key)

    again = True

    while again:

        # Asking the user to enter the required operation
        operation_symbol = input("Pick an operation to perform on the two numbers: ")

        # Asking the user to enter the 2nd number
        num2 = float(input("What's the second number? : "))

        operation_required = operations[operation_symbol]
        answer = operation_required(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        restart = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ")
        if restart == 'y':
            num1 = answer
        else:
            again = False
            os.system("cls")
            calculator()
            

calculator()
