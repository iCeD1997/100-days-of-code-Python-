#Hangman game
from art import stages,logo
import random
from words import word_list

chosen = random.choice(word_list)
chosen_word = list(chosen)

lives = 6

display = []
for x in chosen_word:
    display += "_"


print(logo)
print(display)

guessed_letters = []

while lives != 0:
    if chosen_word == display:
        print(f"You got it! The correct word was {chosen_word}")
        break
    print(f"You have {lives} lives remaining")
    guess = input("Guess a letter: ")
    if guess in guessed_letters:
        print(f"You have already guessed {guess}")
    elif guess in chosen_word:
        for x in range(len(chosen_word)):
            if guess == chosen_word[x]:
                display[x] = guess
        guessed_letters.append(guess)
        print(stages[lives])
        print(display)
                
    elif guess not in chosen_word:
        lives -= 1
        print(f"The letter {guess} is not in the word!")
        guessed_letters.append(guess)
        print(stages[lives])
        print(display)

if lives == 0:
    print(f"You ran out of lives. You lost!\nThe correct word was {chosen}")