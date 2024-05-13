# A Tic Tac Tow board template
#
# Implement the functions to complete a Menace implementation.
# Pure procedural programming is used, i.e. we calculate everything with functions

# Quasi-constants (board size and line size for winning can be defined)
# Custom board configuration
# PLAYERS = ['X', 'O']
# NUM_WIN = 3
# BOARD_ROWS = 3
# BOARD_COLUMNS = 3


# Create an empty board
def init_board():
    return [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

# Print the board to the console
def print_board(board):
    for row in board:
        row_str = '|'
        for cell in row:
            row_str += cell + ' |'
        print(row_str)


# Return the player of the next move
def next_player(board):
    count_X = count_entry(board, "X")
    count_O = count_entry(board, "0")
    if count_X <= count_O:
        return 'X'

    return '0'

# Calculate how many moves a player has already made
def count_entry(board, player):
    count = 0
    for row in board:
         for cell in row:
                if cell == player:
                    count += 1
    return count

# Make a move at a specific position
def move_at(board, pos):
    row = pos // 3
    column = pos % 3
    board[row][column] = next_player(board)


# Get all the moves that are possible for a specific board state
def possible_moves(board):
    moves = []
    curr_move = 0
    for row in board:
        for cell in row:
            if(cell == ' '):
                moves.append(curr_move)
            curr_move += 1
    return moves

# Get an immutable identifier for the board (e.g. for the use in dictionaries)
def get_ident(board):
    identifier = ''
    for row in board:
        for cell in row:
            identifier += cell
    return identifier

# Check wether the game has ended.
# Possible return values are the players, draw, or a continue value
def check_win(board):
    for player in ('X', '0'):
        if check_rows(board, player):
            return player
        elif check_columns(board, player):
            return player
        elif check_diagonals(board,player):
            return player

        if len(possible_moves(board)) == 0:
            return 'D'
    return 'C'

# You might need the following functions to check wether the game has ended:
# Test if a player has a full row
def check_rows(board, player):
    for row in board:
        if row[0] == row[1] == row[2] == player:
            return True
    return False

# Test if a player has a full column
def check_columns(board, player):
    for i_column in range(3):
        if board[0][i_column] == board[1][i_column] == board[2][i_column] == player:
            return True
    return False

# Test if a player has a full diagonal
def check_diagonals(board, player):
    is_diagonal = False
    if board[0][0] == board[1][1] == board[2][2] == player:
        is_diagonal = True
    if board[0][2] == board[1][1] == board[2][0] == player:
        is_diagonal = True
    return is_diagonal