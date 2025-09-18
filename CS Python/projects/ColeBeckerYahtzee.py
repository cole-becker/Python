# End of Unit 4: Yahtzee Project
#
# Purpose: to create a two player text based game.
#
# Author: Cole Becker
#
# Date: October 12 2023
#
# Setup the initial environment 

import random
from colorama import Fore

# dice symbols
dice = { 1 : "⚀",
         2 : "⚁",
         3 : "⚂",
         4 : "⚃",
         5 : "⚄",
         6 : "⚅"
         }
# the dice cup which hold the dice (a list of dice) - starting with impossible values
# the parallel array boolean flags required to hold specific dice 
cup = [0,0,0,0,0]
held = [False,False,False,False,False]

# include any other global variables you need here
current_player = '1'
rounds = 26
rolls = 0

# Define score categories
score_categories = [
    "Ones", "Twos", "Threes", "Fours", "Fives", "Sixes",
    "Three of a Kind", "Four of a Kind", "Full House",
    "Small Straight", "Large Straight", "Yahtzee", "Chance"
]

# Initialize player score sheets
player_scores = {
    '1': {category: None for category in score_categories},
    '2': {category: None for category in score_categories},
}

# rolling the dice 
def rollDice():
    for index in range(5):
        if held[index] == False: # we can roll the die at that location
            cup[index] = random.randint(1,6)


# displaying the dice where a die held is indicated by a >, example: 1>⚀
# a held die is not rolled but kept back to help a player create a particular pattern of five dice.
def displayDice():
    for index in range (5):
        if held[index] == False:
            print('{0}:{1} '.format(index+1, dice.get(cup[index])), end="")
        else:
            print('{0}>{1} '.format(index+1, dice.get(cup[index])), end="")
    print()
 

# methods to hold or release the die at a particular location - used for players holding dice back
# during their turn while trying to produce a particular pattern of dice. 
def holdDie(index):
    flag = False
    if (index > 0 and index < 6):
        index = index - 1 # update for correct list interaction
        held[index] = True
        flag = True
    return flag  # let the calling method know if successfully held

def releaseDie(index):
    flag = False
    if index > 0 and index < 6:
        index = index - 1 # update for correct list interaction
        held[index] = False
        flag = True
    return flag  # let the calling method know if successfully released

# sum of all dice for chance location
def chanceScore():
    chance = 0
    for index in range(5):
        chance += cup[index]
    return chance
    
# Write your other methods here to play the game and display the score sheet
# Function to display the score card
def display_score_card(player):
    print(f"Player {player}'s Score Card:")
    for category in score_categories:
        score = player_scores[player][category]
        print(f"{category}: {score}")
    print("\n")

# Fuction to calculate score for players
def calculate_totalscore(player_scores):
    total_score = 0
    for category in player_scores:
        score = player_scores[category]
        if score is not None:
            total_score += score
    return total_score

# Methods needed: check-methods (yahtzee,full-house,small-straight,large-straght, etc)
def calculate_ones(cup): # calculate ones
    return sum([1 for die in cup if die == 1])

def calculate_twos(dice): # calculate twos
    return sum([2 for die in cup if die == 2])

def calculate_threes(dice): # calculate threes
    return sum([3 for die in cup if die == 3])

def calculate_fours(dice): # calculate fours
    return sum([4 for die in cup if die == 4])

def calculate_fives(dice): # calculate fives
    return sum([5 for die in cup if die == 5])

def calculate_sixes(dice): # calculate sixes
    return sum([6 for die in cup if die == 6])

def calculate_threeofakind(dice):
    dice.sort()
    for i in range(3):
        if dice[i] == dice[i+2]:
            return sum(dice)
    return 0 # if no 3 of kind return 0

def calculate_fourofakind(dice):
    dice.sort()
    for i in range(len(dice) - 3):
        if dice[i] == dice[i+3]:
            return sum(dice)
    return 0 # if no 4 of kind return 0

# Function to calculate a full house score
def calculate_fullhouse(cup):
    counts = [cup.count(i) for i in range(1, 7)]
    if 2 in counts and 3 in counts:
        return 25
    return 0

# Function to calculate a small straight score
def calculate_smallstraight(cup):
    sorted_cup = sorted(cup)
    if sorted_cup in [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]:
        return 30
    return 0

# Function to calculate a large straight score
def calculate_largestraight(cup):
    sorted_cup = sorted(cup)
    if sorted_cup in [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6]]:
        return 40
    return 0

# Function to calculate a Yahtzee score
def calculate_yahtzee(cup):
    if cup.count(cup[0]) == 5:
        return 50
    return 0

