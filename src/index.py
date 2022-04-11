from tkinter import Tk
from ui.ui import UI


def start():
    window = Tk()
    window.title('Tic-tac-toe')

    ui_view = UI(window)
    ui_view.start()

    window.mainloop()


if __name__ == '__main__':
    start()
