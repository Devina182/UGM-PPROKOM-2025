#Meminta user memasukkan 5 nama buah
buah = []
for i in range(5):
    nama = input(f"Masukkan nama buah ke-{i+1}: ")
    buah.append(nama)

#Menampilkan semua nama
print("\nDaftar buah:")
for i, nama in enumerate(buah):
    print(f"{i}, {nama}")

#Menanyakan indeks nama yang inghin diganti
indeks = int(input("n\Ingin mengganti nama pada indeks ke berapa? "))

#Meminta nama 
nama_baru = input("Masukkan nama pengganti: ")
buah[indeks] = nama_baru

#Menampilkan list baru
print("\nDaftar buah yang sudah diperbarui:")
for i, nama in enumerate(buah):
    print(f"{i}, {nama}")
