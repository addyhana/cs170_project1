# from node import Node
from typing import Optional
import numpy as np
import copy

class State: 
    def __init__(self,
                #  node: Node
                ) -> None:
        """
        Args:
            node (Node): _description_
            start (list): _description_
            end (list): _description_
        """
        # self.node = node
        self.end = self.set_goal()
        self.current_state = None


    def set_start(self,
                  start: Optional[np.array] = None):
        #print("hi")
        if start is None:
            self.current_state =  np.array([[1, 2, 3], 
                                            [4, 5, 6], 
                                            [7, 8, 0]
                                        ])  
            return self.current_state
        
        self.current_state = start
        #print(self.current_state)
        return self.current_state
    
    def set_goal(self):
        return np.array([
            [1, 2, 3], 
            [4, 5, 6], 
            [7, 8, 0]
        ])
    
    def set_state(self,
                  state):
        self.current_state = state
    
    def find_blank_tile(self):
        for row in range(len(self.current_state)):
            for column in range(len(self.current_state)):
                if self.current_state[row][column] == 0:
                    return row, column
                
    
    
    def move_up(self):
        row, column = self.find_blank_tile()
        curr_state = copy.deepcopy(self.current_state)

        
        if row > 0:
            temp_state = curr_state[row][column]
            curr_state[row][column] = curr_state[row - 1][column]
            curr_state[row - 1][column] = temp_state
            return curr_state
        
        return None
        
        
    def move_down(self):
        row, column = self.find_blank_tile()
        curr_state = copy.deepcopy(self.current_state)
        
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
    
    
    def heuristic(self):
        goal = self.set_goal()
        boxes_away = np.sum(self.current_state != goal)
        if boxes_away > 0: 
            boxes_away = boxes_away - 1
        return boxes_away
        