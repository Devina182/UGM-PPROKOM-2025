from array import array
nilai = array('i', [20, 40, 60, 80, 100])

print("Isi array:", nilai)
print("Jumlah elemen dalam array:", len(nilai))

#Menghitung jumlah total
total = sum(nilai)
print("Jumlah total elemen array:", total)

#Menghitung nilai rata-rata
rata_rata = total/len(nilai)
print("Nilai rata-rata elemen array:", rata_rata)
