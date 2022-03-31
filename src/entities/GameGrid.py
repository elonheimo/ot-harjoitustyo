from entities import Player

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
    
    def place_to_grid(self, x, y, player: Player):
        self.grid[y][x] = player

    def is_win(self):
        #check rows
        for y in range(self.grid_size):
            consecutive_count = 0
            consecutive_player = None
            for x in range(self.grid_size):
                if self.grid[y][x] == None:
                    consecutive_count = 0
                else:
                    if consecutive_count >= 1:
                        if consecutive_player != self.grid[y][x]:
                            consecutive_count == 0
                            consecutive_player = self.grid[y][x]
                    else:
                        consecutive_player == self.grid[y][x]
                    consecutive_count +=1
                    if consecutive_count == self.win_length:
                        self.winner = self.grid[y][x]
                        return True
        #check columns
        for x in range(self.grid_size):
            consecutive_count = 0
            consecutive_player = None
            for y in range(self.grid_size):
                if self.grid[y][x] == None:
                    consecutive_count = 0
                else:
                    if consecutive_count >= 1:
                        if consecutive_player != self.grid[y][x]:
                            consecutive_count == 0
                            consecutive_player = self.grid[y][x]
                    else:
                        consecutive_player == self.grid[y][x]
                    consecutive_count +=1
                    if consecutive_count == self.win_length:
                        self.winner = self.grid[y][x]
                        return True
        #check left up to right down
        #check left down to right up
        return False

    def winner():
        pass
    
    
