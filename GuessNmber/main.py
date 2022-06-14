from random import randint
from art import logo


EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Function to check user's guess against actual answer.


def check_answer(guess, answer, turns):
    if guess > answer:
        print("To high.")
        return turns - 1
    elif guess < answer:
        print("To low")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")

# Make function to set difficulty.


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard':")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        if level == "hard":
            return HARD_LEVEL_TURNS


def game():
    print(logo)
    # Choose a random number between 1 and 100.
    print('Welcome to the Number Guessing Game!')
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)

    turns = set_difficulty()
    # Repeat the guessing functionality if they get it wrong.
    guess = 0

    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

        # Let the user guess a number.
        guess = int(input("Make a guess: "))

        # Track the number of turns and reduce by 1 if they get it wrong.
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've tun out of guesses, you lose.")
            print(f"Pssst, the correct answer is {answer}")
            return
        elif guess != answer:
            print("Guess again.")


game()
