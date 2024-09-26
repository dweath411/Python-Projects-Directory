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

# add the same get_move function for the player
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

# now, we're going to create a genius computer.

class GeniusComputerPlayer(Player):
    def __init__(self, letter): 
        super().__init__(letter)

    def get_move(self, game):
        # another version of get_move, where the magic happens
        if len(game.available_moves()) == 9: # if all spaces are available, just choose one
            square = random.choice(game.available_moves())
        else: 
            # get the square based off the minimax algorithm
            square = self.minimax(game, self.letter)['position']
        return square
    
    # defining minimax
    def minimax(self, state, player): # called 'state' and not 'game', just a variable name
        max_player = self.letter # you
        other_player = 'O' if player == 'X' else 'X' # whatever letter you are not

        # first, check if the previous move is a winner
        # this is our base case
        if state.current_winner == other_player:
            # return position and score because we need to keep track of the score for minimax to work
            return {'position': None,
                    'score': 1 * (state.number_of_empty_squares() + 1) 
                    if other_player == max_player else -1 * (state.number_of_empty_squares() +1)}
        
        elif not state.empty_squares(): # no empty squares
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf} # dictionary to save the best position to move
            # each score should be maximize
        else: 
            best = {'position': None, 'score': math.inf} # trying to minimize
        for possible_move in state.available_moves():
            # step 1: make a move, try that spot
            state.make_move(possible_move, player)
            # step 2: recurse using minimize to simulate a game after making that move
            sim_score = self.minimax(state, other_player) # alternate players
            # step 3: undo that move
            state.board[possible_move] = ' ' # empty space
            state.current_winner = None # undoing the move
            sim_score['position'] = possible_move # otherwise, this will get messed up from the recursion
            # step 4: update dictionaries, if necessary
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score # replace best score
            else: 
                if sim_score['score'] < best['score']:
                    best = sim_score # replace best
            
        return best
