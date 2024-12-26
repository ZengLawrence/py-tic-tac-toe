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

class App:
    """Class for GUI app"""
    def __init__(self, master):
        self.root = master
        self.root.title("Tic Tac Too")
        self.frm = ttk.Frame(self.root, padding=10)
        self.frm.grid()
        ttk.Label(self.frm, text="Click on a box").grid()
        self.board_frame = ttk.Frame(self.frm)
        self.board_frame.grid()
        self.game = Game()
        self.board = init_board(self.board_frame, self.game)
        self.game.register(lambda game: refresh_board(self.board, game.state))
        ttk.Button(self.frm, text="Quit", command=self.root.destroy).grid()

    def run(self):
        """Run the app"""
        self.root.mainloop()

if __name__ == "__main__":
    root = Tk()
    app = App(root)
    app.run()
