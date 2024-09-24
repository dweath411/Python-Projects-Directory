#1 - **Madlibs**

In a traditional Madlib, you have a bunch of blanks in a paragraph. Somebody would fill out those blanks, then read the paragraph out loud with the words that they chose in those blanks.

This project is completed using the concept of string concatenation.
For our madlib, we define 1 adjective, 2 verbs, and 1 noun to complete our string.

#2 - **Guess the number (Computer)**

Here, we create a guessing game you can play, but the computer has the secret number! Our goal is to attempt to guess that number.

The first step is having the computer generate a secret, random number. 

In this script, we're starting to implement looping methods, with `while`, `if`, and `elif`.  

Try to beat the computer in under 3 tries, while it guesses a number between 1 and 10!

#3 - **Guess the number (User)**

Alternatively of the last script, we're going to flip the script onto the computer, and have guess our number. Using functions and while loops, we've gotten the computer to guess our random, and we've also guessed the computers random number!

#4 - **Rock Paper Scissors**

A super simple rock paper scissors game using the `random` package once in a different way than the previous games (#2 and #3).

This time, we're giving the computer a choice of 3 random inputs, (R,P,S) and building a function to determine the next steps after user input.
 
#5 - **Hangman**

A game of hangman that utilizes random word choice. In this game, we'll use a separate python file of 5000 random English words to read in and play hangman with. `hangman_words.py`.
We'll be using the `random` package again.

The first step of this game is to get the computer to figure out a word for us to guess, from the list 5000 words. 
*However*, in this list of words, some of the words have dashes (like "black-and-white") or spaces between them - which means we can't use those to play hangman! So we'll have to find a way to bypass that, meaning we'll find valid words and use those only.

Also, we'll import `string` for its alphabet. Of course, for hangman, you'll want some aspect of the game, meaning you don't get unlimited tries. So that will be included in this script as well.

#6 **Tic-Tac-Toe**

A command line version of everyones favorite game, Tic-Tac-Toe. In this game, either a human can play, or the computer can play. A person can play against another person or the computer, and a computer can even play against another computer. To do this, we're going to split up the player in the game into two separate classes. 
When the game is created, you can tell game that what player is 'x' and what player is 'o'.

This game features a plethora of user defined functions that help make the game run smoothly and efficiently.
