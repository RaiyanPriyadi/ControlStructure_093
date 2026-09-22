n = int(input("Masukkan nilai n: "))

# Loop luar untuk mengatur baris
for i in range(1, n + 1):
    # Loop dalam untuk mengatur berapa kali angka dicetak per baris
    for j in range(i):
        print(i, end=" ")
    # Pindah ke baris baru setelah setiap baris selesai
    print()