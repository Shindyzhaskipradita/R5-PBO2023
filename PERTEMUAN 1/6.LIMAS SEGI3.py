print("SHINDYZP_220511004_TIF22E")
print()
print("6.MENCARI NILAI LIMAS SEGI3")
print()
print("#SOAL, DIKETAHUI")
print("SISI ALAS                        = 3")
print("TINGGI LIMAS                     = 30")
print("TINGGI LIMAS SEGI3               = 15")
#VARIABEL_LIMASSEGI3
ALAS = 3
TINGGI_LIMAS = 30
TINGGI_SEGITIGA = 15
#RUMUS_LIMASSEGI3
LUAS_PERMUKAAN= (ALAS * TINGGI_LIMAS) / 2 + 3 * (0.5 * ALAS * TINGGI_SEGITIGA)
VOLUME= (ALAS ** 2 * TINGGI_SEGITIGA) / 6
print()
print("#RUMUS")
print ("LUAS PERMUKAAN LIMAS SEGI TIGA   = (ALAS * TINGGI LIMAS) / 2 + 3 * (0.5 * ALAS * TINGGI SEGITIGA)")
print ("VOLUME                           = (ALAS ** 2 * TINGGI SEGITIGA) / 6")
print()
print("#HASIL") 
#OUTPUT
print("LUAS PERMUKAAN LIMAS SEGI TIGA   = ", LUAS_PERMUKAAN)
print("VOLUME LIMAS SEGI TIGA           = ", VOLUME)