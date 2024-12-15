"""Module for GUI app"""

from tkinter import Tk
from tkinter import ttk

def init_button(frame, col, row):
    """Initialize button in board"""
    btn = ttk.Button(frame, text=" ")
    btn.grid(column=col, row=row)
    return btn

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
board = [init_button(frm, col=i, row=j) for i in range(3) for j in range(3)]
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=4)
root.mainloop()
