import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("LB 5")
root.geometry("500x500")
root.iconbitmap(default = "fish.ico")

btn = ttk.Button(root, text = "Hello")
btn.place(relx = .5, rely = .5, anchor ='center')
root.mainloop()

root.mainloop()



