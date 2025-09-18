# Title: BlackJack - game of 21 against the computer
# Purpose: To get closest to 21
# Author: Cole Becker
# Date: September 28 2023

# Import Modules
from colorama import Fore, Back, Style
import random

# Functions
def dealCard(turn): # picks a random card from deck
    card = random.choice(deck)
    turn.append(card)
    deck.remove(card)

def revealHand(): # hides one of the dealers cards
    if len(dealerCards) == 2:
        return dealerCards[0]
    elif len(dealerCards) > 2:
        return dealerCards[0] + ' ' + dealerCards[1]

def total(turn): # calculate the total of the hands
    total = 0
    num_aces = 0  # Count of Aces in the hand
    for card in turn:
        card_value = card[1]  # Extract the face value of the card
        if card_value.isdigit():
            total += int(card_value)
        elif card_value in ['J', 'K', 'Q', 'T']:
            total += 10
        elif card_value == 'A':
            num_aces += 1
            total += 11  # Assume Ace is worth 11 initially
    # Check if we need to adjust the value of Aces
    while num_aces > 0 and total > 21:
        total -= 10  # Change the value of one Ace from 11 to 1
        num_aces -= 1
    return total

def printList(n):
    for item in n:
        print(item, end=" ")
        
def newGame():
    while True:
        play_again = input("New game? [Y/y] or [N/n]: ")
        if play_again.lower() == 'y':
            return True  # Player wants to play again
        elif play_again.lower() == 'n':
            return False  # Player wants to quit
        else:
            print("Error: Invalid response. Please enter 'Y' to play again or 'N' to quit.")

# Variables
suits = (Fore.BLACK+'\u2660'+Fore.BLACK, # Spades
         Fore.BLACK+'\u2663'+Fore.BLACK, # Clubs
         Fore.RED+'\u2665'+Fore.BLACK,   # Hearts
         Fore.RED+'\u2666'+Fore.BLACK)   # Diamonds
faces = ('A','K','Q','J','T','9','8','7','6','5','4','3','2') # values
deck = [] # The deck the game will play from
playerCards = [] # users cards score if above 21 lose
dealerCards = [] # computers cards score if above 21 win
play = True # whether or not to start the game loop - Assume True
playerPlay = True # player not stand or bust
dealerPlay = True # dealer not stand or bust

for face in faces: # Creates all the values for each suit in the deck
    for suit in suits:
        deck.append("["+face+suit+"]")

print(Fore.GREEN)
# Welcome screen and Intructions for player
print('''
█▀▀▄ █░░ █▀▀█ █▀▀ █░█ ░░▀ █▀▀█ █▀▀ █░█ 
█▀▀▄ █░░ █▄▄█ █░░ █▀▄ ░░█ █▄▄█ █░░ █▀▄
▀▀▀░ ▀▀▀ ▀░░▀ ▀▀▀ ▀░▀ █▄█ ▀░░▀ ▀▀▀ ▀░▀    
-Get as close to 21 as you can to win
-Dealer must stand on 17 or up
-Player can choose to hit or stand (h or s)
-Aces can be worth 1 point or 11 points
-Face cards are all worth 10 points
''')
print(Fore.RESET)

# Ask player if they want to play
while True:
    start_game = input("Would you like to start a new game? [Y/y] or [N/n]: ")
    if start_game.lower() == 'y':
        break  # Exit the loop and start the game
    elif start_game.lower() == 'n':
        print("Maybe next time! Goodbye.")
        exit()  # Exit the program if the user doesn't want to play
    else:
        print("Error: Invalid response. Please enter 'Y' to play or 'N' to quit.")

