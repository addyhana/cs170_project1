from src.state import State
from queue import PriorityQueue
import numpy as np

class Algorithms:
    
    def __init__(self,
                 initial_state: State,
                 goal_state: State) -> None:
        self.initial_state = initial_state
        self.goal_state = goal_state
        
        
    def is_array_in_list(self, target, list_arrays):
        for array in list_arrays:
            if np.array_equal(target, array):
                return True
        return False
    
    
    def ucs(self):
        state = State()
        frontier = PriorityQueue()
        explored = []
        path = []
        depth = 0
        order_determiner = 0
        
        frontier.put((depth, self.initial_state))
        num_nodes = 1 # start at 1 to account for initial state
        
        while not frontier.empty():
            curr_state = frontier.get()[1]
            path.append(curr_state)
            
            if np.array_equal(curr_state, self.goal_state):
                #print("found ucs goal")
                return path
            
            explored.append(curr_state)
            state.set_state(state=curr_state)
            
            up_move = state.move_up()
            down_move = state.move_down()
            left_move = state.move_left()
            right_move = state.move_right()
            moves = [up_move, down_move, left_move, right_move]
            
            num_nodes += 1
            depth = np.floor(np.log(num_nodes) + 1)
            
            for move in moves: 
                if move is not None:
                    if not any(np.array_equal(move, item[1]) for item in frontier.queue):
                        if not self.is_array_in_list(move, explored):
                            order_determiner += 1
                            frontier.put((depth + order_determiner, move))

        return None