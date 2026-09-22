n = int(input("Masukkan nilai batas maksimum (n) untuk deret Fibonacci: "))

# Inisialisasi dua angka pertama dari deret
a, b = 0, 1

print(f"Deret Fibonacci hingga {n}:")
while a <= n:
    print(a, end=" ")
    # Perbarui nilai: 'a' menjadi 'b', dan 'b' menjadi hasil penjumlahan keduanya
    a, b = b, a + b
print() # Untuk membuat baris baru di akhir