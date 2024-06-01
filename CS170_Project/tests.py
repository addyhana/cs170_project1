import os
import sys
import numpy as np

from src.state import State
from src.search_functions import Algorithms

state = State()
goal_state = state.set_goal()

#------------------------------------------
# trace case
#------------------------------------------
search = Algorithms(initial_state=state.set_start(start = np.array([[1, 0, 3], 
                                            [4, 2, 6], 
                                            [7, 5, 8]
                                        ])),
                    goal_state=goal_state)
solution = search.eucDistTRACE()


#------------------------------------------
# all 6 test cases
#------------------------------------------
search = Algorithms(initial_state=state.set_start(start = np.array([[1, 2, 3], 
                                            [4, 5, 6], 
                                            [7, 8, 0]
                                        ])),
                    goal_state=goal_state)
print("TRIVIAL")
solution = search.missingTile()

search = Algorithms(initial_state=state.set_start(start = np.array([[1, 2, 3], 
                                            [4, 5, 6], 
                                            [7, 0, 8]
                                        ])),
                    goal_state=goal_state)
print("VERY EASY")
solution = search.missingTile()

search = Algorithms(initial_state=state.set_start(start = np.array([[1, 2, 0], 
                                            [4, 5, 3], 
                                            [7, 8, 6]
                                        ])),
                    goal_state=goal_state)
print("EASY")
solution = search.missingTile()

search = Algorithms(initial_state=state.set_start(start = np.array([[0, 1, 2], 
                                            [4, 5, 3], 
                                            [7, 8, 6]
                                        ])),
                    goal_state=goal_state)
print("DOABLE")
solution = search.missingTile()

search = Algorithms(initial_state=state.set_start(start = np.array([[8, 7, 1], 
                                            [6, 0, 2], 
                                            [5, 4, 3]
                                        ])),
                    goal_state=goal_state)
print("OH BOY")
solution = search.ucs()
