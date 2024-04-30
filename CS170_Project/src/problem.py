import numpy as np
import os
import sys


def swap_elements(arr, idx1, idx2):
    arr[idx1], arr[idx2] = arr[idx2], arr[idx1]
    return arr

def find_blank_tile(state):
    """Return the position of the blank tile (0) in the state"""
    return np.argwhere(state == 0)[0]

def generate_children(initial_state):
    """_summary_

        Args:
             
            
        """
    
    children_list = []
    row, col = find_blank_tile(initial_state)
    
    #possible moves: up, down, left, right
    moves = []
    if row > 0:  #can move up
        moves.append((row - 1, col))
    if row < len(initial_state) - 1:  #can move down
        moves.append((row + 1, col))
    if col > 0:  #can move left
        moves.append((row, col - 1))
    if col < len(initial_state[0]) - 1:  #can move right
        moves.append((row, col + 1))
    
    #generate all possible children by swapping the blank cell with each possible move
    for move in moves: #for each move in the list moves...
        child = np.copy(initial_state)
        swap_elements(child, (row, col), move)
        children_list.append(child)
    
    print(children_list)
        
    
        
        
    
    
        
    
    
    
        