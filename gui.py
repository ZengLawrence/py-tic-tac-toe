"""Module for GUI app"""

from tkinter import Tk
from tkinter import ttk
from game import Game

def init_button(frame, text, game, col, row):
    """Initialize button in board"""
    def make_move():
        game.make((row+1, col+1))
    btn = ttk.Button(frame, text=text, command=make_move)
    btn.grid(column=col, row=row)
    return btn

def init_board(frame, game):
    """Initialize board with game state"""
    return [[init_button(frame, btn_text, game, row=i, col=j)
            for (j, btn_text) in enumerate(row)]
            for (i, row) in enumerate(game.state)]

def refresh_board(board, state):
    """Refresh board with game state"""
    for (i, row) in enumerate(state):
        for (j, btn_text) in enumerate(row):
            btn = board[i][j]
            btn["text"] = btn_text

root = Tk()
root.title("Tic Tac Too")
frm = ttk.Frame(root, padding=10)
frm.grid()
game = Game()
board = init_board(frm, game)
game.register(lambda game: refresh_board(board, game.state))
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=4)
root.mainloop()
