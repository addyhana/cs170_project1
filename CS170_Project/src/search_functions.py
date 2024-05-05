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

    def state_to_tuple(state):
        #converts array state to a hashable tuple for tracking parent/child relationship
        return tuple(map(tuple, state))
    
    def ucs(self):
        state = State() 
        frontier = PriorityQueue()
        explored = set()
        parent_map = {}   # stores parent-child relationships for path reconstruction
        depth_map = {}    # stores depths of each state
        order_determiner = 0
        num_nodes = 0 
        biggest_queue = 0 
        
        initial_state_tuple = Algorithms.state_to_tuple(self.initial_state)
        goal_state_tuple = Algorithms.state_to_tuple(self.goal_state)
        
        frontier.put((0, initial_state_tuple))  # initial state with depth 0
        depth_map[initial_state_tuple] = 0

        print ("Beginning uniform cost search... \n")
        
        while not frontier.empty():
            if frontier.qsize() > biggest_queue: 
                biggest_queue = frontier.qsize()
            
            curr_depth, curr_state_tuple = frontier.get()
            curr_state = np.array(curr_state_tuple)
            num_nodes += 1
            
            if np.array_equal(curr_state, self.goal_state):
                # reconstruct direct path using parent_map
                path = []
                while curr_state_tuple in parent_map:
                    path.append(curr_state)
                    curr_state_tuple = parent_map[curr_state_tuple]
                    curr_state = np.array(curr_state_tuple)
                path.append(self.initial_state)  # add the initial state to the path
                path.reverse()  # reverse to get path from start to goal
                i = 0
                for curr_state in path:
                    state.set_state(curr_state)
                    print("Expanding node with g(n) = ", i, "and h(n) = 0")
                    i = i + 1
                    print(f"{curr_state}\n")
                print("Goal reached at depth:", len(path)-1 )
                print("Most nodes in frontier at a single time:", biggest_queue )
                print("Nodes expanded:", num_nodes, "\n")
                return path
            
            explored.add(curr_state_tuple)
            state.set_state(state=curr_state)
            
            # all possible moves
            moves = [
                state.move_up(),
                state.move_down(),
                state.move_left(),
                state.move_right()
            ]
            
            for move in moves:
                if move is not None:
                    move_tuple = Algorithms.state_to_tuple(move)
                    if move_tuple not in explored:
                        # calculate the new depth for the move and replace if better 
                        new_depth = curr_depth + 1
                        if move_tuple not in depth_map or new_depth < depth_map[move_tuple]:
                            depth_map[move_tuple] = new_depth
                            parent_map[move_tuple] = curr_state_tuple
                            #order_determiner += 1
                            frontier.put((new_depth + order_determiner, move_tuple))
        print("Goal not found.")
        print("Nodes expanded:", num_nodes)
        return None
    
    def missingTile(self):
        state = State() 
        frontier = PriorityQueue()
        explored = set()
        parent_map = {}   # stores parent-child relationships for path reconstruction
        f_map = {}    # stores depths of each state
        order_determiner = 0
        num_nodes = 0 
        biggest_queue = 0 
        
        initial_state_tuple = Algorithms.state_to_tuple(self.initial_state)
        goal_state_tuple = Algorithms.state_to_tuple(self.goal_state)
        state.set_state(state=self.initial_state)
        frontier.put((state.heuristic(), initial_state_tuple))  # initial state with f = h 
        f_map[initial_state_tuple] = state.heuristic()

        print ("Beginning missing tile heuristic A* search... \n")
        
        while not frontier.empty():
            if frontier.qsize() > biggest_queue: 
                biggest_queue = frontier.qsize()
            
            curr_f, curr_state_tuple = frontier.get()
            curr_state = np.array(curr_state_tuple)
            num_nodes += 1
            state.set_state(state=curr_state)
            curr_depth = curr_f - state.heuristic()
            
            if np.array_equal(curr_state, self.goal_state):
                # reconstruct direct path using parent_map
                path = []
                while curr_state_tuple in parent_map:
                    path.append(curr_state)
                    curr_state_tuple = parent_map[curr_state_tuple]
                    curr_state = np.array(curr_state_tuple)
                path.append(self.initial_state)  # add the initial state to the path
                path.reverse()  # reverse to get path from start to goal
                i = 0
                for curr_state in path:
                    state.set_state(curr_state)
                    print("Expanding node with g(n) = ", i, "and h(n) = ", state.heuristic())
                    i = i + 1
                    print(f"{curr_state}\n")
                print("Goal reached at depth:", len(path)-1 )
                print("Most nodes in frontier at a single time:", biggest_queue )
                print("Nodes expanded:", num_nodes, "\n")
                return path
            
            explored.add(curr_state_tuple)
            
            # all possible moves
            moves = [
                state.move_up(),
                state.move_down(),
                state.move_left(),
                state.move_right()
            ]
            
            for move in moves:
                if move is not None:
                    move_tuple = Algorithms.state_to_tuple(move)
                    if move_tuple not in explored:
                        # calculate the new f for the move and replace if better 
                        state.set_state(state=move)
                        new_f = curr_depth + 1 + state.heuristic()
                        if move_tuple not in f_map or new_f < f_map[move_tuple]:
                            f_map[move_tuple] = new_f
                            parent_map[move_tuple] = curr_state_tuple
                            #order_determiner += 1
                            frontier.put((new_f + order_determiner, move_tuple))
        
        print("Goal not found.")
        print("Nodes expanded:", num_nodes)
        return None
    
    def eucDist(self):
        state = State() 
        frontier = PriorityQueue()
        explored = set()
        parent_map = {}   # stores parent-child relationships for path reconstruction
        f_map = {}    # stores depths of each state
        order_determiner = 0
        num_nodes = 0 
        biggest_queue = 0 
        
        initial_state_tuple = Algorithms.state_to_tuple(self.initial_state)
        goal_state_tuple = Algorithms.state_to_tuple(self.goal_state)
        state.set_state(state=self.initial_state)
        frontier.put((state.eucFIX(), initial_state_tuple))  # initial state with f = h 
        f_map[initial_state_tuple] = state.eucFIX()

        print ("Beginning Euclidean distance heuristic A* search... \n")
        
        while not frontier.empty():
            if frontier.qsize() > biggest_queue: 
                biggest_queue = frontier.qsize()
            
            curr_f, curr_state_tuple = frontier.get()
            curr_state = np.array(curr_state_tuple)
            num_nodes += 1
            state.set_state(state=curr_state)
            curr_depth = curr_f - state.eucFIX()
            
            if np.array_equal(curr_state, self.goal_state):
                # reconstruct direct path using parent_map
                path = []
                while curr_state_tuple in parent_map:
                    path.append(curr_state)
                    curr_state_tuple = parent_map[curr_state_tuple]
                    curr_state = np.array(curr_state_tuple)
                path.append(self.initial_state)  # add the initial state to the path
                path.reverse()  # reverse to get path from start to goal
                i = 0
                for curr_state in path:
                    state.set_state(curr_state)
                    print("Expanding node with g(n) = ", i, "and h(n) = ", state.eucFIX())
                    i = i + 1
                    print(f"{curr_state}\n")
                print("Goal reached at depth:", len(path)-1 )
                print("Most nodes in frontier at a single time:", biggest_queue )
                print("Nodes expanded:", num_nodes, "\n")
                return path
            
            explored.add(curr_state_tuple)
            
            # all possible moves
            moves = [
                state.move_up(),
                state.move_down(),
                state.move_left(),
                state.move_right()
            ]
            
            for move in moves:
                if move is not None:
                    move_tuple = Algorithms.state_to_tuple(move)
                    if move_tuple not in explored:
                        # calculate the new f for the move and replace if better 
                        state.set_state(state=move)
                        new_f = curr_depth + 1 + state.eucFIX()
                        if move_tuple not in f_map or new_f < f_map[move_tuple]:
                            f_map[move_tuple] = new_f
                            parent_map[move_tuple] = curr_state_tuple
                            #order_determiner += 1
                            frontier.put((new_f + order_determiner, move_tuple))
        
        print("Goal not found.")
        print("Nodes expanded:", num_nodes)
        return None

    def eucDistTRACE(self):
        state = State() 
        frontier = PriorityQueue()
        explored = set()
        path = []
        f_map = {}    # stores depths of each state
        order_determiner = 0
        num_nodes = 0 
        biggest_queue = 0 
        
        initial_state_tuple = Algorithms.state_to_tuple(self.initial_state)
        goal_state_tuple = Algorithms.state_to_tuple(self.goal_state)
        state.set_state(state=self.initial_state)
        frontier.put((state.eucFIX(), initial_state_tuple))  # initial state with f = h 
        f_map[initial_state_tuple] = state.eucFIX()

        print ("\nBeginning Euclidean distance heuristic A* search... \n")
        
        while not frontier.empty():
            if frontier.qsize() > biggest_queue: 
                biggest_queue = frontier.qsize()
            
            curr_f, curr_state_tuple = frontier.get()
            curr_state = np.array(curr_state_tuple)
            num_nodes += 1
            state.set_state(state=curr_state)
            curr_depth = curr_f - state.eucFIX()
            path.append(curr_state)
            
            if np.array_equal(curr_state, self.goal_state):
                print("Total Trace Of Puzzle:")
                i = 0
                for curr_state in path:
                    state.set_state(curr_state)
                    print("Expanding node with g(n) = ", i, "and h(n) = ", state.eucFIX())
                    i = i + 1
                    print(f"{curr_state}\n")
                print("Goal reached at depth:", len(path)-1 )
                print("Most nodes in frontier at a single time:", biggest_queue )
                print("Nodes expanded:", num_nodes, "\n")
                return path
            
            explored.add(curr_state_tuple)
            
            # all possible moves
            moves = [
                state.move_up(),
                state.move_down(),
                state.move_left(),
                state.move_right()
            ]
            
            for move in moves:
                if move is not None:
                    move_tuple = Algorithms.state_to_tuple(move)
                    if move_tuple not in explored:
                        # calculate the new f for the move and replace if better 
                        state.set_state(state=move)
                        new_f = curr_depth + 1 + state.eucFIX()
                        if move_tuple not in f_map or new_f < f_map[move_tuple]:
                            f_map[move_tuple] = new_f
                            frontier.put((new_f + order_determiner, move_tuple))
        
        print("Goal not found.")
        print("Nodes expanded:", num_nodes)
        return None
    
    
        