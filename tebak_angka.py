import random

# Menghasilkan angka acak antara 1 dan 100
angka_rahasia = random.randint(1, 100)

# Menginisialisasi jumlah tebakan
jumlah_tebakan = 0

while True:
    # Minta pengguna untuk menebak angka
    tebakan = int(input("Tebak angka antara 1 dan 100: "))
    
    # Menambah jumlah tebakan
    jumlah_tebakan += 1
    
    # Memeriksa apakah tebakan benar
    if tebakan == angka_rahasia:
        print(f"Selamat! Anda menebak angka {angka_rahasia} dengan benar dalam {jumlah_tebakan} tebakan.")
        break
    elif tebakan < angka_rahasia:
        print("Tebakan terlalu rendah. Coba lagi.")
    else:
        print("Tebakan terlalu tinggi. Coba lagi.")
