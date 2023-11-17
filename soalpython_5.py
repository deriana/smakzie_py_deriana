#Soal 5

daftar_buah = input("Masukkan Nama Buah Lalu Pisahkan Dengan Koma (,) =")

buah = daftar_buah.split(",")

if len(buah) >= 5:
    buah_dua =buah [1].strip()
    buah_empat = buah [3].strip()
    
    print (f"Buah Kedua {buah_dua}")
    print (f"Buah Keempat {buah_empat}")