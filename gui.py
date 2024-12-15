"""Module for GUI app"""

from tkinter import Tk
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
board = [ttk.Button(frm, text=" ").grid(column=i, row=j) for i in range(3) for j in range(3)]
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=4)
root.mainloop()
