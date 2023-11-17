while True:
    print("==========================================")
    print("============Madilbs Generator=============")
    print("==========================================")
    print("Opsi Cerita Dari Madlibs Generator")
    print("1. Cerita Happy Ending 😊")
    print("2. Cerita Sad Ending 😭")
    print("3. Keluar ? 😥")
    print("==========================================")

    choice = int(input("Masukkan pilihan anda: "))

    if choice == 1:
        # Fungsi untuk mengakses file dengan nama yang sesuai
        with open("story_happy.txt", "r") as f:
            story = f.read()

        # ... (bagian pengisian jawaban dan pemrosesan cerita)

        print(story)
        input("Tekan Enter untuk melanjutkan...")
    elif choice == 2:
        # Fungsi untuk mengakses file dengan nama yang sesuai
        with open("story_sad.txt", "r") as f:
            story = f.read()

        # ... (bagian pengisian jawaban dan pemrosesan cerita)

        print(story)
        input("Tekan Enter untuk melanjutkan...")
    elif choice == 3:
        print("=========================================")
        print("   TERIMA KASIH TELAH MENGGUNAKAN       ")
        print("       APLIKASI KAMI DI PYTHON          ")
        print("=========================================")
        break
    else:
        print ("=====================================")
        print ("=========Authentication Eror=========")
        print ("=====================================")
    
    back = input("Ketik 'apapun' untuk kembali atau 'keluar' untuk keluar [Yakin mau keluar :((( ] :")
    if back.lower() == 'keluar':
        print("=========================================")
        print("   TERIMA KASIH TELAH MENGGUNAKAN       ")
        print("       APLIKASI KAMI DI PYTHON          ")
        print("=========================================")  
        break
