# A template for a Maze goal search implementation
# - The maze (= game rules) is represented as a 2D list
# - The state of the Maze system is a position within the maze represented as a tuple.
# - The decision making system is again (like Menace) represented as a dictionary of "sugar pearl boxes"
# - Reinforcement learning is used to find the shortest path through the maze

import random

# Quasi constants for system training
NUM_START_PEARLS = 3
LEARN_WIN = 3

# The maze representation
MAZE = [[' ', 'W', ' ', ' ', 'G'],
        [' ', 'W', ' ', 'W', ' '],
        [' ', 'W', ' ', ' ', ' '],
        [' ', ' ', 'W', 'W', ' '],
        [' ', ' ', ' ', ' ', ' ']]

# We start at a certain position
def init_state():
    return (4,0)


# Print the maze (optionally with a position marked)
def print_maze(state=()):
    for i_row, row in enumerate(MAZE):
        row_str = '|'
        for i_column, cell in enumerate(row):
            if state == (i_row, i_column):
                row_str += 'X' + ' | '
            else:
                row_str += cell + ' | '
        print(row_str)


# Make a move within the maze (the move is assumed to be valid)
def make_move(state, move):
    return (state[0] + move[0], state[1] + move[1])


#def possible_moves(state):
#    moves = []
#    for i_row, row in enumerate(MAZE):
#        for i_column, cell in enumerate(row):
 #           if is_in_same_column(state, i_column) or is_in_same_row(state, i_row):    
#            return moves
#        pass
#    pass


# When the position matches the goal, we're done
def goal_reached(state):
    return MAZE[state[0]][state[1]] == 'G'


# Get a move from our learning system
def get_move(gps, state):
    if state not in gps.keys():
        gps[state] = init_pearls(state)

    pearls = gps[state]
    return calc_move(pearls)


# Get a move from one of our learning system entries
# Helper for get_move(gps, state)
def calc_move(pearls):
    return random.choice(pearls)


# Initialize a new box (i.e. learning system entry)
def init_pearls(state):
    moves = possible_moves(state)
    pearls = []
    for move in moves:
        pearls = pearls + [move] * NUM_START_PEARLS
    return pearls


# Play a game of maze. Do try to reach the goal and record the game history.
def game(gps):
    state = init_state()
    hist = []
    while not goal_reached(state):
        move = get_move(gps, state)
        hist.append((state, move))
        state = make_move(state, move)
    return hist


# Print a game history
def print_hist(hist):
    for state, _ in hist:
        print_maze(state)
        print('')


# Update the learning system with a game history
def update(gps, hist):
    hist_reversed = hist.reverse()
    while len(hist_reversed) > 0:
        state, move = hist_reversed[0]
        gps[state] = gps[state] + [move] * LEARN_WIN
        hist_remaining = []
        for state_compare, move_compare in hist_reversed:
            if state_compare == state:
                if move != move_compare:
                    if move_compare in gps[state]:
                        gps[state].remove(move_compare)
            else:
                hist_remaining.append(state_compare, move_compare)
        hist_reversed = hist_remaining
        

# Perform a couple of maze games and learn from them
def train(gps, n_times):
    for i in range(n_times):
        if i % 100 == 0:
            print(f"Train run: {i}")
        hist = game(gps)
        update(gps, hist)
    return


# Try out the system:
my_gps = {}
my_state = init_state()
print_maze()
hist = game(my_gps)

# Perform a single game and print the game history:
# my_hist = game(my_gps)
# print("Length of game history before training: " + str(len(my_hist)))
# print_hist(my_hist)

# Perform a lot of games and train the system:
# Is the path to the goal now shorter?
# train(my_gps, 1000)

# my_hist = game(my_gps)
# print("Length of game history after training: " + str(len(my_hist)))
# print_hist(my_hist)