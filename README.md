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

#7 **Unwinnable Tic-Tac-Toe! (AI)**

We've done one version of a tic-tac-toe game. How about we up the ante, and make the game unwinnable? You can tie, but you can never win! To do this, we'll introduce `minimax`.

minimax is a decision making algorithm built off of a maximizer and minimizer concept. You essentially are trying to maximize your win while your opponent is trying to minimize their loss. With tic-tac-toe, we can step though each state and see how minimax might help us win.

In minimmax, we are trying to find the best move to make. We can determine this by deducing which move is the most optimal. To do this, we'll use a `utility` function, a measurement of how valuable the final result in that decision tree is.

There will be some overlap of code in these files as the last tic-tac-toe files.

#8 **Binary Search**
What is Binary Search? Binary Search algorithm is a divide and conquer type of algorithm. It helps you search an ordered list in a faster way than scanning every single element in the list. 

An example of how Binary Search works:
Assume there is some list of ordered elements we have, from least to greatest. We're trying to see if a target is in the list, and if it is, return the index of where it is. 

In Binary Search, we can go to the middle elemnt of the list and ask, "Is the target equal to, less than, or greater than this middle element. If it's equal to, then that's our element. If it's less than, then we know it has to be on the left side of that element, so we can completely disregard everything to the right (greater than) of the middle element. Vice versa for if it is greater than that middle element. Reiterate. Divide and conquer! We will prove that Binary Search is faster than Naive Search (iterating through a list and asking "is this my element?" one by one until it's reached.)

#9 **Minesweeper**

Next up - Minesweeper. To make this command line minesweeper game, we're going to be using recursion and classes. This is explicitly a very bare bones command line version of the game. Potentially, I'll decide to make improvements to the game in the future. This is strictly for practice on learning to code, translating ideas and translating algorithms into Python code.

#10 **Sudoku Solver**

A Sudoku solver using backtracking, recursion, and mutation. Mostly simple project, if you give it a board it will solve the puzzle. The important part is knowing how to format the board and make it clearly viewable.

If this is your example board:
 
  example_board = [

        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]

It should run smoothly, of course you can change the numbers how you see fit though. When you run it in the terminal, you'll have to resize your screen so it looks like a normal sudoku board. The program will return True if the puzzle is solved, otherwise, it will be False.



