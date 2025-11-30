import tkinter as tk
from tkinter import ttk


class TabbedApp:
    def __init__(self, window):
        self.root = window
        self.note = ttk.Notebook(self.root)
        self.setup_ui()
        self.center_window()

    def center_window(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')

    def setup_ui(self):
        self.root.title("LB 5")
        self.root.geometry("800x500")

        self.note.pack(expand=True, fill="both")

        self.create_tab1()
        self.create_tab2()

    def create_tab1(self):
        frame1 = tk.Frame(self.note)
        frame1.pack(expand=True, fill="both")

        label1 = ttk.Label(
            frame1,
            text=(
                "Разработка GUI на Python с Tkinter позволяет быстро создавать "
                "кроссплатформенные десктопные приложения"
            ),
            background="red"
        )
        label1.pack(padx=10, pady=10)

        self.note.add(frame1, text="Tab 1")

    def create_tab2(self):
        frame2 = tk.Frame(self.note)
        frame2.pack(expand=True, fill="both")

        label2 = ttk.Label(
            frame2,
            text=(
                "Эффективный GUI на Python требует не только правильного выбора "
                "фреймворка, но и грамотной организации кода"
            ),
            background="green"
        )
        label2.pack(padx=10, pady=10)

        self.note.add(frame2, text="Tab 2")


if __name__ == "__main__":
    root = tk.Tk()
    app = TabbedApp(root)
    root.mainloop()