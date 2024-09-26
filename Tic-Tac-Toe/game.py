# the actual game will be in this file

from player import HumanPlayer, RandomComputerPlayer
from super_player import GeniusComputerPlayer
import time

class TicTacToe:
    def __init__(self): #  need a 3 x 3 board to play the game! 
        self.board = [' ' for _ in range(9)] # use a single list to replicate 3x3 board
        self.current_winner = None # keep track of winner, and if there is, who won

    def print_board(self):
        # index into the length 9 list
        # [i*3:(i+1)*3] is saying which group of 3 spaces are we choosing (indices 012 are the first row, 345 is the second row, etc)
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |') # join the string where the separator is a vertical line
    
    @staticmethod 
    # use a staticmethod because this part doesn't relate to any specific board
    # don't have to pass in a 'self'
    # print out which numbers correspond to which spot
    def print_board_nums():
        # example: 0 | 1 | 2 , etc. tells us what number corresponds to what box
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)] # the same range we made earlier. gives us the indices are in the rows for each of the rows
        for row in number_board: # concatenate strings in similar fashion to self.board
            print('| ' + ' | '.join(row) + ' |')
    
    # with how the logic of tic tac toe works, we're going to need to know the available moves after you've placed your letter
    def available_moves(self): # return a list of a indices []
        return [i for i, spot in enumerate(self.board) if spot == ' '] # a cleaner one liner to do what the below chunk of code does
        # moves = [] # initialize moves to an empty list
        # for (i, spot) in enumerate(self.board) # enumerate a list and assign tuples
        #     # ['x', 'x', 'o'] --> [(0, 'x'), (1, 'x'), (2, 'o')]
        #     if spot ==  ' ': # if the spot chosen is an empty space, we now know it's an available move
        #         moves.append(i) # append the index so we know what spaces are available   
        # return moves
    def empty_squares(self): 
        # function to check if there are empty squares on the board
        return ' ' in self.board
        # returns a Boolean of whether or not there are empty spaces on the board

    def number_of_empty_squares(self): 
        # checking the number of empty squares
        return self.board.count(' ') # counts the number of spaces on the board
    
    def make_move(self, square, letter): 
        # we need information on what square the user wants their move to be at
        # if the move is valid, then we can make the move and return True
        # if invalid, just return False (this shouldn't happen)
        if self.board[square] == ' ': # if self.board(square) is empty, then assign that letter to that given square
            self.board[square] = letter 
            print(f'Made move {letter} at square {square}')  # Debugging: Print the move
            # toggle current_winner to the winner if there is one
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    # define a function that checks for a winner
    def winner(self, square, letter): # winner if 3 in a row anywhere. check row, diagonal, and columns
        row_ind = square // 3 # checking if there are 3 in a row
        row = self.board[row_ind*3: (row_ind + 1) * 3]
        print(f'Checking row: {row}')  # Debugging: Print the row
        if all([spot == letter for spot in row]): # check every spot in the row, whether or not every spot has the same letter
            return True
        
        # check columns next
        col_ind = square % 3 # divide by 3 and take the remainder
        column = [self.board[col_ind + i*3] for i in range(3)]
        print(f'Checking column: {column}')  # Debugging: Print the column
        if all([spot == letter for spot in column]):
            return True

        # check diagonals
        # only if the square is an even number (0, 2, 4, 6, 8)
        # these are the only moves possible to win a diagonal
        if square % 2 == 0: # if square is divisible by 2 (i.e, even)
            diagonal1 = [self.board[i] for i in [0, 4, 8]] # left to right diag
            diagonal2 = [self.board[i] for i in [2, 4, 6]] # right to left diag
            print(f'Checking diagonals: {diagonal1}, {diagonal2}')  # Debugging: Print the diagonals
            if all([spot == letter for spot in diagonal1]):
                return True
            if all([spot == letter for spot in diagonal2]):
                return True
        # if all of these checks fail, then there is no winner yet, so return False
        return False
    
# define a function outside of the class TicTacToe, where we pass in a game, an x player and an o player
def play(game, x_player, o_player, print_game=True): 
    # returns the winner of the game (The letter), or None for a tie
    if print_game:
        game.print_board_nums()  # print numbers corresponding to board positions
    letter = 'X'  # starting letter
    print(f'Initial board: {game.board}')  # Debugging: Initial board state
    print(f'Available moves: {game.available_moves()}')
    # iterate while the game still has empty squares
    # there is no need to worry about the winner because we'll return that, which then breaks the loop
    while game.empty_squares():
        # get the move from the appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        # if the move is valid, make the move and continue the game
        if game.make_move(square, letter):
            if print_game:
                print(f'{letter} makes a move to square {square}')
                game.print_board()  # new representation of the board
                print('')  # empty line for spacing


            # Debugging: Print board and available moves
            print(f'Current board: {game.board}')
            print(f'Available moves: {game.available_moves()}')
            print(f'Current winner: {game.current_winner}')
            # check if there's a winner after this move
            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter  # exit the function when someone wins
            # alternate between X and O
            letter = 'O' if letter == 'X' else 'X'

        time.sleep(0.8)  # tiny pause so the game doesn't progress too fast

    # If the loop ends and there is no winner, it's a tie
    if print_game:
        print('It\'s a tie!')

# def play(game, x_player, o_player, print_game=True): 
#     # returns the winner of the game (The letter), or None for a tie
#     if print_game:
#         game.print_board_nums()  # print numbers corresponding to board positions
#     letter = 'X'  # starting letter
    
#     # iterate while the game still has empty squares
#     # there is no need to worry about the winner because we'll return that, which then breaks the loop
#     while game.empty_squares():
#         # get the move from the appropriate player
#         if letter == 'O':
#             square = o_player.get_move(game) # if the letter is the O player, prompt them to make a move
#         else:
#             square = x_player.get_move(game)  # if it's not letter O, then it must be the X player, so prompt them to get a move

#         if game.make_move(square, letter):
#             if print_game:
#                 print(f'{letter} makes a move to square {square}')
#                 game.print_board() # new representation of the board
#                 print('')  # empty line for spacing

# # if current_winner is not set to None anymore, then a letter has won
#             if game.current_winner:
#                 if print_game:
#                     print(letter + ' wins!')
#                 return letter  # exit the function when someone wins

#             # alternate between X and O
#             letter = 'O' if letter == 'X' else 'X'
#               # if letter == 'X':
#                 # letter = 'O'
#             # else:
#                 # letter = 'X'
#         time.sleep(0.8)  # tiny pause so the game doesn't progress too fast

#     # If the loop ends and there is no winner, it's a tie
#     if print_game:
#         print('It\'s a tie!')


# play game
if __name__ == '__main__':
    # import functions from 'player.py' for this to work
    x_player = HumanPlayer('X')
    #o_player = RandomComputerPlayer('O')
    # comment the other o_player to play with a default computer player
    o_player = GeniusComputerPlayer('O')
    # this o_player is the unbeatable AI
    game = TicTacToe()
    play(game, x_player, o_player, print_game=True)


