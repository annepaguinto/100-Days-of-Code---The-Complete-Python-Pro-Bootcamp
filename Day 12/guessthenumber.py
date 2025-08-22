import random
import art

number = random.randint(1, 100)
attempt = 0
guess = 0

print(art.logo)
choice = input("Welcome to the number guessing game! \nI'm thinking of a number between 1 and 100. \nChoose a difficulty. Type 'easy' or 'hard': ").lower()

if choice == 'easy':
    attempt = 10
elif choice == 'hard':
    attempt = 5
else:
    print("Invalid Input.")

while guess != number:
    print(f"You have {attempt} attempts to guess the number")
    guess = int(input("Make a guess:"))
    attempt -= 1

    if guess == number:
        print(f"You got it. The answer was {number}.")
    elif attempt < 1:
        print(f"Number is {number}. You've run out of guesses. Refresh the page to run again.")
        guess = number
    elif guess < number:
        print("Too low.\nGuess again.")
    else:
        print("Too high. \nGuess again.")
