# from node import Node

class State: 
    def __init__(self,
                #  node: Node
                ) -> None:
        """_summary_

        Args:
            node (Node): _description_
            start (list): _description_
            end (list): _description_
        """
        # self.node = node
        self.end = self.set_goal()


    def build_board(self) -> list(list()):
        return [
            [1, 2, 3], 
            [4, 5, 6], 
            [7, 8, 0]
        ]
    
    def set_goal(self) -> list(list()):
        return [
            [1, 0, 3], 
            [4, 5, 6], 
            [7, 8, 2]
        ]
    
    def print_board(self,
                    board) -> None:
        for x in board:
            print(*x, sep=' ')
        