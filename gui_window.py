#!/usr/bin/env python3

import tkinter as tk

def Process_data():
    print("Click")


root = tk.Tk()
root.title("Basic Interface")
root.geometry("600x400")

lablel = tk.Label(root, text="Frederic Biondi && Mr Baumgarten")
lablel.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Process", command=Process_data)
button.pack()

root.mainloop()

