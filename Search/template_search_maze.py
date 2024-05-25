# A template for a first solution to solve the "Maze" problem with
# breadth-first search.
# Markus Mayer

from search import Search

MAZE = [[' ', 'W', ' ', ' ', 'G'],
        [' ', 'W', ' ', 'W', ' '],
        [' ', 'W', ' ', ' ', ' '],
        [' ', ' ', 'W', 'W', ' '],
        [' ', ' ', ' ', ' ', ' ']]


# Print the maze (optionally with a position marked)
def print_state(state=()):
    for i in range(len(MAZE)):
        print('|', end='')
        for j in range(len(MAZE[i])):
            if len(state) == 2 and state[0] == i and state[1] == j:
                print('X|', end='')
            else:
                print(MAZE[i][j] + '|', end='')
        print('')


# When the position matches the goal, we're done
def is_goal(state):
    return MAZE[state[0]][state[1]] == 'G'


# Make a move within the maze (the move is assumed to be valid)
def make_move(state, move):
    return state[0] + move[0], state[1] + move[1]


# Get all possible moves from a certain position
def next_states(state):
    states_ok = []
    moves_all = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for move in moves_all:
        next_state = make_move(state, move)
        if next_state[0] >= 0 and next_state[1] >= 0 \
                and next_state[0] < len(MAZE) \
                and next_state[1] < len(MAZE[0]) \
                and MAZE[next_state[0]][next_state[1]] != '0':
            states_ok.append(move)
    return states_ok

# Implementation of breadth-first search
# The function should return the path to the goal
def breadth_first(start_state):
    to_do = [[start_state]]
    while to_do:
        path = to_do.pop(0)
        current = path[-1]
        if is_goal(current):
            return path
        for state in next_states(current):
            if not state in path or not is_state_in_to_do(state, to_do):
                to_do.append(path + [state])
    return []


def is_state_in_to_do(state, to_do):
    for path in to_do:
        if state in path:
            return True
    return False

# Print a solution path
def print_path(path):
    for state in path:
        print_state(state)
        print('')


search = Search(is_goal, next_states, print_state)
path = search.breadth_first((0, 0))
search.print_path(path)

