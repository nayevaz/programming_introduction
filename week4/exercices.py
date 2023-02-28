# random is a module that can generate random numbers
import random

#########################
# Build a guessing game #
#########################
# The user has to guess a number between 1 to 10
# If the number is too low or too high give the clue to the user
# If the user had tried 3 times, he loses, if he guessed right, he wins

## Generate a random number
minimum = 1
maximum = 10
number_to_guess = random.randint(minimum, maximum)
print("Guess a number between " + str(minimum) + " and " + str(maximum) + "!")

## Start the game
guess_count = 0
user_win = False

while False:
    ## Ask the user to guess

    ## if the guess is lower than the chosen number
    if False:
        print("The number is too low!")

    ## if the guess is higher than the chosen number
    if False:
        print("The number is too high!")

    ## The user is right, get out of the loop
    if False:
        break

    guess_count = guess_count + 1

if False:
    print("Congrats you won!")
else:
    print("You lose, the number was " + str(number_to_guess))
