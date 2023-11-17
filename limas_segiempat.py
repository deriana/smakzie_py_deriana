print ("=================================")
print ("Bangun Ruang Limas Segiempat :3")
print ("=================================")

print ("1. Luas")
print ("2. Volume")
limas =input("Silahkan Masukkan Pilihan Anda :")
if limas == '1':
    print ("Anda Memilih Luas")
    la =int(input("Silahkan Masukkan Luas Alas Nya :"))
    tg =int(input("Silahkan Masukkan Tinggi Nya :"))
    kl =int(input("Silahkan Masukkan Keliling Alas Nya :"))
    st =int(input("Silahkan Masukkan Sisi Tegak Nya : "))
    print ('Luas = ',la+0.5*kl*st,'cm2')
elif limas == '2':
    print ("Anda Memilih Volume")
    la =float(input("Silahkan Masukkan Luas Alas Nya :"))
    tg =float(input("Silahkan Masukkan Tinggi Nya :"))
    print ('Volume = ',1/3*la*tg,'cm3')