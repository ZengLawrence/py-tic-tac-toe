"""Main module to start the game."""

import argparse
from console import Console

try:
    from tkinter import Tk
    from gui import App
    GUI_AVAILABLE = True
except ImportError:
    GUI_AVAILABLE = False


def main():
    """Main function to start the game."""
    desc = "Tic Tac Toe game. By default, runs in console mode."
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--gui', action='store_true', help="Start the game with GUI")
    args = parser.parse_args()

    if args.gui:
        if not GUI_AVAILABLE:
            print("GUI is not available. Please ensure tkinter is installed.")
            return
        App(Tk()).run()
    else:
        Console().start()

if __name__ == "__main__":
    main()
