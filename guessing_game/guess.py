#python guessing game

import random

guessTaken = 0

print('What is your name?')
myName = input()


number = random.randint(1,20)

print(myName + ' I am thinking of a number between 1 and 20')

for guessTaken in range(6):
    print('What is your guess?')
    guess = input()
    guess = int(guess)

    if guess < number:
        print('Your guess is too low')
    elif guess > number:
        print('Your guess is too high')
    else:
        break

if guess == number:
    guessTaken = str(guessTaken+1)
    print('Good job '+myName+'! You guessed the number in '+guessTaken+ ' tries.')

if guess != number:
    number = str(number)
    print('The correct answer was '+number)