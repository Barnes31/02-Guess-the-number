#!/Library/Frameworks/Python.framework/Versions/3.6/bin

import sys
import random
assert sys.version_info >= (3,4), "This script requires at least Python 3.4"

maxGuess = 4
player = input('Please type your name: ')

    
number = random.randint(1,10)
print('Hello ' + player + '!' + ' Welcome to Guess That Number!')

print('Im thinking of a number between 1 an 10. Can you guess what it is?')
      
print('But! You will have to guess carfully! You will only have' + " " + (str(maxGuess)) + " " + 'guesses!')
      
print('Lets begin!')




for GuessCount in range(maxGuess):
        try:
                guess = input('Whats your guess, ' + player + "? ")
                guess = int(guess)
                if guess < number and (maxGuess - (GuessCount + 1)) > 0:
                        print('Oops too low!' + ' You have ' + (str(maxGuess - (GuessCount + 1))) + ' guesses left! Try again!')
                elif guess > number and (maxGuess - (GuessCount + 1)) == 0:
                        print('Oops too high!' + ' You have ' + (str(maxGuess - (GuessCount + 1))) + ' guesses left!')
                elif guess > number and (maxGuess - (GuessCount + 1)) > 0:
                        print('Oops too high!' + ' You have ' + (str(maxGuess - (GuessCount + 1))) + ' guesses left! Try again!')
                elif guess < number and (maxGuess - (GuessCount + 1)) == 0:
                        print('Oops too high!' + ' You have ' + (str(maxGuess - (GuessCount + 1))) + ' guesses left!')
                elif guess == number:
                        print('Way to go! Thats the one!')
                        break


        except ValueError:
                print('Please enter a whole number.')

if guess != number:
      number = str(number)
      print('Uh oh seems like you ran out of lives! The number I was thinking of was ' + number + '.' + ' Better luck next time!')

if guess == number:
        print('Congratulations, ' + player + '!' + ' You have won...bragging rights!')

