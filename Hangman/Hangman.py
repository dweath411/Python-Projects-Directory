# Hangman! 

import random
import string # alphabet, predetermined list of uppercase characters in the English dictionary
from hangman_words import words # taking the file `hangman_words` and importing the variable `words` from the file

# print(words) # only print this if you want to see the full list of words

# create a function that will only get words with no dashes/spaces

def valid_word(words): # pass the list of words through the function
    word = random.choice(words) # takes a list and randomly chooses something from that list. like `sample` in R
    while '-' in word or ' ' in word: # if there is a dash or space in the word, it will keep iterating back and forth until it gets a word without dash/space
        word = random.choice(words)
# when it stops iterating, we'll get a valid word
    return word.upper() # uppercase the word when it gets return, so apply upper()

# function for the game hangman
"""
what we need for this function
- to be able to keep track of letters that have been guessed 
- keep track of which letters in the word that have been correctly guessed
- a way to keep track of what is a valid letter
- the condition we need to satisfy for when the user gets all the letters in the word, is when the length of word letters equal to zero
- so while the length of word letters is greater than zero, keep iterating through user input 
- including a concept of lives so the game isn't totally easy
"""
def hangman():
    word = valid_word(words) # get a valid word
    word_letters = set(word) # variable that saves all letters in a word as a set, keeping track of what's already been guessed
    alphabet = set(string.ascii_uppercase) # string containing all uppercase letters in the English dictionary
    used_letters = set() # an empty set, keeping track of what has been guessed by the user
    lives = 6 # 6 tries until the hangman is dead

    # add user input method
    while len(word_letters) > 0 and lives > 0 : # set the conditions for the loop (either they haven't won yet AND they haven't ran out of lives)
        # letters used
        # **EXAMPLE**: ' '.join(['a', 'b', 'cd']) ----> []'a b cd']
        print('You have', lives, 'lives left and you have used these letters: ',' '.join(used_letters))

        # what current word is (ie: W - O R D)
        word_list = [letter if letter in used_letters else '-' for letter in word] # show the words guessed that show up in the word
        print('Current word: ', ' '.join(word_list))
    # user input   
        user_letter = input('Guess a letter:').upper() # for having equality between two strings, uppercase everything since Python is case sensitive
        if user_letter in alphabet - used_letters: # if the input letter is a alphabet that hasn't been used yet, then add to `used_letters` set
            used_letters.add(user_letter) 
            if user_letter in word_letters: # then, if the letter that was guessed is in the word, remove that letter from `word_letters`
                word_letters.remove(user_letter)
                print(f'Good guess! {user_letter} is in the word.')
            else:
                lives = lives - 1 # subtract a life if you guess wrong
                print('Letter is not in the word.')
        elif user_letter in used_letters: # if the user letter that was just entered is in `used_letters`, then that means they've used it before, and it's an invalid guess. print a try again error message
            print('You have used that word already. Try again.')
        else: 
            print('Invalid charfacter. Try again.') # print error message for invalid character
        # arrive here when len(word_letters) == 0 OR when lives == 0, exit while loop
    if lives == 0:
        print('You died, sorry. The word was', word)
    else: 
        print('You guessed the word', word, '!!')

# run game
if __name__ == '__main__': 
    hangman()