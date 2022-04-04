
from ui.grid_view import GridView
from ui.settings_view import SettingsView
from tkinter import *


class UI:

    def __init__(self, root):
        self._root = root
        self._root.columnconfigure(0, weight=1)
        self._root.rowconfigure(0, weight=1)
        self._current_view = None

    def start(self):
        #self._show_grid_view()
        self._show_settings_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _show_grid_view(self,grid):
        self._hide_current_view()
        self._current_view = GridView(self._root,grid)
        self._current_view.pack()

    def _show_settings_view(self):
        self._hide_current_view()
        self._current_view = SettingsView(
            self._root,
            self._show_grid_view    
        )
        self._current_view.pack()