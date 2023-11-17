print("=======================================")
print("Welcome To My Calculator Project :3")
print("-By Hideri")
print("=======================================")

while True:
    print("1. Kalkulator Biasa")
    print("2. Kalkulator Bangun Ruang")
    print("3. Kalkulator Bangun Datar")
    print("4. Konversi Satuan")
    print('5. Keluar')

    pilihan = input("Masukkan Pilihan Anda =")

    if pilihan == '5':
        print("Terima Kasih Telah Menggunakan Kalkulator Saya :)")
        break  # Keluar dari program jika pilihan adalah '5'

    # Kalkulator Biasa
    if pilihan == '1':
        print("Anda Memilih Pilihan Yaitu Kalkulator Biasa/Normal :>")
        # Tambahkan kode kalkulator biasa di sini

    # Kalkulator Bangun Ruang
    elif pilihan == '2':
        print("Anda Memilih Kalkulator Bangun Ruang :3")
        # Tambahkan kode kalkulator bangun ruang di sini

    # Kalkulator Bangun Datar
    elif pilihan == '3':
        print("Anda Memilih Kalkulator Bangun Datar <3")
        # Tambahkan kode kalkulator bangun datar di sini

    # Konversi Satuan
    elif pilihan == '4':
        print("Anda Memilih Konversi Satuan :o")
        # Tambahkan kode konversi satuan di sini

    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
