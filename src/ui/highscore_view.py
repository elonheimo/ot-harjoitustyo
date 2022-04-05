from tkinter import *

from entities.GameGrid import GameGrid


class HighscoresView:
    def __init__(self, root, show_grid_view, show_settings_view, game_grid : GameGrid):
        self._root = root
        self._show_grid_view = show_grid_view
        self._game_grid = game_grid
        self._game_grid.empty_grid()
        self._show_settings_view = show_settings_view
        self._frame = None
        self._initialize()

                
    def pack(self):
        self._frame.grid(row=0,column=0,sticky=E+W+S+N)
        self._frame.columnconfigure(0, weight=1)
        self._frame.rowconfigure(0, weight=1)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = Frame(master=self._root)
        
        title_label = Label(master= self._frame, text = "Highscores")
        play_again_button = Button(
            master = self._frame,
            text= "Play again",
            command= lambda : self._show_grid_view(self._game_grid)
        )
        settings_button = Button(
            master = self._frame,
            text="Settings",
            command= lambda : self._show_settings_view(self._game_grid)
        )

        #add functionality to buttons

        title_label.grid(row=0,column=0,columnspan=2, sticky=N+S+E+W)

        play_again_button.grid(row=2,column=0, sticky=N+S+E+W)
        settings_button.grid(row=2,column=1, sticky=N+S+E+W)
        