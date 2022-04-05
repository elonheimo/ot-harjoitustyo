from functools import partial
from tkinter import *

from entities.GameGrid import *

class SettingsView:
    def __init__(self, root, handle_grid_view, game_grid : GameGrid):
        self._handle_grid_view = handle_grid_view
        self._game_grid = game_grid
        self._root = root
        self._frame = None
        self._player1_entry = None
        self._player2_entry = None
        self._selected_grid_size = None
        self._initialize()

    def pack(self):
        self._frame.grid(row=0,column=0,sticky=E+W+S+N)
        self._frame.columnconfigure(0, weight=1)
        self._frame.rowconfigure(0, weight=1)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = Frame(master=self._root)

        label_name = Label(master = self._frame, text = "Tic-tac-toe")
        label_player1 = Label(master = self._frame, text="Player 1 name: ")
        self._player1_entry  = Entry(master = self._frame)
        self._player1_entry.insert(END,self._game_grid.player1.name)
        
        label_player2 = Label(master = self._frame, text="Player 2 name: ")
        self._player2_entry  = Entry(master = self._frame)
        self._player2_entry.insert(END,self._game_grid.player2.name)


        grid_size_options = {
            3: "3 x 3",
            5: "5 x 5",
            7: "7 x 7",
        }
        self._selected_grid_size = StringVar()
        self._selected_grid_size.set( 
            grid_size_options[ self._game_grid.grid_size ]
        )
        drop = OptionMenu( self._frame , self._selected_grid_size , *grid_size_options )
        start_button = Button(
            master= self._frame,
            text= "Play",
            command= lambda: self._handle_grid_view(self._create_game_grid())
            )
        
        label_name.grid(row = 0, column=0, columnspan=2)
        label_player1.grid(row=1,column=0,sticky=N+S+E+W)
        self._player1_entry .grid(row=1,column=1,sticky=N+S+E+W)
        label_player2.grid(row=2,column=0,sticky=N+S+E+W)
        self._player2_entry .grid(row=2,column=1,sticky=N+S+E+W)
        drop.grid(row=3,column=0,sticky=N+S+E+W)
        start_button.grid(row=3,column=1,sticky=N+S+E+W)
        self._frame.columnconfigure(1, weight=1)

    def _create_game_grid(self):
        size = int(self._selected_grid_size.get()[0]) #first index is the grid size
        player1 = Player(self._player1_entry.get())
        player2 = Player(self._player2_entry.get())
        print(size, player1, player2)
        return GameGrid(size,player1,player2)