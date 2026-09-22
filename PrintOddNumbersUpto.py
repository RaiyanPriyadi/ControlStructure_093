n = int(input("Masukkan nilai batas maksimum (n): "))

print(f"Bilangan ganjil hingga {n}:")
# range(mulai, berhenti, langkah)
for i in range(1, n + 1, 2):
    print(i, end=" ")
print()