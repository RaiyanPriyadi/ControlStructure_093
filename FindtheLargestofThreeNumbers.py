angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua: "))
angka3 = int(input("Masukkan angka ketiga: "))

if (angka1 > angka2) and (angka1 > angka3):
    terbesar = angka1
    print("Angka terbesar adalah:", terbesar)
elif (angka2 > angka1) and (angka2 > angka3):
    terbesar = angka2
    print("Angka terbesar adalah:", terbesar)
elif (angka3 > angka1) and (angka3 > angka2):
    terbesar = angka3
    print("Angka terbesar adalah:", terbesar)
else:
    print("tidak ada angka terbesar.")    

