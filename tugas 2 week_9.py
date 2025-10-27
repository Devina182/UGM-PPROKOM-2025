n = int(input("Masukkan ukuran matriks identitas: "))
matriks = [[1 if i == j else 0 for j in range(n)]
           for i in range(n)]

print(f"\nMatriks identitas {n}x{n}:")
for baris in matriks:
    for elemen in baris:
        print(elemen, end="")
    print()