while True:
    # main game loop
    for i in range(2): # Deal two cards to the player and dealer
        dealCard(playerCards)
        dealCard(dealerCards)

    while playerPlay:
        print(f"\n{revealHand()} [??] : Dealer")
        printList(playerCards)
        print(f": You for {total(playerCards)}")
            
        if playerPlay and total(playerCards) <= 21:
            if total(playerCards) == 21 and len(playerCards) == 2: # Player blackjack
                break
            data = input("\n(s)tand or (h)it: ")
            if data.lower() == 's': # If stand playerplay false
                playerPlay = False
            elif data.lower() == 'h':
                dealCard(playerCards)
            else:
                print("Error: Invalid input.")
        elif total(playerCards) > 21: # Player bust
            break
        elif total(dealerCards) > 21: # Dealer bust
            break

    while dealerPlay and not playerPlay:
        if total(dealerCards) >= 17: # Dealer stands on 17 or up
            dealerPlay = False
        else:
            dealCard(dealerCards)
        if total(dealerCards) == 21 and len(dealerCards) == 2: # Dealer blackjack
            break
        elif total(playerCards) > 21: # Player bust
            break
        elif total(dealerCards) > 21: # Dealer bust
            break

    # Check for winner!
    if total(dealerCards) == total(playerCards): # Player and dealer tie
        printList(dealerCards)
        print(f": Dealer for {total(dealerCards)}")
        printList(playerCards)
        print(f": You for {total(playerCards)}")
        print(Fore.YELLOW)
        print("Push! You tied.")
        print(Fore.RESET)
    elif total(dealerCards) == 21 and len(dealerCards) == 2: # Dealer got 21
        printList(dealerCards)
        print(f": Dealer for {total(dealerCards)}")
        printList(playerCards)
        print(f": You for {total(playerCards)}")
        print(Fore.RED)
        print("BlackJack! Dealer got 21, you lose.")
        print(Fore.RESET)
    elif total(playerCards) == 21 and len(playerCards) == 2: # Player got 21
        printList(dealerCards)
        print(f": Dealer for {total(dealerCards)}")
        printList(playerCards)
        print(f": You for {total(playerCards)}")
        print(Fore.GREEN)
        print("BlackJack! you got 21, you win!")
        print(Fore.RESET)
    elif total(playerCards) > 21: # Player bust
        printList(dealerCards)
        print(f": Dealer for {total(dealerCards)}")
        printList(playerCards)
        print(f": You for {total(playerCards)}")
        print(Fore.RED)
        print("Player Bust! You lose.")
        print(Fore.RESET)
    elif total(dealerCards) > 21: # Dealer bust
        printList(dealerCards)
        print(f": Dealer for {total(dealerCards)}")
        printList(playerCards)
        print(f": You for {total(playerCards)}")
        print(Fore.GREEN)
        print("Dealer Bust! You win!")
        print(Fore.RESET)
    elif total(playerCards) > total(dealerCards): # Player closer to 21
        printList(dealerCards)
        print(f": Dealer for {total(dealerCards)}")
        printList(playerCards)
        print(f": You for {total(playerCards)}")
        print(Fore.GREEN)
        print("You win!")
        print(Fore.RESET)
    elif total(playerCards) < total(dealerCards): # Dealer closer to 21
        printList(dealerCards)
        print(f": Dealer for {total(dealerCards)}")
        printList(playerCards)
        print(f": You for {total(playerCards)}")
        print(Fore.RED)
        print("You lose.")
        print(Fore.RESET)

    if not newGame():
        print('''
              

  _______ _                 _           __                   _             _             _ 
 |__   __| |               | |         / _|                 | |           (_)           | |
    | |  | |__   __ _ _ __ | | _____  | |_ ___  _ __   _ __ | | __ _ _   _ _ _ __   __ _| |
    | |  | '_ \ / _` | '_ \| |/ / __| |  _/ _ \| '__| | '_ \| |/ _` | | | | | '_ \ / _` | |
    | |  | | | | (_| | | | |   <\__ \ | || (_) | |    | |_) | | (_| | |_| | | | | | (_| |_|
    |_|  |_| |_|\__,_|_| |_|_|\_\___/ |_| \___/|_|    | .__/|_|\__,_|\__, |_|_| |_|\__, (_)
                                                      | |             __/ |         __/ |  
                                                      |_|            |___/         |___/   

''')
        exit()
    else:
        playerCards = [] #Reset all variables for play again
        dealerCards = []
        playerPlay = True
        dealerPlay = True

        # Reset deck
        deck = []
        for face in faces:
            for suit in suits:
                deck.append("["+face+suit+"]")