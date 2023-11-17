print ("=================================")
print ("Ruang Prisma Segitiga :3")
print ("=================================")

print ("1. Luas ")
print ("2. Volume")
prisma =input("Silahkan Masukkan Pilihan Anda :")
if prisma == '1':
    print ("Anda Memilih Luas")
    ls =float(input("Silahkan Masukkan Luas Segitiga Nya : "))
    ks =float(input("Silahkan Masukkan Keliling Segitiga Nya : "))
    tp =float(input("Silahkan Masukkan Tinggi Prisma Nya :"))
    print ('Luas = ',2*(ls)+(ks*tp),'cm2')
elif prisma == '2':
    print ("Anda Memilih Volume")
    ls =float(input("Silahkan Masukkan Luas Segitiga Nya : "))
    tp =float(input("Silahkan Masukkan Tinggi Prisma Nya :"))
    print ('Volume = ',ls*tp,'cm3')