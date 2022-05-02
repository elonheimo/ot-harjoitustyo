import random
from collections import namedtuple
from entities.player import Player
from repositories.highscore_repository import HighscoreRepository


def victory_line_length(grid_size: int) -> int:
    """Returns reguired line length for a win in tic-tac-toe

    Args:
        grid_size (int): size of the game grid
    """
    if grid_size == 3:
        return 3
    if grid_size == 5:
        return 4
    if grid_size == 7:
        return 5
    return 3


class GameGrid:
    """Class that maintains tic-tac-toe game logic

    Attributes:
        grid_size: Size of the grid
        grid: two dimensional list for storing grid
        player1: player object
        player2: player object
        win_length: reguired line length for victory
        winner: references the player that has won
        turn: references player which turn it currently is
        highscore_repo: HighscoreRepository object for database interaction
    """
    def __init__(self, grid_size: int, player1: Player, player2: Player) -> None:
        """Class constructor. Initialises new GameGrid object.

        Args:
            grid_size (int): must be 3, 5 or 7
            player1 (Player):
            player2 (Player):
        """
        self.grid_size = grid_size
        self.grid = [[None for x in range(grid_size)]
                     for y in range(grid_size)]
        self.player1 = player1
        self.player2 = player2
        self.win_length = victory_line_length(grid_size)
        self.winner = None
        self.turn = self.player1 if random.choice(
            [True, False]) else self.player2
        self.highscore_repo = HighscoreRepository()

    def __str__(self) -> str:
        ret = f"\np1 {self.player1.name} | p2 {self.player2.name}"
        ret += f"\nturn: {self.turn.name}"
        for y in range(self.grid_size):
            ret += "\n"
            for x in range(self.grid_size):
                if self.grid[y][x] is None:
                    ret += "[] "
                elif self.grid[y][x] == self.player1:
                    ret += "p1 "
                else:
                    ret += "p2 "
        return ret

    def empty_grid(self):
        """Empties the grid object
        """
        self.grid = [[None for x in range(self.grid_size)]
                     for y in range(self.grid_size)]

    def change_turn(self):
        """Changes turn object from one player to another
        """
        if self.turn == self.player1:
            self.turn = self.player2
        else:
            self.turn = self.player1

    def place_to_grid(self, x: int, y: int, player: Player = None):
        """Places a Player to xy co-ordinate in grid

        Args:
            x (int): x coord
            y (int): y coord
            player (Player, optional): reference to player object. Defaults to None.
        """
        if player is None:
            self.grid[y][x] = self.turn
            self.change_turn()
        else:
            self.grid[y][x] = player
        print("clicked", "x", x, "y", y, self.grid[y][x].name)

    def _get_lines_to_check(self) -> list:
        """Return the lines to check for victory

        Returns:
            list: elements are namedtuple point with x and y values
        """
        Point = namedtuple("Point", "x y")
        lines_to_check = []

        # add rows
        for y in range(self.grid_size):
            lines_to_check.append([Point(x, y) for x in range(self.grid_size)])

        # add columns
        for x in range(self.grid_size):
            lines_to_check.append([Point(x, y) for y in range(self.grid_size)])

        # add diagonal lines
        start = self.win_length - self.grid_size
        end = self.grid_size - self.win_length + 1
        for y in range(start, end):
            increasing_diagonal_line = []
            decreasing_diagonal_line = []
            for x in range(self.grid_size):
                if 0 <= x-y < self.grid_size:
                    increasing_diagonal_line.append(
                        Point(x-y,
                              self.grid_size-1-x))
                    decreasing_diagonal_line.append(Point(x-y, x))

            lines_to_check.append(increasing_diagonal_line)
            lines_to_check.append(decreasing_diagonal_line)

        return lines_to_check

    def grid_size_as_text(self):
        """Return grid size as str. Example '3x3'
        """
        return f"{self.grid_size}x{self.grid_size}"

    def _update_highscore_repo(self):
        """Calls HighscoreRepository object to add event row to database
        """
        self.highscore_repo.add_event(
            self.winner.name, "WIN", self.grid_size_as_text())
        if self.player1 is not self.winner:
            self.highscore_repo.add_event(
                self.player1.name, "LOSE", self.grid_size_as_text())
        else:
            self.highscore_repo.add_event(
                self.player2.name, "LOSE", self.grid_size_as_text())

    def get_highscores(self):
        """Top 5 players. example element ['Name',6]
        """
        return self.highscore_repo.get_highscores(
            self.grid_size_as_text()
        )

    def is_win(self) -> bool:
        """Checks if self.grid contains winning line and updates self.winner to winning player

        Returns:
            bool: True if there is a win. False if no win.
        """
        lines_to_check = self._get_lines_to_check()

        for line in lines_to_check:
            consecutive_count = 0
            consecutive_player = None
            for point in line:
                if self.grid[point.y][point.x] is None:
                    consecutive_count = 0
                else:
                    if consecutive_count >= 1:
                        if consecutive_player != self.grid[point.y][point.x]:
                            consecutive_count = 0
                            consecutive_player = self.grid[point.y][point.x]
                    else:
                        consecutive_player = self.grid[point.y][point.x]
                    consecutive_count += 1
                    if consecutive_count == self.win_length:
                        self.winner = self.grid[point.y][point.x]
                        self._update_highscore_repo()
                        return True
        return False
