#!/usr/bin/env python3 Bullshit GUI Example

import tkinter as tk

def process_data(event=None):
    # 1. Grab the text from the entry box
    user_text = entry.get()

    # 2. Change the label to show what was typed
    label.config(text=f"Hello, {user_text}!")

    # 3. Still print to the console for a heartbeat check
    print(f"Processed: {user_text}")

    # 4. Clear the box
    entry.delete(0, tk.END)


root = tk.Tk()
root.title("Basic Interface")
root.geometry("600x400")

label = tk.Label(root, text="Type a Label in the text box!")
label.pack()

entry = tk.Entry(root)
entry.pack()

# Bind Enter to the Entry widget itself
entry.bind('<Return>', process_data)

button = tk.Button(root, text="Process", command=process_data)
button.pack()

root.mainloop()
