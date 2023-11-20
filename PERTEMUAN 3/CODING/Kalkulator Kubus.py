import tkinter as tk 
from tkinter import Frame, Label, Entry, Button, END, W

def hitung_luas():
    RK = float(txtRusuk.get())

    L = 4*RK 

    txtLuas.delete(0, END)
    txtLuas.insert(END,L)

def hitung_keliling():
    RK = float(txtRusuk.get())

    V = RK**3

    txtKeliling.delete(0,END)
    txtKeliling.insert(END,V)

def hitung():
    hitung_luas()
    hitung_keliling()

# Create tkinter object app = tk.Tk()
app = tk.Tk()

# Tambahkan judul
app.title("Kalkulator Luas dan Volume Kubus")

# Windows
frame = Frame(app) 
frame.pack(padx=20, pady=20)

# Label Panjang
Rusuk = Label(frame, text="Rusuk:") 
Rusuk.grid(row=0, column=0, sticky=W, padx=5, pady=5)

# Textbox Rusuk
txtRusuk = Entry(frame)
txtRusuk.grid(row=0, column=1)


# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=2, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas
Luas = Label(frame, text="Luas: ")
Luas.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Output label Keliling
volume = Label (frame, text="Volume: ")
volume.grid(row=4, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas
txtLuas = Entry(frame)
txtLuas.grid(row=3, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Keliling
txtKeliling = Entry (frame)
txtKeliling.grid(row=4, column=1, sticky=W, padx=5, pady=5)

app.mainloop()