import tkinter as tk
from controller import run_droid

def start():
    run_droid()

root = tk.Tk()
root.title("Droid Assistant")
root.geometry("300x150")

btn = tk.Button(root, text="Start Listening", command=start)
btn_exit = tk.Button(root, text="Exit", command=root.quit)
#
btn.pack(pady=20)
btn_exit.pack(pady=20)

root.mainloop()
