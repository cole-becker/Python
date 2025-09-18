# Assignment: Golf-Scores Program
# Purpose: to generate a score card and report who won
# Author: Cole Becker
# Date: 01/10/2023

# Memory Requirements
from colorama import Fore, Back, Style    # colour coding final score
players = []  # data list of players name, handicap, score and total
winner = [] # player with the least amount of points
def golferData(player):  # pick apart string containing a player's data
    players.append(player)
def calculateTotal(score, handicap):
    total = score - handicap
    return total

# Other Useful Methods Here

# ... Main Program ...
# Input Requirements - Reading Textfile
golfScores = open("golfScores.txt", 'r')
buffer = golfScores.readline()
while True:
    player = golfScores.readline()
    if player == "":
        break

    # Processing Requirements - calculating who won
    playername = player[:player.index(" ")]

    index = -1
    handicap = 0
    pos = 0
    while player[index] != 'H':
        if player[index].isnumeric():
            if pos >= 1:
                handicap = int(player[index]) * 10 + handicap
            else:
                handicap = int(player[index])
            pos += 1
        index -= 1

    index = player.index(" ")
    score = 0
    size = len(player)
    while index < size and player[index] != 'H':
        if player[index].isnumeric():
            score += int(player[index])
        index += 1

    total = calculateTotal(score, handicap)
    player = (playername, score, handicap, total)
    golferData(player)


# Output Requirements - Reporting player's information
    print(f"{playername} scored {score} - {handicap} for a total of {total}") # Prints all scores

if players:
    winner = min(players, key=lambda x: x[3])  # Player with the lowest total score
else:
    winner = None
    
if winner:
    print(Fore.GREEN+ f"The winner is {winner[0]} with a total score of {winner[3]}" + Fore.RESET) # Prints winner in green
else:
    print("Error: No results")

# ... End of Program ...