"""Main module to start the game."""

import argparse
import console
from gui import App

def main():
    """Main function to start the game."""
    desc = "Tic Tac Toe game. By default, runs in console mode."
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--gui', action='store_true', help="Start the game with GUI")
    args = parser.parse_args()

    if args.gui:
        App().run()
    else:
        console.run()

if __name__ == "__main__":
    main()
