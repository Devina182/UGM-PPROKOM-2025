#slicing
A = [
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [7, 8, 9],
        [10, 11, 12]
    ]
]
print(A[0][:])

#elemen kolom terakhir
A = [
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [7, 8, 9],
        [10, 11, 12]
    ]
]
print("Elemen kolom terakhir dari setiap baris dan lapisan:")
for lapisan in range(len(A)):
    for baris in range(len(A[lapisan])):
        nilai = A[lapisan][baris][-1]
        print(f"Lapisan {lapisan}, Baris {baris} -> {nilai}")