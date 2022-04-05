import random
from entities.Player import Player
from collections import namedtuple
def victory_line_length(grid_size :int):
        if grid_size == 3: return 3
        if grid_size == 5: return 4
        if grid_size == 7: return 5

class GameGrid:
    def __init__(self, grid_sise :int, player1: Player, player2: Player) -> None:
        self.grid_size = grid_sise
        self.grid = [[None for x in range(grid_sise) ] for y in range(grid_sise)]
        self.player1 = player1
        self.player2 = player2
        self.win_length = victory_line_length(grid_sise)
        self.winner = None
        self.turn = self.player1 if random.choice([True, False]) else self.player2
    
    def __str__(self) -> str:
        ret = f"\np1 {self.player1.name} | p2 {self.player2.name}"
        ret += f"\nturn: {self.turn.name}"
        for y in range(self.grid_size):
            ret += "\n"
            for x in range(self.grid_size):
                if self.grid[y][x] == None:
                    ret += "[] "
                elif self.grid[y][x] == self.player1:
                    ret += "p1 "
                else:
                    ret += "p2 "
        return ret

    def empty_grid(self):
        self.grid = [[None for x in range(self.grid_size) ] for y in range(self.grid_size)]

    def change_turn(self):
        if self.turn == self.player1:
            self.turn = self.player2
        else:
            self.turn = self.player1

    def place_to_grid(self, x, y, player = None):
        if player == None:
            self.grid[y][x] = self.turn
            self.change_turn()
        else:
            self.grid[y][x] = player
        print("clicked","x",x,"y",y,self.grid[y][x].name)

    def is_win(self):
        Point = namedtuple("Point", "x y")
        lines_to_check = []

        #add rows
        for y in range(self.grid_size):
            lines_to_check.append( [ Point(x,y) for x in range(self.grid_size)] )

        #add columns
        for x in range(self.grid_size):
            lines_to_check.append( [ Point(x,y) for y in range(self.grid_size)] )

        #add diagonal lines
        start = self.win_length - self.grid_size
        end =  self.grid_size - self.win_length +1
        for y in range( start, end):
            increasing_diagonal_line = []
            decreasing_diagonal_line = []
            for x in range(self.grid_size):
                if 0<= x-y < self.grid_size:
                    increasing_diagonal_line.append( Point(x , x-y) )
                    decreasing_diagonal_line.append( Point(x-y , x) )

            lines_to_check.append(increasing_diagonal_line)
            lines_to_check.append(decreasing_diagonal_line)

        #add left down to right up
        for y in range( start, end):
            line = []
            for x in range(self.grid_size):
                if 0<= x-y < self.grid_size:
                    line.append( Point(x , x-y) )
            lines_to_check.append(line)
        
        for line in lines_to_check:
            consecutive_count = 0
            consecutive_player = None
            for point in line:
                if self.grid[point.y][point.x] == None:
                    consecutive_count = 0
                else:
                    if consecutive_count >= 1:
                        if consecutive_player != self.grid[point.y][point.x]:
                            consecutive_count == 0
                            consecutive_player = self.grid[point.y][point.x]
                    else:
                        consecutive_player == self.grid[point.y][point.x]
                    consecutive_count +=1
                    if consecutive_count == self.win_length:
                        self.winner = self.grid[point.y][point.x]
                        return True
        return False
    
    
