print ("=================================")
print ("\tBangun Ruang Kubus :3")
print ("=================================")

print ("1. Luas")
print ("2. Volume")
kubus =input("Silahkan Masukkan Pilihan Anda :")
if kubus == '1':
    print ("Anda Memilih Luas") 
    sisi =int(input('Silahkan Masukkan Sisi Nya :'))
    print ('Luas = ',6*sisi**2,'cm2')
elif kubus == '2':
    print ("Anda Memilih Volume")
    sisi =int(input("Silahkan Masukkan Sisi :"))
    print ('Volume = ',sisi**3,'cm3')