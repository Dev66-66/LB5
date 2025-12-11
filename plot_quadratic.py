import tkinter as tk

import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np


class QuadraticPlotApp:

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("График y = x^2")
        self.root.geometry("700x500")

        self._build_plot()
        self._draw_plot()

    def _build_plot(self) -> None:
        self.figure = Figure(figsize=(6, 4), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.ax.set_title("y = x^2")
        self.ax.set_xlabel("x")
        self.ax.set_ylabel("y")
        self.ax.grid(True)

        canvas = FigureCanvasTkAgg(self.figure, master=self.root)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        self.canvas = canvas

    def _draw_plot(self) -> None:
        x = np.linspace(-10, 10, 400)
        y = x ** 2

        self.ax.clear()
        self.ax.plot(x, y, label="y = x^2")
        self.ax.set_title("y = x^2")
        self.ax.set_xlabel("x")
        self.ax.set_ylabel("y")
        self.ax.grid(True)
        self.ax.legend()

        self.canvas.draw()


if __name__ == "__main__":
    matplotlib.use("TkAgg")
    root = tk.Tk()
    QuadraticPlotApp(root)
    root.mainloop()

