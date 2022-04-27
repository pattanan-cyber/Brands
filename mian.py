import tkinter as tk
import tkinter.ttk as ttk
import matplotlib

matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import pandas as pd


class App(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.df = pd.read_csv("data/GlobalBrands.csv")
        self.winfo_toplevel().title("Brands")
        self.create_widgets()


    def create_widgets(self):
        self.frame_filter = ttk.Label(self, text="Please select your filters")
        self.frame_filter.pack()




if __name__ == "__main__":
    root = tk.Tk()
    root.title("Matplotlib Integration")
    root.geometry("600x800")
    app = App(root)
    root.mainloop()