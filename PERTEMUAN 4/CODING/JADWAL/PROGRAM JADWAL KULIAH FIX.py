import tkinter as tk
from tkinter import ttk


def tambah_jadwal():
    mata_kuliah = entry_mata_kuliah.get()
    gedung = combo_gedung.get()
    hari = combo_hari.get()
    jam_mulai = entry_jam_mulai.get()
    jam_selesai = entry_jam_selesai.get()
    dosen = entry_dosen.get()

    # Menambahkan data ke dalam treeview
    tree.insert("", "end", values=(mata_kuliah, gedung, hari, jam_mulai, jam_selesai, dosen))

    # Mengosongkan input setelah menambahkan data
    entry_mata_kuliah.delete(0, "end")
    entry_jam_mulai.delete(0, "end")
    entry_jam_selesai.delete(0, "end")
    entry_dosen.delete(0, "end")

# Membuat window
window = tk.Tk()
window.title("Jadwal Kuliah")

# Membuat label dan entry untuk setiap kolom
label_mata_kuliah = tk.Label(window, text="Mata Kuliah:")
entry_mata_kuliah = tk.Entry(window)

# Membuat label dan entry untuk setiap kolom
label_Nama = tk.Label(window, text="Nama Shindy ZP_TIF22E_220511004")
entry_Nama = tk.Entry(window)

label_gedung = tk.Label(window, text="Gedung:")
gedung_options = ["Machdor", "Juanda"]
combo_gedung = ttk.Combobox(window, values=gedung_options)

label_hari = tk.Label(window, text="Hari:")
hari_options = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat"]
combo_hari = ttk.Combobox(window, values=hari_options)

label_jam_mulai = tk.Label(window, text="Jam Mulai:")
entry_jam_mulai = tk.Entry(window)

label_jam_selesai = tk.Label(window, text="Jam Selesai:")
entry_jam_selesai = tk.Entry(window)

label_dosen = tk.Label(window, text="Dosen:")
entry_dosen = tk.Entry(window)

# Membuat tombol untuk menambahkan jadwal
tombol_tambah = tk.Button(window, text="Tambah Jadwal", command=tambah_jadwal)

# Membuat Treeview untuk menampilkan jadwal
columns = ("Mata Kuliah", "Gedung", "Hari", "Jam Mulai", "Jam Selesai", "Dosen")
tree = ttk.Treeview(window, columns=columns, show="headings")

# Menambahkan heading untuk setiap kolom
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=150)

# Menempatkan elemen-elemen pada grid
label_mata_kuliah.grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_mata_kuliah.grid(row=0, column=1, padx=10, pady=5, sticky="w")
label_gedung.grid(row=1, column=0, padx=10, pady=5, sticky="w")
combo_gedung.grid(row=1, column=1, padx=10, pady=5, sticky="w")
label_hari.grid(row=2, column=0, padx=10, pady=5, sticky="w")
combo_hari.grid(row=2, column=1, padx=10, pady=5,sticky="w")
label_jam_mulai.grid(row=3, column=0, padx=10, pady=5,sticky="w")
entry_jam_mulai.grid(row=3, column=1, padx=10, pady=5, sticky="w")
label_jam_selesai.grid(row=4, column=0, padx=10, pady=5, sticky="w")
entry_jam_selesai.grid(row=4, column=1, padx=10, pady=5, sticky="w")
label_dosen.grid(row=5, column=0, padx=10, pady=5, sticky="w")
entry_dosen.grid(row=5, column=1, padx=10, pady=5, sticky="w")
tombol_tambah.grid(row=6, column=0, columnspan=2, pady=10 )
tree.grid(row=7, column=0, columnspan=2, padx=10, pady=5, sticky="w")

# Menjalankan main loop
window.mainloop()