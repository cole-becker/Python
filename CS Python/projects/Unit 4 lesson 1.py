import random

def shuffle(list):
    n = len(list)
    for i in range (n - 1, 0, -1):
        j = random.randint(0, i)
        list[i], list[j] = list[j], list[i]

listN = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

print(listN)
print("\n")
shuffle(listN)
print(listN)
print("\n")

suits = ['hearts', 'spades', 'clubs', 'diamonds']
values = ['K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'A']
deck = []

for value in values:
    for suit in suits:
        deck.append(value + ' of ' + suit)

print(deck)
shuffle(deck)
print("\n")
print(deck)