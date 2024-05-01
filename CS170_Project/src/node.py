import numpy as np

class Node:
    def __init__(self,
                 state,
                 g_value, #be careful about type here
                 h_value,
                 parent) -> None:
        """_summary_

        Args:
            state (np.array): the state of the 8 puzzle game
            g_value: depth of node on the tree
            h_value: heuristic 
            
        """
        self.state = state
        self.g_value = g_value
        self.h_value = h_value
        self.f_value = g_value + h_value #or g_value + f_value but then dont make it a parameter? 
        self.parent = None
        self.next = None 
        
        