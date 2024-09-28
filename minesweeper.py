import random
import re
# take advantage of object oriented programming tools Python has!
# create a board object to represent the minesweeper game
# this is so that we can just say 'create a new board object' or
# 'dig here', or 'render this game for this object'
class Board:
    def __init__(self, dim_size, num_bombs):
        # keep track of these parameters. they'll be helpful
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        # create the board, using a helper function
        self.board = self.make_new_board() # plant bombs
        self.assign_values_to_board()
        # initialize a set to keep track of which locations that have been uncovered
        # we'll save (row, col) tuples into this set
        self.dug = set() # if we dig at 0, 0, then self.dug = {(0,0)}

    def make_new_board(self):
        # construct a new board based on the dimension size and number of bombs
        # construct the list of lists here
        # since this is a 2-D board, list of lists is most natural

        # generate a new board
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        # this creates an array like this:
        # [[None, None, ..., None],
        #   None, None, ..., None],
        #   [...                 ],
        #   [None, None, ..., None]]
        # represents a board!

        # plant bombs
        bombs_planted = 0
        # use while loop to pick a random location for the bomb
        while bombs_planted < self.num_bombs:
            # return a random integer N such that a <= N <= b
            loc = random.randint(0, self.dim_size**2 - 1) # dimension size squared, minus 1
            # get the row and column of the ID chosen
            row = loc // self.dim_size # how many times is my dimension size divisible by
            col = loc % self.dim_size # divide and get remainder

            if board[row][col] == '*': # star is a bomb
                # this means we've planted a bomb there already, so keep going
                continue
            board[row][col] = '*' # plant the bomb
            bombs_planted += 1
        return board

    def assign_values_to_board(self):
        # Now that we have the bombs planted, assign a number 0-8 for all empty spaces
        # which represents how many neighboring bombs there are
        # we can precompute these, as it'll save some effort
        # for checking around the board later on
        # essentially, we want to check every row and every column
        for r in range(self.dim_size): # row index
            for c in range(self.dim_size): # column index
                if self.board[r][c] == '*':
                # if this is already a bomb, don't calculate anything, so continue
                    continue
                self.board[r][c] = self.get_num_neighboring_bombs(r, c) # function gets number of neighboring bombs

    def get_num_neighboring_bombs(self, row, col):
        # iterate through each of the neighboring positions and sum number of bombs
        # top left: (row-1, col-1)
        # top middle: (row-1, col)
        # top right: (row-1, col+1)
        # left: (row, col-1)
        # right: (row, col+1)
        # bottom left: (row+1, col-1)
        # bottom middle: (row+1, col)
        # bottom right: (row+1, col+1)
        # check all of these, make sure to not go out of bounds
        num_neighboring_bombs = 0 # counter
        # add max and min statements so we don't go out of bounds
        for r in range(max(0, row - 1), min(self.dim_size - 1, row + 1) + 1): # for the current row, we're checking below and above
            for c in range(max(0, col - 1), min(self.dim_size - 1, col + 1) + 1): # for the current column, we're checking to the left and right
                if r == row and c == col:
                    # our original location, don't check this
                    continue
                if self.board[r][c] == '*':
                    num_neighboring_bombs += 1
        return num_neighboring_bombs

    def dig(self, row, col):
        # dig at that location
        # return True if successful dig, False if bomb was dug up
        # SCENARIOS:
            # hit a bomb -> game over
            # dig at location with neighboring bombs -> finish dig
            # dig at location with no neighboring bombs -> recursively dig neighbors!

        self.dug.add((row, col)) # keep track of what we dug
        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True # dig finished since there are neighboring bombs
        # self.board[row][col] = 0
                # add max and min statements so we don't go out of bounds
        for r in range(max(0, row - 1), min(self.dim_size - 1, row + 1) + 1): # for the current row, we're checking below and above
            for c in range(max(0, col - 1), min(self.dim_size - 1, col + 1) + 1): # for the current column, we're checking to the left and right
                if (r, c) in self.dug: # don't dig where already dug
                    continue
                self.dig(r, c)
        # if our initial dig didn't hit a bomb, we shouldn't hit a bomb there
        return True
    
    def __str__(self):
        # if you call print on this object, it'll print out what this function returns
        # we want to return a string that shows the board to the player
        # first, create a new array that represents what the user should see
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row, col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '
        # put this together in a string
        string_rep = ''
        # get max column widths for printing
        widths = []
        # loop through each index for the dimension size
        for idx in range(self.dim_size):
        # get a list of elements in the current column from the visible board
            columns = map(lambda x: x[idx], visible_board)
        # find the maximum width of the elements in the current column and append it to 'widths'
            widths.append(
                len(
                    max(columns, key=len)  # find the longest string in the column
                )
            )

        # create a list of column indices for the top row header
        indices = [i for i in range(self.dim_size)]
        indices_row = '   '  # start with a space for row numbers
        cells = []

        # format and append each index to the header row, adjusting for column width
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"  # create a format string for width
            cells.append(format % (col))  # add the formatted index to 'cells'

        # join the cells and add them to 'indices_row' with proper spacing
        indices_row += '  '.join(cells)
        indices_row += '  \n'  # add a newline at the end of the row

        # loop through each row in the visible board to construct the string representation
        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'  # add the row number with a separator
            cells = []
    
        # format and append each cell in the row according to its column width
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"  # format the cell content based on width
                cells.append(format % (col))  # add the formatted cell to 'cells'
    
        # join the formatted cells and add them to the string representation for this row
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'  # end the row with a newline

        # calculate the length of the separator line based on the length of the string
        str_len = int(len(string_rep) / self.dim_size)

        # add the column header, separator line, board content, and another separator line at the end
        string_rep = indices_row + '-' * str_len + '\n' + string_rep + '-' * str_len
        return string_rep
# play the game 
def play(dim_size = 10, num_bombs = 10): # size of board and number of bombs
    # step 1: create the board, plant the bombs
    board = Board(dim_size, num_bombs) 
    # step 2: show the user the board and ask for where they want to dig

    # step 3a: if location is a bomb, print game over message
    # step 3b: if location is not a bomb, recursively until each square is at least next to do a bomb
    # step 4: repeat steps 2 and 3a or 3b, until there are no more places to dig
    safe = True # we haven't dug anything in the beginning, so safe is True
    while len(board.dug) < board.dim_size ** 2 - num_bombs: # there are no duplicates, it's a set
        print(board)
        # using RegEx to handle inputs of: 0,0 or 0, 0 or 0,    0
        user_input = re.split(',(\\s)*', input("Where would you like to dig? Input as row, col: ")) # '0, 3'
        # use of RegEx is splitting the string. So detect any commas and any white spaces.
        row, col = int(user_input[0]), int(user_input[-1])
        if row < 0 or row >= board.dim_size or col < 0 or col >= dim_size: # out of bounds
            print("Invalid location. Try again.")
            continue
        # if it's valid, dig!
        safe = board.dig(row, col) # whether or not the dig was safe
        if not safe:
            # we hit a bomb...
            break # game over :( [break out of the while loop]

    # now there's two ways to exit this while loop. 
    if safe:
        print("Congratulations. You've won!")
    else: 
        print("Sorry. Game over!")
        # reveal the whole board now
        board.dug = [(r, c) for r in range(board.dim_size) for c in range(board.dim_size)]
        print(board)

    # step 5: if you made it past step 4, congratulations, you've won
    
if __name__ == '__main__':
    play()