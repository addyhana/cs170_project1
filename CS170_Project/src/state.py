# from node import Node
from typing import Optional
import numpy as np
import copy
import math

class State: 
    def __init__(self,
                ) -> None:
        self.end = self.set_goal()
        self.current_state = None


    def set_start(self,
                  start: Optional[np.array] = None):
        if start is None: # default (trivial) state if none is provided
            self.current_state =  np.array([[1, 2, 3], 
                                            [4, 5, 6], 
                                            [7, 8, 0]
                                        ])  
            return self.current_state
        # else, set provided array as current state     
        self.current_state = start
        return self.current_state
    
    def set_goal(self): # set_goal is hard-coded, but unnecessary to call search algos
        return np.array([
            [1, 2, 3], 
            [4, 5, 6], 
            [7, 8, 0]
        ])
    
    def set_state(self,
                  state):
        self.current_state = state
    
    def find_blank_tile(self):
        state = self.current_state
        curr_position = np.where(state == 0)
        row, col = curr_position[0][0], curr_position[1][0]

        return row, col
                
    
    # all four operators, swapping tiles in given direction
    def move_up(self):
        row, column = self.find_blank_tile()
        #deep copy ensures no changes are made to initial state
        curr_state = copy.deepcopy(self.current_state)
        
        if row > 0:
            temp_state = curr_state[row][column]
            curr_state[row][column] = curr_state[row - 1][column]
            curr_state[row - 1][column] = temp_state
            return curr_state
        # returns none if move cannot be made 
        return None 
        
        
    def move_down(self):
        row, column = self.find_blank_tile()
        curr_state = copy.deepcopy(self.current_state)
        # note: each operator has different location constraints
        if row < 2:            
            temp_state = curr_state[row][column]
            curr_state[row][column] = curr_state[row + 1][column]
            curr_state[row + 1][column] = temp_state
            return curr_state
                     
        return None
            
            
    def move_right(self):
        row, column = self.find_blank_tile()
        curr_state = copy.deepcopy(self.current_state)
        
        if column < 2:
            temp_state = curr_state[row][column]
            curr_state[row][column] = curr_state[row][column + 1]
            curr_state[row][column + 1] = temp_state
            return curr_state
            
        return None
            
    def move_left(self):
        row, column = self.find_blank_tile()
        curr_state = copy.deepcopy(self.current_state)
        
        if column > 0:            
            temp_state = curr_state[row][column]
            curr_state[row][column] = curr_state[row][column - 1]
            curr_state[row][column - 1] = temp_state
            return curr_state
            
        return None
        
    
    
    def print_board(self,
                    board) -> None:
        for x in board:
            print(*x, sep=' ')
    
    # missing tile heuristic, sums total tiles that do not match goal
    def heuristic(self):
        goal = self.set_goal()
        boxes_away = np.sum(self.current_state != goal)

        # accounts for when the previous line adds the '0' to the heuristic
        # and it should be removed from the count 
        if boxes_away > 0: 
            boxes_away = boxes_away - 1
        return boxes_away
    
    #euclidean distance heuristic, sums all euclidean distances from all misplaced tiles
    def euc_distance(self):
        goal_state = self.set_goal()
        state = self.current_state

        distance = 0
        # does NOT include blank tile
        for i in range(1,9):
            # current pos for tile 
            curr_position = np.where(state == i)
            curr_row, curr_col = curr_position[0][0], curr_position[1][0]

            # target pos for matching tile (bottom right)
            goal_position = np.where(goal_state == i)
            goal_row, goal_col = goal_position[0][0], goal_position[1][0]

            # euc dist from original to final
            distance += np.sqrt((curr_row - goal_row)**2 + (curr_col - goal_col)**2)
        
        return distance