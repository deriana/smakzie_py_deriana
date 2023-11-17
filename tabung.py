print ("=================================")
print ("Bangun Ruang Tabung :3")
print ("=================================")

print ("1. Luas")
print ("2. Volume")
phi =3.14
tabung =input("Silahkan Masukkan Pilihan Anda :")
if tabung == '1':
    print ("Anda Memilih Luas")
    alas =float(input("Silahkan Masukkan Alas Nya : "))
    r =float(input("Silahkan Masukkan Jari Jari Nya :"))
    tinggi =float(input("Silahkan Masukkan Tinggi Nya :"))
    print ('Luas = ',2*phi*r*tinggi+2*phi*r**2,'cm2')
elif tabung == '2':
    print ("Anda Memilih Volume")
    r =float(input("Silahkan Masukkan Jari Jari Nya :"))
    tinggi =float(input("Silahkan Masukkan Tinggi Nya :"))
    print ('Volume = ',phi*r**2*tinggi,'cm3')