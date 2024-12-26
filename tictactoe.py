"""Main module to start the game."""

import argparse
import tkinter as tk
from console import Console
from gui import App

def main():
    parser = argparse.ArgumentParser(description="Start the Tic Tac Toe game.")
    parser.add_argument('--gui', action='store_true', help="Run the game with a GUI")
    args = parser.parse_args()

    if args.gui:
        root = tk.Tk()
        app = App(root)
        root.mainloop()
    else:
        Console().start()

if __name__ == "__main__":
    main()
