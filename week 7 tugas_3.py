nilai_mahasiswa = {
    "Aba": 85,
    "Abi": 90,
    "Abu": 78
}
print(nilai_mahasiswa)

print("\nMenambah nilai Abe:")
nilai_mhasiswa.update({"Abe": 88})
print(nilai_mahasiswa)

print("\nmengupdate Nilai Abu:")
nilai_mahasiswa["Abu"] = 87
print(nilai_mahasiswa)

print("\nMencetak Semua Nilai:")
for nama, nilai in nilai_mahasiswa.items():
    print(f"Nilai {nama} adalah {nilai}")