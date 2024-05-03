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


search = Algorithms(initial_state=state.set_start(start = np.array([[0, 2, 3], 
                                            [1, 8, 4], 
                                            [7, 6, 5]
                                        ])),
                    goal_state=goal_state)

solution = search.ucs()
for i in solution:
    print(f"{i}\n")