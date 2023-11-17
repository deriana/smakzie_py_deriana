print ("=================================")
print ("Anda Memilih Bangun Ruang Bola :3")
print ("=================================")

print ("1. Luas")
print ("2. Volume")
phi = 3.14
bola =input("Silahkan Masukkan Pilihan Anda :")
if bola ==  '1' :
    print ("Anda Memilih Luas")
    jari =float(input("Silahkan Masukkan Jari Jari Nya :"))
    print ('Luas = ',4*phi*jari**2)
elif bola == '2' :
    print ("Anda Memilih Volume")
    jari =float(input("Silahkan Masukkan Jari Jari Nya :"))
    print ('Volume = ',(4/3)*phi*jari**2)