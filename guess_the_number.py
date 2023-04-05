import random

def random_number():
    # generates a random number between 1 and 100
    return random.randint(1, 100)

def guess_game():
    # generates a random number and initialize the number of guesses
    secret_number = random_number()
    num_of_guesses = 0


    # loop until the user guesses the correct number or quits the game
    while True:
        # ask the user to input a number or quit the game
        user_input = input("Guess a number between 1 and 100 (or type 'q' to quit): ")

        # if user wants to quit the game
        if user_input.lower() == "q":
            print("You are quitting the game!")
            return

        try:
            guess = int(user_input)
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 100 (or type 'q' to quit).")
            continue

        num_of_guesses += 1

        if guess < secret_number:
            print("Too low! Guess again.")
        elif guess > secret_number:
            print("Too high! Guess again.")
        else:

            print(f"Congratulations! You guessed the secret number ({secret_number}) in {num_of_guesses} guesses.")

            return

guess_game()
