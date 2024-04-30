from src.state import State
import numpy as np

def check_array(starting_state: np.array):
    expected_values = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
    unique_vals = np.unique(starting_state)
    if np.array_equal(np.sort(expected_values), np.sort(unique_vals)):
        return True
    return False

def build_custom_puzzle():
    board = []

    for i in range(3):
        num = input(f"Enter row {i + 1} with a space between each number: ")
        num = num.split()
        board.append(num)
    board = np.array(board).reshape(3,3)
    return board.astype(dtype=int)
    


def main_menu():
    print("Welcome to the 8-puzzle solver.")
    state = State()
    flag = False
    
    
    while flag == False: 
        try: 
            print('Type "1" to use a default puzzle, or "2" to enter your own puzzle.')
            num = int(input())
            
            if num == 1:
                print("default layout being used...")
                starting_state = state.set_start()
                flag = True
        
            elif num == 2:
                print("Enter your puzzle, use a zero to represent the blank")
                print("Enter 9 numbers (including 0) in left to right order for the 3x3 puzzle.")   
                
                starting_state = build_custom_puzzle()
                starting_state = state.set_start(start=starting_state)
                if check_array(starting_state=starting_state):
                    flag = True
                else:
                    print(f"The puzzle may include repeated numbers or not have numbers 0-8... please try again")
        
            else:
                print(f"Invalid input: {num}... please use only 1 or 2")
                
        except ValueError as v:
            print(f"Error caught, please revise: {v}")
            
                     
    print("Enter your choice of algorithm: ")
    print('Type "1" for Uniform Cost Search, "2" for A* with the Misplaced Tile heuristic, or "3" for A* with the Euclidean distance heuristic.')
    choice = input()
    

 
        