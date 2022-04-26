from tkinter import *

from entities.game_grid import GameGrid


class HighscoresView:
    def __init__(self, root, show_grid_view, show_settings_view, game_grid: GameGrid):
        self._root = root
        self._show_grid_view = show_grid_view
        self._game_grid = game_grid
        self._game_grid.empty_grid()
        self._show_settings_view = show_settings_view
        self._frame = None
        self._initialize()

    def pack(self):
        self._frame.grid(row=0, column=0, sticky=E+W+S+N, padx=10, pady=10)
        self._frame.columnconfigure(0, weight=1)
        self._frame.rowconfigure(0, weight=1)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = Frame(master=self._root)

        title_label = Label(
            master=self._frame,
            text=f"{self._game_grid.grid_size_as_text()} Highscores"
        )
        play_again_button = Button(
            master=self._frame,
            text="Play again",
            command=lambda: self._show_grid_view(self._game_grid)
        )
        settings_button = Button(
            master=self._frame,
            text="Settings",
            command=lambda: self._show_settings_view(self._game_grid)
        )

        highscore_frame = Frame(master=self._frame)
        highscore_frame.columnconfigure(
            tuple(range(3)),
            weight=1
        )
        highscore_frame.rowconfigure(0, weight=1)

        highscores = self._game_grid.get_highscores()
        for i, header, in enumerate(["place:", "name:", "points:"]):
            head_label = Label(
                master=highscore_frame,
                text=header
            )
            head_label.grid(row=0, column=i, sticky=W)
        print(highscores)

        placement_text = {
            1: "1st", 2: "2nd", 3: "3th", 4: "4th", 5: "5th"
        }
        for i, (name, wins) in enumerate(highscores, 1):
            place = Label(
                master=highscore_frame,
                text=placement_text[i]
            )
            name = Label(
                master=highscore_frame,
                text=name
            )
            win_count = Label(
                master=highscore_frame,
                text=wins
            )
            place.grid(row=i, column=0, sticky=W)
            name.grid(row=i, column=1, sticky=W)
            win_count.grid(row=i, column=2, sticky=E)

        title_label.grid(row=0, column=0, columnspan=2, sticky=N+S+E+W)
        highscore_frame.grid(row=1, columnspan=2,
                             sticky=N+S+E+W, padx=10, pady=10)
        play_again_button.grid(row=2, column=0, sticky=N+S+E+W)
        settings_button.grid(row=2, column=1, sticky=N+S+E+W)
