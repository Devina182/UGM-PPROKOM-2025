#Menyimpan nama siswa lulus dan tidak lulus
lulus = ""
tidak_lulus = ""

#Input dan pemeriksaan siswa 1
nama1 = input("Masukkan nama siswa 1: ")
nilai1 = int(input("Masukkan nilai siswa 1: "))
if nilai1 >= 70:
    lulus += nama1 + "\n"
else:
    tidak_lulus += nama1 + "\n"

#Input dan pemeriksaan siswa 2
nama2 = input("Masukkan nama siswa 2: ")
nilai2 = int(input("Masukkan nilai siswa 2: "))
if nilai2 >= 70:
    lulus += nama2 + "\n"
else:
    tidak_lulus += nama2 + "\n"

#Input dan pemeriksaan siswa 3
nama3 = input("Masukkan nama siswa 3: ")
nilai3 = int(input("Masukkan nilai siswa 3: "))
if nilai3 >= 70:
    lulus += nama3 + "\n"
else:
    tidak_lulus += nama3 + "\n"

#Input dan pemeriksaan siswa 4
nama4 = input("Masukkan nama siswa 4: ")
nilai4 = int(input("Masukkan nilai siswa 4: "))
if nilai4 >= 70:
    lulus += nama4 + "\n"
else:
    tidak_lulus += nama4 + "\n"

#Input dan pemeriksaan siswa 5
nama5 = input("Masukkan nama siswa 5: ")
nilai5 = int(input("Masukkan nilai siswa 5: "))
if nilai5 >= 70:
    lulus += nama5 + "\n"
else:
    tidak_lulus += nama5 + "\n"

print("\n=== Daftar Siswa Lulus ===")
print(lulus)
print("=== Daftar Siswa Tidak Lulus ===")
print(tidak_lulus)