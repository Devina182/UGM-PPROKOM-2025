import konversi_suhu as s
import os

def input_angka(pesan):
        while True:
            try:
                return float(input(pesan))
            except ValueError:
                print("Input berupa angka\n")
while True:
    print("== Program Konversi Suhu ==")
    print("1. Celcius ke Fahrenheit dan Kelvin")
    print("2. Fahrenheit ke Celcius  dan Kelvin")
    print("3. Kelvin ke Celcius & Fahrenheit")
    print("4. keluar")

    menu = input("Pilih menu (1-4): ")

    if menu == "4":
        print(Terimakasih)
        break
    if menu not in ["1", "2", "3"]:
        print("\nPilihan tidak valid")
        input("Tekan ENTER untuk lanjut...")
        continue
    print()
    if menu == "1":
        c = input_angka("Masukkan suhu kedalam Celcius: ")
        print(f"{c}C = {s.c_to_f(c)}F ")
        print(f"{c}C = {s.c_to_k(c)}K ")

    elif menu == "2":
        f = input_angka("Masukkan suhu kedalam Fahrenheit: ")
        print(f"{f}F = {s.f_to_c(f)}C ")
        print(f"{f}F = {s.f_to_k(f)}K ")
    
    elif menu == "3":
        k = input_angka("Masukkan suhu kedalam Kelvin ")
        print(f"{k}K = {s.k_to_c(k)}C ")
        print(f"{k}K = {s.k_to_f(k)}F ")