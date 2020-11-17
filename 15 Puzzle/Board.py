from copy import deepcopy
from os import system
from random import randint, seed
from queue import Queue # import Queue class from queue library


MAX_COL = 4
MAX_ROW = 4
SHUFFLE_MAGNITUDE = 50

class Board():

    def __init__(self):
        """construct a board"""
        self.goal = [[" 1"," 2"," 3"," 4"],
                     [" 5"," 6"," 7"," 8"],
                     [" 9","10","11","12"],
                     ["13","14","15","__"]]
                    
        
        self.board = deepcopy(self.goal)

        self.e_loc = [MAX_ROW - 1, MAX_COL - 1]

        """create a moves dict, no () after self.move_up cause we don't want to 
        call the funtion"""
        self.moves = {0: self.move_up, 1: self.move_right, 2: self.move_down, 3: self.move_left}


    def __repr__(self):
        """represent the board"""
        for i in range (MAX_ROW):
            for j in range (MAX_COL):
                print(self.board[i][j], end = " ")
            print()
        
        # __repr__ must return something
        return ""

    
    def refresh(self):
        """clear the screen and print the board"""
        system ("cls")
        print("Welcome to the game of 15 puzzle!\n")
        print(self)

        if self.board == self.goal:
            print("\nCongrats! You won!")
            return False
        else:
            return True


    def shuffle(self):
        """randomise the board using succession of legal moves"""

        seed()
        for i in range(SHUFFLE_MAGNITUDE):
            m = randint(0,3)
            self.moves[m](self.board, self.e_loc)

        """for aesthetic purposes, move the empty location to the lower right corner"""
        for i in range(MAX_ROW):
            self.moves[2](self.board, self.e_loc)

        for i in range(MAX_COL):
            self.moves[1](self.board, self.e_loc)



    def move(self, board, e_loc, x, y):
        """make legal moves"""
        if e_loc[0] + x < 0 or e_loc[0] + x > 3 or e_loc[1] + y < 0 or e_loc[1] + y > 3:
            return board, e_loc    
        # swap
        board[e_loc[0]][e_loc[1]], board[e_loc[0] + x][e_loc[1] + y] = board[e_loc[0] + x][e_loc[1] + y], board[e_loc[0]][e_loc[1]]
        # update empty location
        e_loc[0] += x
        e_loc[1] += y
        # return updated board, updated empty location
        return board, e_loc


    def move_up(self, board, e_loc):
        return self.move(board, e_loc, -1, 0)

    def move_down(self, board, e_loc):
        return self.move(board, e_loc, 1, 0)

    def move_left(self, board, e_loc):
        return self.move(board, e_loc, 0, -1)

    def move_right(self, board, e_loc):
        return self.move(board, e_loc, 0, 1)

    def solve(self):
        """solve the game using breadth first search BFS algorithm"""
        # self.board = deepcopy(self.goal)"""

        def successors(board, e_loc):
            b_lst = [deepcopy(board), deepcopy(board), deepcopy(board), deepcopy(board)]
            e_loc_lst = [list(e_loc), list(e_loc), list(e_loc), list(e_loc)]
            b_lst[0], e_loc_lst[0] = self.move_up(b_lst[0], e_loc_lst[0])
            b_lst[1], e_loc_lst[1] = self.move_right(b_lst[1], e_loc_lst[1])
            b_lst[2], e_loc_lst[2] = self.move_down(b_lst[2], e_loc_lst[2])
            b_lst[3], e_loc_lst[3] = self.move_left(b_lst[3], e_loc_lst[3])

            return [[b_lst[0], e_loc_lst[0], 0], [b_lst[1], e_loc_lst[1], 1], [b_lst[2], e_loc_lst[2], 2], [b_lst[3], e_loc_lst[3], 3]]



        searched = set()
        fringe = Queue()

        # Put an item into the queue
        fringe.put ({"board": self.board, "e_loc": self.e_loc, "path": []})

        while True:
            
            # quit if no solution is found
            if fringe.empty():
                return []
            
            # inspect current node
            node = fringe.get() # get() remove and return an item from the queue

            # quit if node contains goal
            if node["board"] == self.goal:
                return node["path"]

            # if not goal, add node to searched list, put its children in the fringe
            if str(node["board"]) not in searched:
                searched.add(str(node["board"]))
                # child contains board, location and direction
                for child in successors(node["board"], node["e_loc"]):
                    if str(child[0]) not in searched:
                        fringe.put ({"board": child[0], "e_loc": child[1], "path": node["path"] + [child[2]]})





