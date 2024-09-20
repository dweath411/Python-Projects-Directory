# A guessing game where you have the secret number, and the computer has to guess

import random

def computer_guess(x): # x is a parameter we can pass into a random get number function
    # since we're not telling the computer our secret number, so the computer has a minimum and maximum of values it can search through.
    # we set the lower and upper bounds
    lower = 1
    upper = x
    # initialize a feedback variable for the computer
    feedback = ''
    # one issue, random.randit will throw and error if the lower and upper values are the same number.
    # how can we circumvent this? 
    while feedback != 'c':
        if  lower != upper:
            guess = random.randint(lower, upper)
        else:
            guess = lower # could also be upper, because lower = higher.
            # so computer guessed our number before it we could get a chance to prompt it with feedback
        # c is just chosen because it is c for correct
        guess = random.randint(lower, upper)
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)? ').lower() # lowers the string in the input
        # so the user input is going to be H, L, or C. don't cheat!
        if feedback == 'h': # if the number is too high
            upper = guess - 1 # we choose guess - 1, so that we know it's between 1 and 7 if we guess 8, since 8 is too high
        elif feedback == 'l':
            lower = guess + 1 # same reasoning as above, we know that if the guess is too low then it's at least one higher than the initial guess
    
    print(f'Congratulations. The computer guessed your number, {guess}, correctly!')

computer_guess(10) # choose a number higher than 10 for the next time!

# Let's say the secret number is 7. Be honest with the computer!
