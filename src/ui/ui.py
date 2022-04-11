from entities.game_grid import GameGrid
from entities.player import Player
from ui.grid_view import GridView
from ui.settings_view import SettingsView
from ui.highscore_view import HighscoresView
from tkinter import *


class UI:

    def __init__(self, root: Tk):
        self._root = root
        self._root.columnconfigure(0, weight=1)
        self._root.rowconfigure(0, weight=1)
        self._current_view = None

    def start(self):
        grid = GameGrid(3, Player("X"), Player("O"))
        self._handle_settings_view(grid)

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _handle_grid_view(self, grid):
        self._show_grid_view(grid)

    def _show_grid_view(self, grid):
        self._hide_current_view()
        self._current_view = GridView(
            self._root,
            self._handle_highscores_view,
            grid
        )
        self._current_view.pack()

    def _handle_settings_view(self, grid):
        self._show_settings_view(grid)

    def _show_settings_view(self, game_grid):
        self._hide_current_view()
        self._current_view = SettingsView(
            self._root,
            self._handle_grid_view,
            game_grid
        )
        self._current_view.pack()

    def _show_highscores_view(self, game_grid):
        self._hide_current_view()
        self._current_view = HighscoresView(
            self._root,
            self._show_grid_view,
            self._show_settings_view,
            game_grid
        )
        self._current_view.pack()

    def _handle_highscores_view(self, game_grid):
        self._show_highscores_view(game_grid)
