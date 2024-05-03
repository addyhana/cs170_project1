import numpy as np
import os
import sys
from src.state import State

def swap_elements(arr, idx1, idx2):
    #helper function for generate_children
    arr[idx1], arr[idx2] = arr[idx2], arr[idx1]
    return arr

def find_blank_tile(state): 
    """Return the position of the blank tile (0) in the state"""
    return np.argwhere(state == 0)[0]

def generate_children(initial_state): #EDIT SO IT DOES NOT RETURN REPEAT STATES
    """
        Args:
            initial_state: the initial/current state of our problem
            
        Summary:
            This function returns the list of children states given a state   
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
    
    return children_list


def delete_repeats(visited, new_states):
    print("repeat function")
    for state in new_states:
        #if the new state is a repeat
        if np.any(np.all(state == visited, axis=1)):
            #then delete the repeat
            new_states.pop(new_states.index(state))
    
    
def goal_state_found(states_list):
    print("checks if goal state is found")
    state = State()
    array_to_check = state.set_goal()
    return np.any(np.all(array_to_check == states_list, axis=1))
        
def explore_state(init_state):
    print("exploring function")
    visited = []
    new_states = []
    
    #append initial state to new_states list 
    new_states.append(init_state)
    
    for state in new_states:
        new_states = delete_repeats(visited, new_states) #delete repeats
        num_parent_states = len(new_states)
        
        new_states = new_states + generate_children(state) #add the new states
        
        #check if new states contains goal state 
        if goal_state_found(new_states):
            print("GOAL FOUND")
            break
        
        #move parent state(s) to visited 
        visited = visited + new_states[:num_parent_states]
    
        
        
        
    
    
    
    
        
        

    
 
        
        
    
    
        
    
    
    
        