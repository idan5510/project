import tkinter as tk

from prepare_data import prepare_data
from test import test_model
from train import train_model


def main_window():
    tk_root = tk.Tk()
    tk_root.geometry("220x170")
    tk_root.title('Project')
    tk_root.resizable(0, 0)

    tk_root.columnconfigure(0, weight=1)
    tk_root.rowconfigure(0, weight=1)
    tk_root.rowconfigure(1, weight=1)
    tk_root.rowconfigure(2, weight=1)

    train_btn = tk.Button(tk_root, text='prepare data', command=prepare_data)
    train_btn.grid(column=0, row=0)

    train_btn = tk.Button(tk_root, text='train model', command=train_model)
    train_btn.grid(column=0, row=1)

    train_btn = tk.Button(tk_root, text='test model', command=test_model)
    train_btn.grid(column=0, row=2)

    tk_root.mainloop()

