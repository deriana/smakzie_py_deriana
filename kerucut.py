print ("=================================")
print ("Anda Memilih Bangun Ruang Kerucut :3")
print ("=================================")

print ("1. Luas")
print ("2. Volume")
phi =3.14
kerucut =input("Silahkan Masukkan Pilihan Anda :")
if kerucut == '1':
    print ("Anda Memilih Luas")
    jari =float(input('Silahkan Masukkan Jari Jari Alas Nya :'))
    garis =float(input('Silahkan Masukkan Garis Pelukis Nya :'))
    tinggi =float(input('Silahkan Masukkan Tinggi Nya :'))
    print ('Luas = ',phi*jari*(jari+garis),'cm2')
elif kerucut == '2':
    print ("Anda Memilih Volume")
    jari =float(input('Silahkan Masukkan Jari Jari Alas Nya :'))
    tinggi =float(input('Silahkan Masukkan Tinggi Nya :'))
    print ('Volume =',(1/3)*phi*jari**2*tinggi,'cm3')