import tkinter as tk
from tkinter import ttk

class PlayerDialog:
    def __init__(self, parent):
        self.top = tk.Toplevel(parent)
        self.top.title("Choose Mode")
        self.top.geometry("300x100")
        self.result = None

        tk.Label(self.top, text="Select the number of players:").pack(pady=10)
        tk.Button(self.top, text="1 Player", command=self.one_player).pack(side=tk.LEFT, padx=20)
        tk.Button(self.top, text="2 Players", command=self.two_players).pack(side=tk.RIGHT, padx=20)

    def one_player(self):
        self.result = 1
        self.top.destroy()

    def two_players(self):
        self.result = 2
        self.top.destroy()

def show_player_dialog(root):
    dialog = PlayerDialog(root)
    root.wait_window(dialog.top)
    return dialog.result

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Main Application")

    def on_start():
        result = show_player_dialog(root)
        if result:
            print(f"Selected: {result}")

    tk.Button(root, text="Start Game", command=on_start).pack(pady=20)

    root.mainloop()
