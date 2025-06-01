import tkinter as tk
from controller import run_droid

def start():
    run_droid()

root = tk.Tk()
root.title("Droid Assistant")
root.geometry("300x150")

btn = tk.Button(root, text="Start Listening", command=start)
btn.pack(pady=50)

root.mainloop()
