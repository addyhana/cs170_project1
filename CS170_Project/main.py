import os
import sys

from src.state import State

sys.path.append(os.getcwd())

state = State()
board = state.build_board()
state.print_board(board=board)
print()
state.print_board(state.end)