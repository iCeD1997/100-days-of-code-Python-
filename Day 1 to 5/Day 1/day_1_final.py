import os
x = True
while x:
    print("Welcome to the band name generator!")
    city = input("What's the name of the city you grew up in?: ").title()
    print(city)
    pet = input("What's the name of your first pet?: ").title()
    print(pet)
    print(f"Your pet name could be {city} {pet}")

    restart = input("\n\nDo you want to try again? Type 'y' or 'n' ")
    if restart == 'n':
        x = False
    os.system("cls")