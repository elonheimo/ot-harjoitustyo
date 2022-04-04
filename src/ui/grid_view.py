from functools import partial
from tkinter import *
from entities import *
from entities.GameGrid import GameGrid
from entities.Player import Player

class GridView:
    def __init__(self, root, game_grid : GameGrid):
        self._root = root
        self._frame = None

        ##FIX
        self._game_grid = game_grid
        self._button_frame = None
        self._initialize()

                
    def pack(self):
        self._frame.grid(row=0,column=0,sticky=E+W+S+N)
        self._frame.columnconfigure(0, weight=1)
        self._frame.rowconfigure(0, weight=1)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = Frame(master=self._root)
        self._root.rowconfigure(0, weight=1)
        self._root.columnconfigure(0, weight=1)
        self._addButtons()


    def _addButtons(self):

        self.buttonFrame = Frame( master= self._frame)
        self.buttonFrame.rowconfigure(0, weight=1)
        self.buttonFrame.columnconfigure(0, weight=1)

        self.buttonFrame.grid(row=0, column=0, sticky=N+S+E+W)

        for y in range(self._game_grid.grid_size):
            for x in range(self._game_grid.grid_size):
                if self._game_grid.grid[y][x] == None:

                    def button_click(x,y):
                        if self._game_grid.grid[y][x] == None:
                            self._game_grid.place_to_grid(x,y)
                            self._addButtons()

                    button = Button(self.buttonFrame, command = partial(button_click,x,y))
                    button.grid(row = y, column = x, sticky=N+S+E+W)
                else:
                    if self._game_grid.grid[y][x] == self._game_grid.player1:
                        text = "X"
                    else: text = "O"
                    label = Label(self.buttonFrame, text = text)
                    label.grid(row = y, column = x, sticky=N+S+E+W)
        self.buttonFrame.rowconfigure(tuple( range( self._game_grid.grid_size ) ), weight=1)
        self.buttonFrame.columnconfigure(tuple( range( self._game_grid.grid_size ) ), weight=1)
