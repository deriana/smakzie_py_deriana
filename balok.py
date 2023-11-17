print ("=================================")
print ("\tBangun Ruang Balok :3")
print ("=================================")
print ("1. Luas")
print ("2. Volume")
balok =input("Silahkan Masukkan Pilihan Anda :")
if balok == '1':
    print ("Anda Memilih luas")
    panjang =int(input('Silahkan Masukkan Panjang Nya :'))
    lebar =int(input('Silahkan Masukkan Lebar Nya :'))
    tinggi =int(input('Silahkan Masukkan Tinggi Nya :'))
    print ('Luas = ',2*(panjang*lebar+panjang*tinggi+lebar*tinggi,'cm2'))
elif balok == '2':
    print ("Anda Memilih Volume")
    panjang =int(input('Silahkan Masukkan Panjang Nya :'))
    lebar =int(input('Silahkan Masukkan Lebar Nya :'))
    tinggi =int(input('Silahkan Masukkan Tinggi Nya :'))
    print ('Volume = ',panjang*lebar*tinggi,'cm3')
                