# from node import Node
from typing import Optional
import numpy as np

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


    def set_start(self,
                  start: Optional[np.array] = None):
        if start is None:   
            return np.array([
                [1, 2, 3], 
                [4, 5, 6], 
                [7, 8, 0]
            ])
        return start
    
    def set_goal(self):
        return np.array([
            [1, 0, 3], 
            [4, 5, 6], 
            [7, 8, 2]
        ])
    
    def print_board(self,
                    board) -> None:
        for x in board:
            print(*x, sep=' ')
        