"""Plays the guess my number game with the computer guessing."""

from math import log2

low = int(input("Enter the smaller number: "))
high = int(input("Enter the larger number: "))
max_tries = round(log2(high - low) + 1)
tries = 0

while True:
    guess = ((high - low) // 2) + low
    tries += 1
    if tries > max_tries:
        print("You're cheating!")
        break
    print("Your number is", guess)
    how_close = input("Enter =, <, or >: ")
    if how_close == "<":
        high = guess
    elif how_close == ">":
        low = guess
    else:
        print("Hooray, I've got it in", tries, "tries!")
        break
    
