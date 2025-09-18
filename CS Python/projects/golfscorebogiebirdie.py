# Assignment: Golf-Scores Program
# Purpose: to generate a score card and report how many birdies and bogies
# Author: Cole Becker
# Date: 01/10/2023

# Functions
def totalBogies(parList = [], scores = []): # returns the total amount of bogies
    bogietotal = 0
    index = 0
    size = len(parList)
    while index < size:
        if (parList[index] + 1 == scores[index]): 
            bogietotal += 1
        index += 1
    return bogietotal

def totalBirdies(parList = [], scores = []): # returns the total amount of birdies
    birdietotal = 0
    index = 0
    size = len(parList)
    while index < size:
        if (parList[index] - 1 == scores[index]): 
            birdietotal += 1
        index += 1
    return birdietotal

# ... Main Program ...
# Input Requirements - Reading Textfile
golfScores = open("golfScores.txt", 'r')
buffer = golfScores.readline()
par = []
for ch in buffer:
    if ch.isnumeric():
        par.append(int(ch))
print(par)

# Processing Requirements 
buffer = golfScores.readline()
name = buffer[:buffer.index(" ")]
golfer1 = []
for ch in buffer:
    if ch.isnumeric():
        golfer1.append(int(ch))
    if ch == 'H':
        break
print("{} scored {} bogies and {} birdies.".format(name, totalBogies(par, golfer1), totalBirdies(par, golfer1))) # Output the bidies and bogies for golfer 1

buffer = golfScores.readline()
name = buffer[:buffer.index(" ")]
golfer2 = []
for ch in buffer:
    if ch.isnumeric():
        golfer2.append(int(ch))
    if ch == 'H':
        break
print("{} scored {} bogies and {} birdies.".format(name, totalBogies(par, golfer2), totalBirdies(par, golfer2))) # Output the bidies and bogies for golfer 2

buffer = golfScores.readline()
name = buffer[:buffer.index(" ")]
golfer3 = []
for ch in buffer:
    if ch.isnumeric():
        golfer3.append(int(ch))
    if ch == 'H':
        break
print("{} scored {} bogies and {} birdies.".format(name, totalBogies(par, golfer3), totalBirdies(par, golfer3))) # Output the bidies and bogies for golfer 3
    
# ... End of Program ...