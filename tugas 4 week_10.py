# Nama:  [nama]
# NIM: [NIM]

import math
#Input Nama dan Nim pengguna
print("=== KALKULATOR ===")
nama = input("Masukkan nama Anda: ")
nim = input("Masukkan NIM anda: ")
    
# Fungsi-fungsi Operasi Matematika
def penjumlahan(A, B):
    return A + B
def pengurangan(A, B):
    return A - B
def perkalian(A, B):
    return A * B
def pembagian(A, B):
    return A / B
def perpangkatan(A, B):
    return A ** B
def akar_kuadrat(A, B):
    if A < 0:
        return "Error tidak dapat menghitung akar kuadrat dari bilangan negatif."
    return math.sqrt(A)

# Tampilan Menu
def tampilkan_menu():
    print("\n=========================")
    print("Kalkulator Matematika")
    print("\n=========================")
    print("Menu Utama")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Perpangkatan")
    print("6. Akar Kuadrat")
    print("---------------------------")
    
# Looping Program Kalkulator
while True: 
    tampilkan_menu()
    pilihan = input("Masukkan pilihan (1-7): ")
    if pilihan == '7':
        print("\nTerima kasih telah menggunakan kalkulator ini")
        break
    try:
        # pilihan 1-5
        if pilihan in ('1', '2', '3', '4', '5'):
            A = float(input("Masukkan bilangan pertama (A): "))
            B = float(input("Masukkan bilangan kedua(B): "))
            hasil = ""
            
            if pilihan == '1':
                hasil = penjumlahan(A, B)
                operasi = f"{A} + {B}"
            elif pilihan == '2':
                hasil = pengurangan(A, B)
                operasi = f"{A} - {B}"
            elif pilihan == '3':
                hasil = perkalian(A, B)
                operasi = f"{A} * {B}"
            elif pilihan == '4':
                hasil = pembagian(A, B)
                operasi = f"{A} / {B}"
            elif pilihan == '5':
                hasil = perpangkatan(A, B)
                operasi = f"{A} ** {B}"
            print(f"\nHasil dari {operasi} adalah: **{hasil}**")
            
        #pilihan 6
        elif pilihan == '6':
            A = float(input("Masukkan bilangan yang akan dicari akar kuadratnya (A): "))
            hasil = akar_kuadrat(A)
            print(f"\nAkar Kuadrat dari {A} adalah **{hasil}**")
            
        else:
            print("nPilihan tidak valid. Silahkan masukkan angka antara 1 sampai 7.")
    except valueError:
        print("\nInput tidak valid. Harap masukkan angka yang benar")
    except Exception as e:
        print(f"\nTerjadi kesalahan: {e}")
# Jalankan program
if __name__ == "__main__":
    kalkulator()
    


    