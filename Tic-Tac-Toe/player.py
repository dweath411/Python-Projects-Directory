import math
import random

class Player:
    def __init__(self, letter): # initialize the player class with the letter that the player is going to represent
        # letter is x or o
        self.letter = letter
    # we want all players to get their next move given a game
    def get_move(self, game):
        pass

# use inheritance to create a random computer player and a human computer player that builds on top of the base player object
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter) # call the initialization in the super class, which is the player

    def get_move(self, game):
        # for the random computer player, we're going to have a choose a spot on the board that's empty
        square = random.choice(game.available_moves()) 
        return square 

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # we want to human player to choose a spot based on an input passed through terminal
        # keep iterating until they get a valid square
        valid_square = False
        val = None # because user hasn't chosen a value yet
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8): ')
            # check that this is a correct value by trying to cast it to an integer
            # if it's not an integer, then we say its invalid
            # if the spot is not available on the board, we also say its invalid
            try:
                val = int(square) # make sure the value is an integer
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True # if these are successful, good
            except ValueError:
                print('Invalid square. Try again.')
            return val


