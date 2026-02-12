#this is a test

import tkinter as tk

def Process_data():
    print("Click")


root = tk.Tk()
root.title("Basic Interface")
root.geometry("600x400")

lable = tk.Label(root, text="Frederic Biondi && Mr Baumgarten")
lable.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Process", command=Process_data)
button.pack()


root.mainloop()
