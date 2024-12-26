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
    _board_frame = ttk.Frame(frame)
    _board = [[init_button(_board_frame, btn_text, game, row=i, col=j)
            for (j, btn_text) in enumerate(row)]
            for (i, row) in enumerate(game.state)]
    return (_board, _board_frame)

def refresh_board(board, game):
    """Refresh board with game state"""
    enable = game.result is None
    for (i, row) in enumerate(game.state):
        for (j, btn_text) in enumerate(row):
            btn = board[i][j]
            btn["text"] = btn_text
            btn["state"] = "disabled" if not enable else "normal"

def init_status(frame, game):
    """Initialize status label"""
    return ttk.Label(frame, text=status_text(game))

def refresh_status(status, game):
    """Refresh status with game result"""
    status["text"] = status_text(game)

def status_text(game):
    """Return status text"""
    return game.result if game.result else game.side + "'s turn. Click on a box"

class App:
    """Class for GUI app"""
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        _frm = ttk.Frame(self.root, padding=10)
        _frm.grid()
        game = Game()
        self.status = init_status(_frm, game)
        self.status.grid(sticky="w")
        self.board, _board_frame = init_board(_frm, game)
        _board_frame.grid()
        game.register(self.refresh)
        ttk.Button(_frm, text="Quit", command=self.root.destroy).grid()

    def run(self):
        """Run the app"""
        self.root.mainloop()

    def refresh(self, game):
        """Refresh the app"""
        refresh_status(self.status, game)
        refresh_board(self.board, game)
        self.root.update()

if __name__ == "__main__":
    _root = Tk()
    App(_root).run()
