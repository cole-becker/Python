import random
from colorama import Fore

RPS = ['Rock', 'Paper', 'Scissors']

def userChoice():
    while True:
        user_choice = input("Rock, Paper, or Scissors?: ").capitalize()
        if user_choice in RPS:
            return user_choice
        else:
            print("error: invalid response. Try again.")

def computerChoice():
    computer_choice = random.choice(RPS)
    return computer_choice

print(Fore.CYAN + "Welcome to Rock, Paper, Scissors!\n-Rock beats Scissors\n-Scissors beats Paper\n-Paper beats Rock" + Fore.RESET)
while True:
    user_choice = userChoice()
    computer_choice = computerChoice()
    print(f"You chose {user_choice} and computer chose {computer_choice}")
    if user_choice == computer_choice:
        print(Fore.YELLOW + "You Tied, Please Choose Again" + Fore.RESET)
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or (user_choice == 'Scissors' and computer_choice == 'Paper') or (user_choice == 'Paper' and computer_choice == 'Rock'):
        print(Fore.GREEN + "You Win!" + Fore.RESET)
    else:
        print(Fore.RED + "You Lose." + Fore.RESET)