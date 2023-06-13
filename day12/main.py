# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from art import logo

print(logo)

print(
    "Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100.")

num = random.randint(1, 101)

diff = input("Choose a difficulty. Type 'easy' or 'hard': ")


def guess_and_compare(attempts):
    print(f"You have {attempts} attempts remaining to guess the number.")
    while attempts > 0:
        guess = int(input("Make a guess: "))
        if guess == num:
            print(f"You got it! The answer was {num}.")
            attempts = -1
        elif guess < num and attempts > 1:
            attempts -= 1
            print("Too Low \nGuess again.")
            print(
                f"You have {attempts} attempts remaining to guess the number.")
        elif guess < num:
            attempts -= 1
            print("Too Low.")
        elif guess > num and attempts > 1:
            attempts -= 1
            print("Too High \nGuess again.")
            print(
                f"You have {attempts} attempts remaining to guess the number.")
        else:
            attempts -= 1
            print("Too High.")
    if attempts != -1:
        print("You've run out of guesses, you lose.")


if diff == 'easy':
    attempts = 10
    guess_and_compare(attempts)
elif diff == 'hard':
    attempts = 5
    guess_and_compare(attempts)
