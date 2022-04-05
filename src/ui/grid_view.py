from cProfile import label
from doctest import master
from functools import partial
from tkinter import *
from entities import *
from entities.GameGrid import GameGrid
from entities.Player import Player

class GridView:
    def __init__(self, root, handle_hichscores_view, game_grid : GameGrid):
        self._root = root
        self._handle_hichscores_view = handle_hichscores_view
        self._game_grid = game_grid
        self._frame = None
        self._button_frame = None
        self._turn_label = None
        self._initialize()

                
    def pack(self):
        self._root.rowconfigure(0, weight=1)
        self._root.columnconfigure(0, weight=1)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = Frame(master=self._root)

        self._frame.grid(row=0,column=0,sticky=E+W+S+N)
        self._frame.columnconfigure(0, weight=1)
        self._frame.rowconfigure(0, weight=1)

        self._turn_label = Label(
            master= self._frame,
            text=f"{self._game_grid.turn.name}'s turn"
        )
        self._turn_label.grid(row=0, column=0, columnspan=self._game_grid.grid_size)

        self._addButtons()

    def _button_click(self, x, y):

        if self._game_grid.grid[y][x] == None:
                self._game_grid.place_to_grid(x,y)
                self._addButtons()

        if self._game_grid.is_win():
            self._turn_label["text"] = f"{self._game_grid.winner.name} won. Press here to exit"
            self._turn_label.bind(
                "<Button-1>",#"<Return>", #"<Button-1>", 
                lambda e: self._handle_hichscores_view(self._game_grid)
            )
        else:
            self._turn_label["text"] = f"{self._game_grid.turn.name}'s turn"

        print(self._game_grid)

    def _addButtons(self):

        self.buttonFrame = Frame( master= self._frame)
        self.buttonFrame.rowconfigure(0, weight=1)
        self.buttonFrame.columnconfigure(0, weight=1)

        self.buttonFrame.grid(row=1, column=0, sticky=N+S+E+W)

        for y in range(self._game_grid.grid_size):
            for x in range(self._game_grid.grid_size):
                if self._game_grid.grid[y][x] == None:
                    onClick = lambda a, b : self._button_click(a, b)
                    button = Button(
                        self.buttonFrame,
                        command = partial(onClick,x,y)
                    )
                    button.grid(row = y, column = x, sticky=N+S+E+W)
                else:
                    if self._game_grid.grid[y][x] == self._game_grid.player1:
                        text = "X"
                    else: text = "O"
                    label = Label(self.buttonFrame, text = text)
                    label.grid(row = y, column = x, sticky=N+S+E+W)
        self.buttonFrame.rowconfigure(tuple( range( self._game_grid.grid_size ) ), weight=1)
        self.buttonFrame.columnconfigure(tuple( range( self._game_grid.grid_size ) ), weight=1)
