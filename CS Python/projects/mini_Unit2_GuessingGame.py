# UNIT 4: Mini Programming Project - Number Guessing Game
#
# Purpose to program the childhood game hi-low.  The computer picks
# a number between 1-100 and the human player tries to guess the number
# in the fewest number of rounds.  The game should keep track of how
# many attempts the player makes guessing the right number.
# Should the player take ten attempts at guessing the game ends displaying
# the correct answer and asks the user if they want to play again.
#
# Author: Cole Becker
#
# Date: September 18, 2023

# Setup the environment
import random                   # the library 'tool' used to generate pesudo random values
number = random.randint(1,100)  # pick a random value between 1 and 100
data = "NA"                     # the user's data to check valid input of whole numbers
counter = 0                     # keep track of the number of guesses
play = False                    # game flag for main loop and play again feature
guess = -1                      # an impossible starting value, human's guess

# Inform the human player about the program - specific to CLI programs
print("Welcome to the guessing game: Hi-Low.")
print("I'm thinking of a number between 1 and 100")
print("You have ten attempts to guess the right number")
print("Would you like to play the game?")
print()
data = input("yes (y/Y) or no (n/N): ")

# check the player's response and set the play flag to True or False
if data.lower() == "y":
    play = True
elif data.lower() == "n":
    play = False
    print("Thanks for playing! bye.")
else:
    print("Error, please enter 'y/Y' or 'n/N'.")
   
# Write a while loop as the main game loop
while play: # your condition here:

    # Write the guess and check loop using variables guess and number
    while guess != number: # your condition here:
        
        while True: 
            
            counter += 1 # add one to the guess counter
        
            data = input("please enter your guess from 1 to 100: ") # ask the user for a number between 1 and 100
        
            if data.isdigit(): # check that the string holds a number using a while loop
            
        
            # if and only if the user has entered a whole number assign guess
                guess = int(data)
                if guess not in range (1, 101):
                    print("please enter a valid number.")
                    counter = 0
                    continue
        
            if guess > number: # check the guess and report too high or two low
                print("Too high, please try again: ")
            if guess < number:
                print("Too low, please try again: ")
            if guess == number:
                break
        
# check number of guesses .. over ten? end the loop
            if counter >= 10:
                break
    # End of Guess Loop    
        if counter < 10:
            print("Correct! you guessed {0} times.".format(counter))
            counter = 0
            guess = -1
            number = random.randint(1,100)
            break
        elif guess == number:
            print("Max guesses reached, but you guessed right at last")
            counter = 0
            guess = -1
            number = random.randint(1,100)
            break
        else:
            print("Sorry it was {0}. You are out of guesses".format(number))
            counter = 0
            guess = -1
            number = random.randint(1,100)
            break
        
    data = input("Would you like to play again 'yes' (Y/y) or 'no' (N/n): ") # Ask to play again - process the play flag according to user input
    if data.lower() == "y":
        play = True
    elif data.lower() == "n":
        play = False
        print("Thanks for playing! bye.")
# End of game loop
print("Game Over .. ")