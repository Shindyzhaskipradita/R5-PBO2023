import tkinter as tk 
from tkinter import Frame, Label, Entry, Button, END, W
import math

def hitung_luas():
    Jari_jari = float(txtJari_jari.get())
    
    Luas = 4*math.pi*Jari_jari

    txtLuas.delete(0, END)
    txtLuas.insert(END,Luas)

def hitung_volume():
    Jari_jari = float(txtJari_jari.get())


    Volume = (4/3) * math.pi * (Jari_jari ** 3)

    txtVolume.delete(0,END)
    txtVolume.insert(END,Volume)

def hitung():
    hitung_luas()
    hitung_volume()
# Create tkinter object app = tk.Tk()
app = tk.Tk()

# Tambahkan judul
app.title("Kalkulator Luas dan Keliling Bola")

# Windows
frame = Frame(app) 
frame.pack(padx=20, pady=20)

# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Label Jari-jari
Jari_jari = Label(frame, text="Jari-jari:") 
Jari_jari.grid(row=0, column=0, sticky=W, padx=5, pady=5)

#label volume
Volume= Label(frame, text="Volume:")
Volume.grid(row=5, column=0, sticky=W, padx=5, pady=5)

#label Luas
Luas= Label(frame, text="Luas:")
Luas.grid(row=4, column=0, sticky=W, padx=5, pady=5)


# Output Textbox Luas
txtJari_jari = Entry(frame)
txtJari_jari.grid(row=0, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Luas
txtLuas = Entry(frame)
txtLuas.grid(row=4, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Keliling
txtVolume = Entry (frame)
txtVolume.grid(row=5, column=1, sticky=W, padx=5, pady=5)

app.mainloop()