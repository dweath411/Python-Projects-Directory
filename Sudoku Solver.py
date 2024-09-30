def find_next_empty(puzzle):
    # finds the next row, col on the puzzle that's not filled yet
    # replace it with -1
    # return row, col, tuple (or (None, None), if there is none)
    # keep in mind, we are using 0-8 for indices
    for r in range(9): # iterate through 9 rows
        for c in range(9): # range(9) is 0, 1, 2, ..., 8
            if puzzle[r][c] == -1:
                return r, c
    return None, None # if no spaces in the puzzle are empty (-1)

def is_valid(puzzle, guess, row, col):
    # determines whether the guess as the row/col of the puzzle is a valid guess
    # returns True if valid, False otherwise
    row_vals = puzzle[row] # start with the row!
    if guess in row_vals:
        return False
    
    col_vals = [] # now, do the columns. a little it trickier
    # for i in range(9): another way to do it as done below
    #     col_vals.append(puzzle[i][col])
    col_vals = [puzzle[i][col] for i in range(9)] # build the list
    if guess in col_vals:
        return False
    
    # and now, we do the square
    # to do this, we want to get where the 3 x 3 square starts
    # iterate over the 3 values in the row/column
    row_start = (row // 3) * 3 # take the row index, divide by 3 and drop the remainder
    # ex: 1 // 3 would be 0 instead of 0.33, 5 // 3 would be 1 since 3 goes in 5 once
    col_start = (col // 3) * 3
    for r in range(row_start, row_start + 3): # + 3 because we want to iterate through 3 rows/columns
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
        # if we get to this point, the checks pass, so we can return True
    return True
def solve_sudoku(puzzle):
    '''
     solve soduku using a backtracking technique
     the puzzle we pass in is a list of lists
     each inner list is a row in the sodoku puzzle
     it represents a 9 x 9 puzzle
     return whether or not a solution exists
     mutates puzzle to be the solution, if solution exists
    '''
    # step 1: choose somewhere on the puzzle to go
    row, col = find_next_empty(puzzle)
    # step 1.1: if there's no where left, then we're done because we only allowed valid inputs
    if row is None: 
        return True # puzzle solved
    
    # step 2: if there is a place to put a number, then make a guess between 1 and 9
    for guess in range(1, 10): # range(1, 10) is 1, 2, 3, ..., 9
        #step 3: check if this is a valid guess
        if is_valid(puzzle, guess, row, col):
            # step 3.1: if this is valid, place that guess on the puzzle
            puzzle[row][col] = guess # mutating puzzle array
            # now, recurse using this puzzle
            # step 4: recursively call our function
            if solve_sudoku(puzzle):
                return True
        
        # step 5: if not valid check is not actually valid OR if our guess does not solve the puzzle
        # we would need to backtrack and try a new number
        puzzle[row][col] = -1 # resetting the guess

    # step 6: if none of the numbers that we try work, then this puzzle is unsolvable
    return False

if __name__ == '__main__':
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
    print(solve_sudoku(example_board))
    print(example_board)