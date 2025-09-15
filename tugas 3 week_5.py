nilai = int(input("Masukkan jumlahn nilai?: "))
total = 0

for i in range(nilai):
    nilai = float(input(f"Masukkan nilai ke-{i+1}: "))
    total += nilai

    rata_rata = total / nilai
    print(f"Rata-rata dan {nilai} nilai adalah: {rata_rata:.2f}")