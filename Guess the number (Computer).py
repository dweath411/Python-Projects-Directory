# A guessing game where the computer has the secret number

import random

# define a function to generate a random number

def guess(x): # x is a parameter we can pass into a random get number function
    random_number = random.randint(1, x) # this returns a random number between 1 and x, part of the random package
    # the computer will keep having us guess between 1 and the number it guesses (x), and it will tell us whether we're too high or too low.
    # this is a job for loops, to help us save time on guessing!
    guess = 0 # we choose guess = 0, because we want the guess to accidentally be the secret number. So 0 can never be the case, since the random number is between 1 and x.
    while guess != random_number: # guess does NOT equal the random number, then we want to iterate over something
        guess = int(input(f'Guess a number between 1 and {x}: '))
        # now, we're going to add IF statements, so that the computer can guide us in the right direction when we guess
        if guess < random_number:
            print('Sorry, guess again. Too low. ')
        elif guess > random_number:
            print('Sorry, guess again. Too high')
        # if the computer doesn't say too high or too low, that means you've hit the random number!
        print(guess)
    print(f'Congratulations. You have guessed the number {random_number} correctly!')
guess(10)
