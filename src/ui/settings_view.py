from tkinter import *

from entities.GameGrid import *

class SettingsView:
    def __init__(self, root, show_grid_view):
        self._show_grid_view = show_grid_view
        self._root = root
        self._frame = None
        self._player1_name = None
        self._player2_name = None
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
        entry_player1 = Entry(master = self._frame)
        
        label_player2 = Label(master = self._frame, text="Player 2 name: ")
        entry_player2 = Entry(master = self._frame)


        grid_size_options = [
            "3 x 3",
            "5 x 5",
            "7 x 7",
        ]
        selected_grid_size = StringVar()
        selected_grid_size.set( grid_size_options[0])
        drop = OptionMenu( self._frame , selected_grid_size , *grid_size_options )
        grid = GameGrid(3,Player("kaaleppi"),Player("Uolevi"))
        start_button = Button(master= self._frame, text= "Play", command=self._show_grid_view(grid))
        
        label_name.grid(row = 0, column=0, columnspan=2)
        label_player1.grid(row=1,column=0,sticky=N+S+E+W)
        entry_player1.grid(row=1,column=1,sticky=N+S+E+W)
        label_player2.grid(row=2,column=0,sticky=N+S+E+W)
        entry_player2.grid(row=2,column=1,sticky=N+S+E+W)
        drop.grid(row=3,column=0,sticky=N+S+E+W)
        start_button.grid(row=3,column=1,sticky=N+S+E+W)
        self._frame.columnconfigure(1, weight=1)