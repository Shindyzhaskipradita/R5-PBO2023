import tkinter as tk
from tkinter import Menu


from bola import *
from balok import *
from kerucut import *
from kubus import *
from limas_segiempat import*
from limas_segitiga import*
from prisma_segitiga import*
from tabung import*

# root window
root = tk.Tk()
root.title('Menu Demo')
#root.attributes('-fullscreen', True)
root.geometry("900x400")
# create a menubar
menubar = Menu(root)
root.config(menu=menubar)

# create a menu
file_menu = Menu(menubar)
app_menu = Menu(menubar)
data_menu = Menu(menubar)

# add a menu item to the menu
file_menu.add_command(
    label='File Open', command=root.destroy
)

file_menu.add_command(
    label='Exit', command=root.destroy
)

app_menu.add_command(
    label='App Balok', command= lambda: new_window("Luas dan Volume balok", balok)
)
app_menu.add_command(
    label='App Bola', command= lambda: new_window("Luas dan Volume bola", bola)
)
app_menu.add_command(
    label='App Kerucut', command= lambda: new_window("Luas dan Volume kerucut", Kerucut)
)
app_menu.add_command(
    label='App Kubus', command= lambda: new_window("Luas dan Volume kubus", kubus)
)
app_menu.add_command(
    label='App Limas segiempat', command= lambda: new_window("Luas dan Volume Limas segiempat", limas_segiempat)
)
app_menu.add_command(
    label='App limas segitiga', command= lambda: new_window("Luas dan Volume", limas_segitiga)
)
app_menu.add_command(
    label='App Prisma', command= lambda: new_window("Luas dan Volume Prisma", prisma_segitiga)
)
app_menu.add_command(
    label='App Tabung', command= lambda: new_window("Luas dan Volume Tabung", Tabung)
)
def new_window( number, _class):
    new = tk.Toplevel()
    new.transient()
    new.grab_set()
    _class(new, number)

# add the File menu to the menubar
menubar.add_cascade(
    label="File", menu=file_menu
)
menubar.add_cascade(
    label="App", menu=app_menu
)
    
root.mainloop()