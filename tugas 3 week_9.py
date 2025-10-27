import numpy as np
#penjumlahan dan pengurangan
A = np.array([[2, 4, 6], [1, 3, 5]])
B = np.array([[1, 1, 1], [2, 2, 2]])

penjumlahan = A + B
pengurangan = A - B
B_tranpose = B.T
perkalian = np.dot(A, B_tranpose)


print("Hasil penjumlahan  matriks: \n", penjumlahan)
print("\nHasil pengurangan matriks:\n", pengurangan)
print("\nHasil perkalian matriks: \n", perkalian)