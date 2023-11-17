print ("=================================")
print ("Anda Memilih Bangun Ruang Limas Segitiga :3")
print ("=================================")

print ("1. Luas")
print ("2. Volume")
limas =input("Silahkan Masukkan Pilihan Anda :")
if limas == '1':
    print ("Anda Memilih Luas")
    la =float(input("Silahkan Masukkan Luas Alas Nya :"))
    ls =float(input("Silahka Masukkan Luas Segitiga Nya :"))
    tl =float(input("Silahkan Masukkan Tinggi Limas Nya :"))
    print ('Luas = ',la+3*(ls),'cm2')
elif limas =='2':
    print ("Anda Memilih Volume")
    la =float(input("Silahkan Masukkan Luas Alas Nya :"))
    tl =float(input("Silahkan Masukkan Tinggi Limas Nya :"))
    print ('Volume = ',(la*tl)/3,'cm3')