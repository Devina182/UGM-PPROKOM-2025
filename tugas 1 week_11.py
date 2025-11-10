import aritmatika

def input_bilangan():
    while True:
        try:
            a = float(input("Masukkan bilangan pertama: "))
            b = float(input("Masukkan bilangan kedua: "))
            return a, b
        except ValueError:
            print("Input tidak valid")

def tampilkan_hasil(operasi, hasil):
    print(f"Hasil {operasi}: {hasil}")

if __name__ == "__main__":
    print("===Kalkulator Aritmatika Modular===")

    a, b = input_bilangan()

    tampilkan_hasil("Penjumlahan", aritmatika.penjumlahan(a, b))
    tampilkan_hasil("Pengurangan", aritmatika.pengurangan(a, b))
    tampilkan_hasil("Perkalian", aritmatika.perkalian(a, b))
    tampilkan_hasil("Pembagian", aritmatika.pembagian(a, b))

    a_int = int(a) if a == int(a) else a
    b_int = int(b) if b == int(b) else b

    tampilkan_hasil("Pembagian Bulat", aritmatika.pembagian_bulat(a_int, b_int))
    tampilkan_hasil("Modulo (sisa bagi)", aritmatika.modulo(a_int, b_int))
    tampilkan_hasil("Pangkat", aritmatika.pangkat(a, b))