# A template to implement the "Sudoku" problem with search

import random

from search import Search

# Size of the "Tiles" problem
SIZE = 3


# In the goal state
# cell (i, j) contains the number i*N + j
def get_goal():
    pass

# The goal state as a quasi-constant
GOAL = get_goal()


# Helpful method: Get a random start state
def make_initial(n_steps):
    current = get_goal()
    for _ in range(n_steps):
        current = random.choice(next_states(current))
    return current

# Helpful method for printing fields with a size > 3
def get_num_digits(number):
    digits = 1
    while number >= 10:
        number = number // 10
        digits = digits + 1
    return digits

# Helpful quasi-constant to print fields with size > 3
MAX_DIGITS = get_num_digits(SIZE * SIZE - 1)


# Helpful method to print fields with size > 3
def cell_to_str(cell):
    n_digits = get_num_digits(cell)
    spacing = ' ' * (MAX_DIGITS - n_digits)
    if cell == 0:
        cell = ' '
    return spacing + str(cell)

# Print the state
def print_state(state):
    pass

# Determine if we have reached the goal
def is_goal(state):
    pass

# Get the position of the empty tile
# Returns row and column number
# This might be helpful...
def get_empty_tile(state):
    pass

# Get the next states
def next_states(state):
    pass


# start_state = make_initial(30)
# search = Search(is_goal, next_states, print_state)
# path_opt = search.breadth_first(start_state)
# search.print_path(path_opt)