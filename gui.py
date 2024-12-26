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

def init_status(frame):
    """Initialize status label"""
    return ttk.Label(frame, text="Click on a box")

def refresh_status(status, game):
    """Refresh status with game result"""
    status["text"] = game.result if game.result else "Click on a box"

class App:
    """Class for GUI app"""
    def __init__(self, master):
        self.root = master
        self.root.title("Tic Tac Too")
        self.frm = ttk.Frame(self.root, padding=10)
        self.frm.grid()
        self.status = init_status(self.frm)
        self.status.grid()
        self.board_frame = ttk.Frame(self.frm)
        self.board_frame.grid()
        game = Game()
        self.board = init_board(self.board_frame, game)
        game.register(self.__refresh)
        ttk.Button(self.frm, text="Quit", command=self.root.destroy).grid()

    def run(self):
        """Run the app"""
        self.root.mainloop()
    
    def __refresh(self, game):
        """Refresh the app"""
        refresh_status(self.status, game)
        refresh_board(self.board, game.state)
        self.root.update()

if __name__ == "__main__":
    root = Tk()
    app = App(root)
    app.run()
