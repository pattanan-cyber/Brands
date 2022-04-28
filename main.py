from models.modelbrand_ads import Brand, Ads
from package.brand_ads import Brands
from tkinter import ttk
from tkinter import *

db = Brands()
def show_all():
    for item in db.brand().all_brands():
        lis.insert(END, item)

root = Tk()
root.title("Brands")

lis = Listbox(root, width=500, height=500)
all_songs = Button(root, text="Show all",
                   command=show_all).pack(side=BOTTOM)
lis.pack()


root.mainloop()