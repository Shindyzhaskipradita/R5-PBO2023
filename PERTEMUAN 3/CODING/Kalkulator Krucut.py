import tkinter as tk
from tkinter import Frame, Label, Entry, Button, END, W
import math

def hitung_luas():
    jari_jari = float(txtjari_jari.get())
    tinggi = float(txttinggi.get())

    luas = math.pi * jari_jari * (jari_jari + math.sqrt(jari_jari * 2 +tinggi * 2))

    txtLuas.delete(0, END)
    txtLuas.insert(END,luas)

def hitung_volume():
    jari_jari = float(txtjari_jari.get())

    Volume = 4/3 * math.pi * jari_jari


    txtVolume.delete(0,END)
    txtVolume.insert(END, Volume)

def hitung():
    hitung_luas()
    hitung_volume()

app = tk . Tk()
app.title ("Kalkulator Mencari Luas dan Volume kerucut")

frame = Frame (app)
frame.pack(padx=20, pady=20)

#panjang
jari_jari = Label (frame, text="Jari-jari:")
jari_jari.grid(row=0, column=0, sticky=W, padx=5, pady=5)

tinggi = Label(frame, text="Tinggi:")
tinggi.grid(row=1, column=0,sticky=W, padx=5, pady=5)


#textbox panjang
txtjari_jari = Entry(frame)
txtjari_jari.grid(row=0, column=1,  sticky=W, padx=5, pady=5)
#textbox tinggi
txttinggi= Entry(frame)
txttinggi.grid(row=1, column=1, sticky=W, padx=5, pady=5)

# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=2, column=0, sticky=W, padx=5, pady=5)

# Output Label Luas
luas= Label(frame, text="Luas: ")
luas.grid(row=3, column=0, sticky=W, padx=5, pady=5)


volume = Label (frame, text="Volume: ")
volume.grid(row=4, column=0, stick=W, padx=5, pady=5)

# Output Textbox Luas
txtLuas = Entry(frame)
txtLuas.grid(row=3, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Keliling
txtVolume = Entry (frame)
txtVolume.grid(row=4, column=1, sticky=W, padx=5, pady=5)

app.mainloop()