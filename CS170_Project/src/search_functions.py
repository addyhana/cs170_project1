from src.state import State
from queue import PriorityQueue
import numpy as np

class Algorithms:
    
    #initial state and goal state given in search fnc calls, allows for expansion into
    #different types of puzzles 
    def __init__(self,
                 initial_state: State,
                 goal_state: State) -> None:
        self.initial_state = initial_state
        self.goal_state = goal_state

    #converts array state to a hashable tuple for tracking parent/child relationships 
    def state_to_tuple(state):
        return tuple(map(tuple, state))
    
    def ucs(self):
        state = State() 
        frontier = PriorityQueue() # uses priority queue with g(n) as priority
        explored = set()
        parent_map = {}   # stores parent-child relationships for path reconstruction @ end 
        depth_map = {}    # stores depths of each state 
        num_nodes = 0 
        biggest_queue = 0 
        
        # converts initial state to a tuple so it can be hashed into depth map and put in frontier
        initial_state_tuple = Algorithms.state_to_tuple(self.initial_state)
        
        frontier.put((0, initial_state_tuple))  
        depth_map[initial_state_tuple] = 0 # initial state has a depth of 0

        print ("\nBeginning uniform cost search... \n")
        
        # generic search algorithm shell fitted to UCS 
        while not frontier.empty():
            # re-checking to see if frontier has a new biggest size for output
            if frontier.qsize() > biggest_queue: 
                biggest_queue = frontier.qsize()
            
            curr_depth, curr_state_tuple = frontier.get()
            curr_state = np.array(curr_state_tuple)
            
            # checks if current state == goal state 
            if np.array_equal(curr_state, self.goal_state): 
                # reconstruct direct path using parent_map
                path = []
                while curr_state_tuple in parent_map:
                    path.append(curr_state)
                    curr_state_tuple = parent_map[curr_state_tuple]
                    curr_state = np.array(curr_state_tuple)
                path.append(self.initial_state)  # add the initial state to the path @ end 
                path.reverse()  # reverse to get path from start to goal
                i = 0
                # prints final optimal path using parent map
                for curr_state in path:
                    state.set_state(curr_state)
                    print("Expanding node with g(n) = ", i, "and h(n) = 0")  
                    i = i + 1
                    print(f"{curr_state}\n")
                # printing extra information about search
                print("Goal reached at depth:", len(path)-1 )
                print("Most nodes in frontier at a single time:", biggest_queue )
                print("Nodes expanded:", num_nodes, "\n")
                return path
            
            num_nodes += 1 # node is expanded, incr. counter for output 
            explored.add(curr_state_tuple)
            state.set_state(state=curr_state)
            
            moves = [
                state.move_up(),
                state.move_down(),
                state.move_left(),
                state.move_right()
            ]
            
            for move in moves:
                # checks to ensure move is viable (i.e. moving left on 1st column would be false)
                if move is not None:
                    move_tuple = Algorithms.state_to_tuple(move)
                    if move_tuple not in explored:
                        # calculate the new depth for the move, incr. by 1
                        new_depth = curr_depth + 1
                        if move_tuple not in depth_map or new_depth < depth_map[move_tuple]:
                            # update depth if better one is found and re-enter into prio. queue 
                            depth_map[move_tuple] = new_depth
                            parent_map[move_tuple] = curr_state_tuple
                            frontier.put((new_depth, move_tuple))
        # if loop terminates without finding goal state, unsolvable puzzle 
        print("Goal not found.")
        print("Nodes expanded:", num_nodes) # how many nodes were checked before failure
        return None
    
    def missingTile(self):
        state = State() 
        frontier = PriorityQueue()
        explored = set()
        parent_map = {}   # stores parent-child relationships for path reconstruction
        f_map = {}    # stores f(n) of each state
        num_nodes = 0 
        biggest_queue = 0 
        
        initial_state_tuple = Algorithms.state_to_tuple(self.initial_state)
        state.set_state(state=self.initial_state)

        # initial state with f(n) = h(n), since depth = 0
        frontier.put((state.heuristic(), initial_state_tuple)) 
        f_map[initial_state_tuple] = state.heuristic()

        print ("\nBeginning missing tile heuristic A* search... \n")
        # shell is the same as the UCS algorithm, just including a heuristic
        # (comments on shared logic isn't repeated)
        while not frontier.empty():
            if frontier.qsize() > biggest_queue: 
                biggest_queue = frontier.qsize()
            
            curr_f, curr_state_tuple = frontier.get()
            curr_state = np.array(curr_state_tuple)
            
            state.set_state(state=curr_state)
            #since the frontier stores f(n), can calculate the depth by subtracting heuristic
            curr_depth = curr_f - state.heuristic()
            
            if np.array_equal(curr_state, self.goal_state):
                path = []
                while curr_state_tuple in parent_map:
                    path.append(curr_state)
                    curr_state_tuple = parent_map[curr_state_tuple]
                    curr_state = np.array(curr_state_tuple)
                path.append(self.initial_state)
                path.reverse()
                i = 0
                for curr_state in path:
                    state.set_state(curr_state)
                    # h(n) no longer hardcoded to 0, calling heuristic on current state we're printing
                    print("Expanding node with g(n) = ", i, "and h(n) = ", state.heuristic())
                    i = i + 1
                    print(f"{curr_state}\n")
                print("Goal reached at depth:", len(path)-1 )
                print("Most nodes in frontier at a single time:", biggest_queue )
                print("Nodes expanded:", num_nodes, "\n")
                return path
            
            num_nodes += 1
            explored.add(curr_state_tuple)
            
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
                        # calculate new f(n) with incr. depth and adding heuristic of the move 
                        state.set_state(state=move)
                        new_f = curr_depth + 1 + state.heuristic()
                        if move_tuple not in f_map or new_f < f_map[move_tuple]:
                            f_map[move_tuple] = new_f
                            parent_map[move_tuple] = curr_state_tuple
                            frontier.put((new_f, move_tuple))
        
        print("Goal not found.")
        print("Nodes expanded:", num_nodes)
        return None
    
    def eucDist(self):
        state = State() 
        frontier = PriorityQueue()
        explored = set()
        parent_map = {}   # stores parent-child relationships for path reconstruction
        f_map = {}    # stores f(n) of each state
        num_nodes = 0 
        biggest_queue = 0 
        
        initial_state_tuple = Algorithms.state_to_tuple(self.initial_state)
        state.set_state(state=self.initial_state)

        # initial state with f(n) = h(n), since depth = 0
        frontier.put((state.euc_distance(), initial_state_tuple))  
        f_map[initial_state_tuple] = state.euc_distance()

        print ("\nBeginning Euclidean distance heuristic A* search... \n")
        # shell is the same as the UCS algorithm, just including a heuristic
        # (comments on shared logic isn't repeated)
        while not frontier.empty():
            if frontier.qsize() > biggest_queue: 
                biggest_queue = frontier.qsize()
            
            curr_f, curr_state_tuple = frontier.get()
            curr_state = np.array(curr_state_tuple)
            state.set_state(state=curr_state)
            # same procedure to find current depth, just subtracting euc. distance instead
            curr_depth = curr_f - state.euc_distance()
            
            if np.array_equal(curr_state, self.goal_state):
                path = []
                while curr_state_tuple in parent_map:
                    path.append(curr_state)
                    curr_state_tuple = parent_map[curr_state_tuple]
                    curr_state = np.array(curr_state_tuple)
                path.append(self.initial_state) 
                path.reverse()  
                i = 0
                for curr_state in path:
                    state.set_state(curr_state)
                    print("Expanding node with g(n) = ", i, "and h(n) = ", state.euc_distance())
                    i = i + 1
                    print(f"{curr_state}\n")
                print("Goal reached at depth:", len(path)-1 )
                print("Most nodes in frontier at a single time:", biggest_queue )
                print("Nodes expanded:", num_nodes, "\n")
                return path
            
            num_nodes += 1
            explored.add(curr_state_tuple)
            
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
                        state.set_state(state=move)
                        #same procedure to find new f(n) for next moves
                        new_f = curr_depth + 1 + state.euc_distance()
                        if move_tuple not in f_map or new_f < f_map[move_tuple]:
                            f_map[move_tuple] = new_f
                            parent_map[move_tuple] = curr_state_tuple
                            #order_determiner += 1
                            frontier.put((new_f, move_tuple))
        
        print("Goal not found.")
        print("Nodes expanded:", num_nodes)
        return None

    # duplicate version of eucDist (previous), but instead of tracking optimal path,
    # prints out entire search trace (per project specs)
    #
    # otherwise, it is exactly the same 
    def eucDistTRACE(self):
        state = State() 
        frontier = PriorityQueue()
        explored = set()
        # note: no parent map, just list of all nodes expanded 
        path = []
        f_map = {}  
        order_determiner = 0
        num_nodes = 0 
        biggest_queue = 0 
        
        initial_state_tuple = Algorithms.state_to_tuple(self.initial_state)
        state.set_state(state=self.initial_state)

        frontier.put((state.euc_distance(), initial_state_tuple))
        f_map[initial_state_tuple] = state.euc_distance()

        print ("\nBeginning Euclidean distance heuristic A* search... \n")
        
        while not frontier.empty():
            if frontier.qsize() > biggest_queue: 
                biggest_queue = frontier.qsize()
            
            curr_f, curr_state_tuple = frontier.get()
            curr_state = np.array(curr_state_tuple)
            
            state.set_state(state=curr_state)
            curr_depth = curr_f - state.euc_distance()
            path.append(curr_state)
            
            if np.array_equal(curr_state, self.goal_state):
                # note: no need to reconstruct a path, just print total trace 
                print("Total Trace Of Puzzle:")
                i = 0
                for curr_state in path:
                    state.set_state(curr_state)
                    print("Expanding node with g(n) = ", i, "and h(n) = ", state.euc_distance())
                    i = i + 1
                    print(f"{curr_state}\n")
                print("Goal reached at depth:", len(path)-1 )
                print("Most nodes in frontier at a single time:", biggest_queue )
                print("Nodes expanded:", num_nodes, "\n")
                return path
            
            num_nodes += 1
            explored.add(curr_state_tuple)
            
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
                        state.set_state(state=move)
                        new_f = curr_depth + 1 + state.euc_distance()
                        if move_tuple not in f_map or new_f < f_map[move_tuple]:
                            f_map[move_tuple] = new_f
                            frontier.put((new_f + order_determiner, move_tuple))
        
        print("Goal not found.")
        print("Nodes expanded:", num_nodes)
        return None
    
    
        