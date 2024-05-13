# A Menace implementation template
#
# Implement the functions to complete a Menace implementation.
# Pure procedural programming is used, i.e. we calculate everything with functions
from random import choice

# Quasi-constants for learning parameters
from board_template import *

NUM_START_PEARLS = 20

LEARN_WIN = 5
LEARN_LOSS = -1
LEARN_DRAW = 1

# Calculate the random move
def calc_move(matchbox):
    return choice(matchbox)


# Initialize a new matchbox (i.e. pearl content)
def init_pearls(board):
    moves = possible_moves(board)
    return moves * NUM_START_PEARLS


# Get a move from menace for a board identifier
def get_move(menace, board):
    state = get_ident(board)
    if state not in menace:
        menace[state] = init_pearls(board)
    matchbox = menace[state]
    return calc_move(matchbox)


# Get a completely random move (might be helpful for implementing a random player)
def get_random_move(board):
    moves = possible_moves(board)
    return choice(moves)

# Play a game between menace and itself (should return the game history and the winner)
def game(menace):
    board = init_board()
    current_win = 'C'
    game_history = []
    while check_win(board) == 'C':
        state = get_ident(board)
        player = next_player(board)
        action = get_move(menace, board)

        # Tupel aus Zustand, welcher Spieler dran ist und welcher Zug ausgeführt wird
        game_history.append((state, player, action))
        
        move_at(board, action)
        current_win = check_win(board)
    return game_history, current_win


# Play a game between menace and a random player (should return the game history and the winner)
def game_random(menace):
    board = init_board()
    current_win = 'C'
    game_history = []
    while check_win(board) == 'C':
        state = get_ident(board)
        player = next_player(board)
        if player == 'X':
            action = get_move(menace, board)
            if action > 8:
                print("Fehler, da Move ungültig ist")
        else:
            action = get_random_move(board)

        game_history.append((state, player, action))
        move_at(board, action)
        current_win = check_win(board)

    return game_history, current_win


# Update menace with a game history and the result of the game
def update(menace, hist, result):
    for state, player, action in hist:
        if result == 'D':
            menace[state] += [action] * LEARN_DRAW
        elif player == result:
            menace[state] += [action] * LEARN_WIN
        else:
            for n in range(-LEARN_LOSS):
                if action in menace[state]:
                    menace[state].remove(action)
    return

# Train menace by playing a lot of games (you might introduce a parameter for the opponent)
def train(menace, n_plays):
    for curr_play in range(n_plays):
        game_history, result = game(menace)
        update(menace, game_history, result)
        print_hist(game_history)
    return menace



# Play a lot of games without training menace (you might introduce a parameter for the opponent)
def tournament(menace, n_plays):
    pass


# Print the game history
def print_hist(hist):
    for state, player, action in hist:
        print(f"State: \n{draw_state(state)}, Player: {player}, Action: {action}")
    print()

#Prints the state of the current game more user friendly
def draw_state(state):
    # converts the current state to a board
    board = convert_state_to_board(state)
    board_str = ''

    for row_index in range(len(board)):
        for cell_index in range(len(board[row_index])):
            board_str += " " + board[row_index][cell_index] + " "
            if cell_index < 2:
                board_str += "|"
        if row_index < 2:
            board_str += "\n" + "--- " * 3 + "\n"
        row_index += 1
    return board_str


def convert_state_to_board(state):
    board = [[' '] * 3 for _ in range(3)]
    index = 0
    for i in range(3):
        for j in range(3):
            board[i][j] = state[index]
            index += 1
    return board


board = init_board()
matchbox = init_pearls(board)
menace = {}

train(menace, 100)
#hist, winner = game(menace)
#print_hist(hist)