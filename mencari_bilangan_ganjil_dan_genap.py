print ("======================================")
print ("Program Mencari Angka Ganjil Dan Genap")
print ("======================================")
#Menu

while True:
    print ("1.Ganjil")
    print ("2.Genap")
    print ("3.Keluar")
    pilihan =(input("Masukkan pilihan anda:"))
    
    if pilihan == '1':
        print ("Anda Memilh Ganjil")
        ganjil =int(input("Silahkan masukkan angka yang ingin dicari:"))
        
        for x in range(1, ganjil):
            if x % 2 != 0:
                print(f"Angka Yang Ganjil: {x}")
    if pilihan == '2':
        print ("Anda Memilih Genap")
        genap =int(input("Masukkan pilihan anda:"))
        
        for y in range (1, genap):
            if y %2 == 0:
                print (y)
    if pilihan == '3':
        print ("Anda Keluar :(")
        print ("Terima Kasih Telah Menggunakan Proggram Ini")
        break
    else:
        print ("Pilhan Tidak Valid")
    kembali = input("Ketik 'iya' untuk kembali atau 'keluar' untuk keluar: ")
    if kembali.lower() == 'keluar':
        print ("Anda Keluar :(")
        print ("Terima Kasih Telah Menggunakan Proggram Ini")
        break