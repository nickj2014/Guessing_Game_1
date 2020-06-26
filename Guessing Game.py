import random

rand_num = random.randint(1, 10)  # Generate random number between 1-9
counter = 0  # Initialise counter
run = True
print("""I'm thinking of a number between 1-9, take a guess!
Type 'exit' to exit the program.""")

while run:
    guess = input("Please enter a number between 1 and 9: ")  # Get user guess

    if guess.lower() == "exit":  # Check for exit input
        run = False
        print("Bye!")

    elif int(guess) > 9 or int(guess) < 0:  # Error check the number input
        print("Invalid option, please enter again.")

    elif int(guess) == rand_num:  # If guess matches, print attempts, reset number and counter
        counter += 1
        print("Correct! It took you", counter, "attempts.")
        rand_num = random.randint(1, 9)
        counter = 0

    elif int(guess) > rand_num:  # If guess is higher, increment counter
        print("You guessed too high!")
        counter += 1

    elif int(guess) < rand_num:  # If guess is lower, increment counter
        print("You guessed too low!")
        counter += 1
