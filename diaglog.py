import tkinter as tk

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

class SideDialog:
    def __init__(self, parent):
        self.top = tk.Toplevel(parent)
        self.top.title("Choose side")
        self.top.geometry("300x100")
        self.result = None

        tk.Label(self.top, text="Select your side:").pack(pady=10)
        tk.Button(self.top, text="X", command=self.choose_x).pack(side=tk.LEFT, padx=20)
        tk.Button(self.top, text="O", command=self.choose_o).pack(side=tk.RIGHT, padx=20)

    def choose_x(self):
        self.result = 'x'
        self.top.destroy()

    def choose_o(self):
        self.result = 'o'
        self.top.destroy()

def show_side_dialog(root):   
    dialog = SideDialog(root)
    root.wait_window(dialog.top)
    return dialog.result

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Main Application")

    def on_start():
        result = show_player_dialog(root)
        if result:
            print(f"Selected: {result}")
            side = show_side_dialog(root)
            if side:
                print(f"Selected: {side}")

    tk.Button(root, text="Start Game", command=on_start).pack(pady=20)

    root.mainloop()