print(Fore.CYAN + """\
 __   __    _   _              
 \ \ / /_ _| |_| |_ ______ ___ 
  \ V / _` | ' \  _|_ / -_) -_)
   |_|\__,_|_||_\__/__\___\___|
    Command Line Instructions
-choose 1-5 to hold that rolled die                                
-choose 0 to reroll all non held die
-choose 6 to keep all rolled die
""" + Fore.RESET)

while rounds > 0:
    print(f"Current Player:" + Fore.RED + f" Player {current_player}" + Fore.RESET)

    # roll the dice
    rolls = 3
    rollDice()
    displayDice()
    # shows chance score potential    
    print(Fore.GREEN + f"Player '{current_player}' has a chance score of {chanceScore()}" + Fore.RESET)

    while True and rolls > 0:
        try:
            print(Fore.BLUE + f"\nrolls left: {rolls}" + Fore.RESET)
            data = int(input("enter your choice (enter 7 for help): "))
            if data == 0: # reroll non held die
                rollDice()
                rolls -= 1
                displayDice()
                # shows chance score potential    
                print(Fore.GREEN + f"Player '{current_player}' has a chance score of {chanceScore()}" + Fore.RESET)
            elif data ==6 : # keep die
                break
            elif data == 7:
                print(Fore.YELLOW + "\nCommands...\n0 to reroll all non held die\n1-5 to hold the die in that slot\n6 to keep all die" + Fore.RESET)
                print(f"\nCurrent Player:" + Fore.RED + f" Player {current_player}" + Fore.RESET), displayDice()
            elif 1 <= data <= 5:
                if held[data - 1]:
                    releaseDie(data)
                    displayDice()
                else:
                    holdDie(data)
                    displayDice()
            else:
                print("Invalid input. Please choose a die between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # shows chance score potential    
    print(Fore.GREEN + f"Player '{current_player}' has a chance score of {chanceScore()}" + Fore.RESET)

    # display score sheet
    display_score_card(current_player)

    while True:
        # choose category
        category_choice = input("Choose a category: ").capitalize()
        if player_scores[current_player].get(category_choice) is None:
            if category_choice.lower() == "ones":
                player_scores[current_player]["Ones"] = calculate_ones(cup)
                break
            
            elif category_choice.lower() == "twos":
                player_scores[current_player]["Twos"] = calculate_twos(cup)
                break
            
            elif category_choice.lower() == "threes":
                player_scores[current_player]["Threes"] = calculate_threes(cup)
                break
            
            elif category_choice.lower() == "fours":
                player_scores[current_player]["Fours"] = calculate_fours(cup)
                break
            
            elif category_choice.lower() == "fives":
                player_scores[current_player]["Fives"] = calculate_fives(cup)
                break
            
            elif category_choice.lower() == "sixes":
                player_scores[current_player]["Sixes"] = calculate_sixes(cup)
                break

            elif category_choice.lower() == "three of a kind":
                player_scores[current_player]["Three of a Kind"] = calculate_threeofakind(cup)
                break

            elif category_choice.lower() == "four of a kind":
                player_scores[current_player]["Four of a Kind"] = calculate_fourofakind(cup)
                break

            elif category_choice.lower() == "full house":
                player_scores[current_player]["Full House"] = calculate_fullhouse(cup)
                break

            elif category_choice.lower() == "small straight":
                player_scores[current_player]["Small Straight"] = calculate_smallstraight(cup)
                break

            elif category_choice.lower() == "large straight":
                player_scores[current_player]["Large Straight"] = calculate_largestraight(cup)
                break

            elif category_choice.lower() == "yahtzee":
                player_scores[current_player]["Yahtzee"] = calculate_yahtzee(cup)
                break

            elif category_choice.lower() == "chance":
                player_scores[current_player]["Chance"] = chanceScore()
                break

            else:
                print("Not a valid category, please try again.")
        
        else:
            print("Invalid category choice or category already scored. Please choose a valid and unscored category.")

    # Display the updated score card
    display_score_card(current_player)

    # switch to the next player
    current_player = '2' if current_player == '1' else '1'
    rounds -= 1

# print final scores
print("\nFinal Scores:\n" + Fore.CYAN)
display_score_card('1')
display_score_card('2')

# calculate totals and determin winner
total_playerscore1 = calculate_totalscore(player_scores['1'])
total_playerscore2 = calculate_totalscore(player_scores['2'])
if total_playerscore1 > total_playerscore2:
    print(Fore.GREEN + "Player 1 wins!" + Fore.RESET)
elif total_playerscore1 < total_playerscore2:
    print(Fore.GREEN + "Player 2 wins!" + Fore.RESET)
else:
    print(Fore.YELLOW + "Tie!" + Fore.RESET)