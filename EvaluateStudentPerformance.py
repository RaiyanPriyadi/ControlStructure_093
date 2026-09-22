persentase = float(input("Masukkan persentase siswa: "))

if persentase >= 90:
    print("Excellent performance (Kinerja Sangat Baik)")
elif persentase >= 80:
    print("Very Good performance (Kinerja Sangat Bagus)")
elif persentase >= 70:
    print("Good performance (Kinerja Baik)")
elif persentase >= 60:
    print("Average performance (Kinerja Rata-rata)")
else:
    print("Kinerja di bawah rata-rata")