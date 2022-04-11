
import unittest

from entities.GameGrid import GameGrid
from entities.player import Player


class TestGameGrid(unittest.TestCase):
    def setUp(self):
        self.player1 = Player("1")
        self.player2 = Player("2")
        self.gamegrid = GameGrid(3, self.player1, self.player2)

    def test_win_row(self):

        self.assertEqual(False, self.gamegrid.is_win())

        for x in range(3):
            self.gamegrid.place_to_grid(x, 0, self.player1)

        self.assertEqual(True, self.gamegrid.is_win())

    def test_win_column(self):

        self.assertEqual(False, self.gamegrid.is_win())

        for y in range(3):
            self.gamegrid.place_to_grid(0, y, self.player1)

        self.assertEqual(True, self.gamegrid.is_win())

    def test_win_increasing_diagonal(self):
        self.assertEqual(False, self.gamegrid.is_win())

        self.gamegrid = GameGrid(5, self.player1, self.player2)
        for y in range(0, 4):
            self.gamegrid.place_to_grid(y, y+1, self.player1)
        self.assertEqual(True, self.gamegrid.is_win())

    def test_win_decreasing_diagonal(self):
        self.assertEqual(False, self.gamegrid.is_win())

        self.gamegrid = GameGrid(5, self.player1, self.player2)
        for y in range(0, 4):
            self.gamegrid.place_to_grid(y+1, y, self.player1)
        self.assertEqual(True, self.gamegrid.is_win())
