
import unittest

from entities.game_grid import GameGrid, victory_line_length
from entities.player import Player


class TestGameGrid(unittest.TestCase):
    def setUp(self):
        self.player1 = Player("1")
        self.player2 = Player("2")
        self.gamegrid = GameGrid(3, self.player1, self.player2)

    def test__str__(self):
        self.gamegrid.turn = self.player1
        self.gamegrid.place_to_grid(0, 0, self.player1)
        self.gamegrid.place_to_grid(1, 0, self.player2)
        text = str(self.gamegrid)
        test_text = f"\np1 {self.player1.name} | p2 {self.player2.name}"
        test_text += f"\nturn: {self.player1.name}"
        test_text += "\n" + "p1 p2 [] "
        test_text += ("\n" + "[] " * 3) * 2
        print(test_text)
        print(text)
        self.assertEqual(text, test_text)

    def test_victory_line_length(self):
        self.assertEqual(victory_line_length(100), 3)
        self.assertEqual(victory_line_length(3), 3)
        self.assertEqual(victory_line_length(5), 4)
        self.assertEqual(victory_line_length(7), 5)

    def test_empty_grid(self):
        self.gamegrid.place_to_grid(0, 0)
        self.gamegrid.empty_grid()
        test_grid = [[None for ii in range(3)] for i in range(3)]
        self.assertEqual(self.gamegrid.grid, test_grid)

    def test_change_turn(self):
        for i in range(2):
            last_turn = self.gamegrid.turn
            self.gamegrid.place_to_grid(0, 0)
            self.assertNotEqual(last_turn, self.gamegrid.turn)

    def test_not_win(self):
        self.gamegrid.place_to_grid(0, 0)
        self.gamegrid.place_to_grid(0, 1)
        self.gamegrid.place_to_grid(0, 2)
        self.assertEqual(False, self.gamegrid.is_win())

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
            self.gamegrid.place_to_grid(
                y,
                self.gamegrid.grid_size - 1 - y,
                self.player1)
        self.assertEqual(True, self.gamegrid.is_win())

    def test_win_decreasing_diagonal(self):
        self.assertEqual(False, self.gamegrid.is_win())

        self.gamegrid = GameGrid(5, self.player1, self.player2)
        for y in range(0, 4):
            self.gamegrid.place_to_grid(y+1, y, self.player1)
        self.assertEqual(True, self.gamegrid.is_win())

    def test_is_full(self):
        self.assertEqual(False, self.gamegrid.is_full())
        for y in range(3):
            for x in range(3):
                self.gamegrid.place_to_grid(x, y)
        self.assertEqual(True, self.gamegrid.is_full())
