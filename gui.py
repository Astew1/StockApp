import numpy as np
import tkinter as tk
import matplotlib as mp
import api as api

# class Window(tk.Frame):
#
#     def __init__(self, master=None):
#         tk.Frame.__init__(self, master)
#         self.master = master
#         self.master.title("StockTracker")
#
#
#     def showText(self, data):
#         txt = tk.Label(self, text=str(data))
#         txt.pack()
def setLabelText(root, label = None, txt = ""):
    txt = str(txt)
    if (label == None):
        label = tk.Label(root, text = txt)
    else:
        label.set(txt)
    label.pack()
    return label
