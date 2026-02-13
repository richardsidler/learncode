import tkinter as tk

# 1. Setup the main window (The root)
root = tk.Tk()
root.title("VS Code Workflow Demo")
root.geometry("400x200")

# 2. Add a Label (The "output")
label = tk.Label(root, text="Waiting for interaction...", font=("Arial", 12))
label.pack(pady=20)

# 3. Define a function (The "logic")
def on_button_click():
    label.config(text="Signal Received! Logic is working.")
    print("Button was pressed in the GUI.")

# 4. Add a Button (The "input")
button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack(pady=10)

# 5. Start the engine (The event loop)
root.mainloop()