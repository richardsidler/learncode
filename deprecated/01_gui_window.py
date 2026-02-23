#!/usr/bin/env python3

import tkinter as tk

def Process_data():
    # 1. Grab the text from the entry box
    user_text = entry.get() 
    
    # 2. Change the label to show what was typed
    lablel.config(text=f"Hello, {user_text}!")
    
    # 3. Still print to the console for a heartbeat check
    print(f"Processed: {user_text}")

root = tk.Tk()
root.title("Basic Interface")
root.geometry("600x400")

lablel = tk.Label(root, text="Type a Label in the text box!")
lablel.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Process", command=Process_data)
button.pack()

root.mainloop()