from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=20)
frm.grid()
ttk.Label(frm, text="Shop Management System").grid(column=0, row=0)
ttk.Label(frm, text="Tkinter Test").grid(column=0, row=1)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=2)
root.mainloop()