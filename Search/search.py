# Implementation of general search and helper methods
# Markus Mayer

class Search:

    # The search instance is created with 3 parameters:
    # is_goal: A function that defines if we have reached the goal. It takes a state as argument.
    # next_states: A function that generates the next possible states for a given state.
    # print_state: A function to print a single state to the console
    def __init__(self, is_goal, next_states, print_state):
        self.is_goal = is_goal
        self.next_states = next_states
        self.print_state = print_state

    # Find the shortest path with breadth-first search
    def breadth_first(self, start_state):
        paths = [[start_state]]
        while len(paths) > 0:
            path = paths.pop(0)
            current_state = path[-1]

            if self.is_goal(current_state):
                return path

            for state in self.next_states(current_state):
                if state not in path and not is_in_paths(paths, state):
                    paths.append(path + [state])
        return []

    # Try to find some solution with depth-first search
    def depth_first(self, start_state):
        paths = [[start_state]]
        while paths:
            path = paths.pop()
            current_state = path[-1]

            if self.is_goal(current_state):
                return path

            for state in self.next_states(current_state):
                if state not in path \
                        and not is_in_paths(paths, state):
                    paths.append(path + [state])
        return []

    # Print a solution path
    def print_path(self, path):
        for state in path:
            self.print_state(state)
            print('')

# Helper function to check if state has already been visited
def is_in_paths(paths, state):
    for path in paths:
        if state in path:
            return True
    return False

