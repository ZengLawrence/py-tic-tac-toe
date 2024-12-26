"""Main module to start the game."""

import argparse
from console import Console

try:
    from gui import App
    GUI_AVAILABLE = True
except ImportError:
    GUI_AVAILABLE = False


def main():
    """Main function to start the game."""
    parser = argparse.ArgumentParser(description="Start the Tic Tac Toe game.")
    parser.add_argument('--gui', action='store_true', help="Run the game with a GUI")
    args = parser.parse_args()

    if args.gui:
        if not GUI_AVAILABLE:
            print("GUI is not available. Please ensure tkinter is installed.")
            return
        App().run()
    else:
        Console().start()

if __name__ == "__main__":
    main()
