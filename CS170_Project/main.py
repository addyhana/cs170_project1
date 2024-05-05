import os
import sys
import numpy as np

from src.state import State
from src.tree import Tree
from src.problem import generate_children
from src.menu import main_menu
from src.search_functions import Algorithms

sys.path.append(os.getcwd()) #you can access files in the same directory this way



#state = State()
#board = state.build_board()
#state.print_board(board=board)
#print()
#state.print_board(board=state.end)

# main_menu()

state = State()
# state.set_start())
goal_state = state.set_goal()
#print(new_state)


# search = Algorithms(initial_state=state.set_start(start = np.array([[1, 2, 3], 
#                                             [4, 5, 6], 
#                                             [7, 8, 0]
#                                         ])),
#                     goal_state=goal_state)

# solution = search.ucs()
# print("trivial:")
# for i in solution:
#     print(f"{i}\n")

search = Algorithms(initial_state=state.set_start(start = np.array([[1, 2, 0], 
                                            [4, 5, 3], 
                                            [7, 8, 6]
                                        ])),
                    goal_state=goal_state)

solution = search.ucs()
print("easy:")
for i in solution:
    print(f"{i}\n")

search = Algorithms(initial_state=state.set_start(start = np.array([[1, 2, 0], 
                                            [4, 5, 3], 
                                            [7, 8, 6]
                                        ])),
                    goal_state=goal_state)

solution = search.missingTile()
print("easy:")
for i in solution:
    print(f"{i}\n")




# search = Algorithms(initial_state=state.set_start(start = np.array([[8, 7, 1], 
#                                             [6, 0, 2], 
#                                             [5, 4, 3]
#                                         ])),
#                     goal_state=goal_state)

# solution = search.ucs()
# print("oh boy:")
# for i in solution:
#     print(f"{i}\n")