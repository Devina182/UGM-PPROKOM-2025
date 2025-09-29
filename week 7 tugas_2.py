stok_buku = {
    "Harry Potter": 10,
    "Laskar Pelangi": 15,
    "Bumi Manusia": 7,
    "Dilan 1990": 20
}
print("Daftar stok buku:")
for judul, stok in  stok_buku.items():
    print("buku: {judul} - stok: {stok}")

judul_baru = input("\nMasukkan judul buku baru: ")
stok_baru = int(input("Masukkan jumlah stok awal: "))
stok_buku[judul_baru] = stok_baru

print(f"Buku {judul_baru} berhasil ditambahkan dengan stok {stok_baru}")
print("Dictionary terbaru:", stok_buku)