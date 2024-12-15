"""Module for GUI app"""

from tkinter import Tk
from tkinter import ttk
from game import Game

def init_button(frame, text, col, row):
    """Initialize button in board"""
    def update_text():
        btn["text"] = "clicked!"
    btn = ttk.Button(frame, text=text, command=update_text)
    btn.grid(column=col, row=row)
    return btn

def init_board(frame, game):
    """Initialize board with game state"""
    return [init_button(frame, btn_text, col=i, row=j)
            for (j, row) in enumerate(game.state)
            for (i, btn_text) in enumerate(row)]

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
board = init_board(frm, Game())
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=4)
root.mainloop()
