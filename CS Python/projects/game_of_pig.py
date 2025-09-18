# End of UNIT 2: Programming Project - GAME OF PIG
#
# Purpose: to create a two player text based game.
# 1. Complete the code -alone- using the template below.
# 2. Do not 're-write' the project, make use of it.
# 3. Rules of the Game:
# 4. Human vs. Computer - Human player against the computer
# 5. Game ends when one player reaches 100 banked points
# 6. During a turn, a player accumulates a score
#    A turn ends when (a) a player banks the score adding
#    the current score to their banked score or (b) when
#    the player rolls a one (1) on the die - loosing all
#    points accumulated that round (the banked score is safe)
# 7. Note: A turn is a series of dice rolls
# 8. At the end of the game, ask to play again.
# 9. Follow the Major Programming Rubric - Keep a Journal!
# 0. REMOVE TEMPLATE INSTRUCTIONS - REPLACE WITH YOUR COMMENTS
#
# Author: Cole Becker
#
# Date: September 22 2023
#
# Import random and Variables 

import random

# Change numbers to dice symbols
dice = { 1 : "⚀",
         2 : "⚁",
         3 : "⚂",
         4 : "⚃",
         5 : "⚄",
         6 : "⚅"
         }

die = random.randint(1,6)  # randomly generate number between 1-6
play = True                # While loop for play - Assume True
answer = "NA"              # user input stored to play game
humanBank = 0              # game memory variables
humanScore = 0
computerBank = 0
computerScore = 0

# Welcome Screen and instructions for player
print("""\
   ___                       __   ___ _      
  / __|__ _ _ __  ___   ___ / _| | _ (_)__ _ 
 | (_ / _` | '  \/ -_) / _ \  _| |  _/ / _` |
  \___\__,_|_|_|_\___| \___/_|   |_| |_\__, |
                                       |___/ 
Welcome to the Dice Game!
Instructions:
- You and the computer take turns rolling a die.
- You can choose to r(oll) or h(old).
- If you roll a 1, your turn ends, and you lose your accumulated points.
- The first player to reach 100 points wins.
""")

# Ask user if they want to play
data = input("Would you like to play? (y/Y) for 'yes' or (n/N) for 'no': ")
if data.lower() == "y":
    play = True
elif data.lower() == "n":
    play = False
else:
    print("error: invalid response.")

# GAME LOOP
while play: 
    while play == True:
        # HUMAN PLAYER 
        humanScore = 0     # initial value at the start of each turn
        die = 0            # impossible die value to enter player turn loop
        # Human Turn loop
        while True: 
            answer = input("(r)oll or (h)old? ")
                
            if answer.lower() == 'r':
                die = random.randint(1,6)
                print("you rolled {0}".format(dice.get(die)))
                
                if die == 1:
                    print("you rolled a 1. Turn over.")
                    humanScore = 0
                    break
                else:
                    humanScore += die
                    print(f"current score is {humanScore}")
                
            if answer.lower() == 'h':
                break
                
                
        # Update humanbank so it adds the humanscore after the turn
        humanBank += humanScore
            
        # Shows the user the round and bank score 
        print(f"User Round Score: {humanScore}, User bank: {humanBank}")
            
        # Check if human score is 100
        if humanBank >= 100:
            break
            
        # Computer Turn
        computerScore = 0 #initial value at the start of every turn
        die = 0 # impossible die value to enter player turn loop
        while True:
            die = random.randint(1,6)
            print("computer rolled {0}".format(dice.get(die)))
                
            if die == 1:
                print(f"computer rolled a 1. Turn over.")
                computerScore = 0
                break
                
            else:
                computerScore += die
                print(f"computer score is {computerScore}")
                
            if computerBank < humanBank and computerScore > 15: #making the computer chase the user if behind
                break
                
            if computerBank > 80 and computerScore > 10: #play risky if close to 100
                break
                
            if computerBank >= humanBank and computerScore > 6: #play conservative if tied or winning
                break

        #update computerBank after the turn
        computerBank += computerScore
            
        # Show computer score and bank
        print(f"Computer Round Score: {computerScore}, Computer Bank: {computerBank}")
            
        # Check to see if computer has won
        if computerBank >= 100:
            break
                
                    
        # GAME OVER - Report who won based on bank score
    if computerBank >= 100:
        print("computer wins!")
    if humanBank >= 100:
        print("you win!")
        
    print("""\
                ___                   ___              
                / __|__ _ _ __  ___   / _ \__ _____ _ _ 
            | (_ / _` | '  \/ -_) | (_) \ V / -_) '_|
                \___\__,_|_|_|_\___|  \___/ \_/\___|_|  """)
        
    # Ask the user if they want to Play Again

    play_again = input("would you like to play again? Y/y or N/n: ")

    if play_again.lower() == "y":
        computerBank = 0
        computerScore = 0 
        humanBank = 0
        humanScore = 0
        continue
        
    elif play_again.lower() == "n":
        break
    
# END PROGRAM - Print thanks for playing
print("Thank's for playing!")