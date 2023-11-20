import tkinter as tk
from tkinter import Frame, Label, Entry, Button, END, W

def hitung_luas():
    luas_alas = float(txtluas_alas.get())
    luas_sisi = float(txtluas_sisi.get())
    
    luas = luas_alas + luas_sisi
    txtLuas.delete(0, END)
    txtLuas.insert(END,luas)

def hitung_volume():
    luas_alas = float(txtluas_alas.get())
    tinggi  = float (txttinggi.get())

    Volume = 1/3 * luas_alas * tinggi
    txtVolume.delete(0,END)
    txtVolume.insert(END, Volume)

def hitung():
    hitung_luas()
    hitung_volume()

app = tk.Tk()

app.title ("Kalkulator Limas Segi Empat")

frame = Frame (app)
frame.pack(padx=20, pady=20)

#La
luas_alas =Label(frame, text="Luas Alas :")
luas_alas.grid(row=0, column=0, sticky=W, padx=5, pady=5)
#ls
luas_sisi = Label(frame, text="Luas Sisi :")
luas_sisi.grid(row=1, column=0,sticky=W, padx=5, pady=5)
#t
tinggi = Label(frame, text="Tinggi :")
tinggi.grid(row=2, column=0,sticky=W, padx=5, pady=5)


#textbox LA
txtluas_alas = Entry(frame)
txtluas_alas.grid(row=0, column=1,  sticky=W, padx=5, pady=5)

#textbox LS
txtluas_sisi = Entry(frame)
txtluas_sisi.grid(row=1, column=1, sticky=W, padx=5, pady=5)
#textbox tinggi
txttinggi= Entry(frame)
txttinggi.grid(row=2, column=1, sticky=W, padx=5, pady=5)

# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Output Label Luas
luas= Label(frame, text="Luas: ")
luas.grid(row=4, column=0, sticky=W, padx=5, pady=5)

# output label volume
volume = Label (frame, text="Volume: ")
volume.grid(row=5, column=0, stick=W, padx=5, pady=5)

# Output Textbox Luas
txtLuas = Entry(frame)
txtLuas.grid(row=4, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Keliling
txtVolume = Entry (frame)
txtVolume.grid(row=5, column=1, sticky=W, padx=5, pady=5)

app.mainloop()