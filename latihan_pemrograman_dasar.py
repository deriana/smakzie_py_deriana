#Tampilan Layar
print ("=======================================")
print ("Aku Anak PPLG YANG KUAT DAN SEMANGAT :)")
print ("=======================================")
#Perkalian
qty = 30
print (qty)
harga = 30000
print (harga)
print ('Hasil =',qty*harga)
#Membuat Variabel
nama = 'Kertas'
jumlah = 20
harga =1000000
ketersediaan = 'true'
print ('Nama Barang : ', nama)
print ('Jumlah Barang : ',jumlah)
print ('Harga Barang : ', harga)
print ('Ketersediaan : ',ketersediaan)
#Mencari Rata Rata
angka1 =87.77
angka2 =66.50
angka3 =97.5
print ('Angka Pertama = ', angka1)
print ('Angka Kedua = ', angka2)
print ('Angka Ketiga = ',angka3)
rata_rata_1_2 = (angka1 +angka2)/2
rata_rata_semua_nilai = (angka1 + angka2 + angka3)/3
print ('Rata Rata Dari Penjumlahan Angka 1 + 2 =',rata_rata_1_2)
print ('Rata Rata Dari Penjumlahan Semua Nilai Itu = ',rata_rata_semua_nilai)
#INPUTAN
kelompok =input('Kelompok : ')
asal_daerah =input('Asal Daerah : ')
jumlah_tim =int(input('Jumlah Tim (orang):'))
print ("Kelompok : ",kelompok)
print ("Asal Daerah : ",asal_daerah)
print ("Jumlah Tim : ",jumlah_tim, "Orang")
#INPUTAN
barang1 =int (input("Masukkan Angka Pertama :"))
barang2 =int (input("Masukkan Angka Kedua :"))
barang3 =int (input("Masukkan Angka Ketiga :"))
barang4 =int (input("Masukkan Angka Keempat :"))
print ("Hasil Penjumlahan = ",barang1+barang2+barang3+barang4)
#IF and ELSE
barang =float (input('Masukkan Harga Barang :'))
if (barang >=100000):
    diskon = barang*0.05
    print ("Anda Mendapat Diskon 5%")
else :
    diskon = 0
harga = barang - diskon
print ("Diskon : Rp", diskon)
print ("Total Yang Harus Dibayar Rp", harga)
#Menghitung Luas Bangunan
print ("Lingkaran")
jari =float(input('Masukkan Jari Jari Nya :'))
diameter =float(input("Masukkan Diameter Nya :"))
print ('Luas = ',3.14*jari**2)
print ('Keliling = ',3.14*diameter)

print ("Segitiga")
alas =float(input('Masukkan Alas Nya :'))
tinggi =float(input('Masukkan Tinggi Nya :'))
sisi1 =float(input('Masukkan Sisi Nya :'))
sisi2 =float(input('Masukkan Sisi Nya :'))
sisi3 =float(input('Masukkan Sisi Nya :'))

print ('Luas = ',1/2*alas*tinggi)
print ('Keliling = ',sisi1+sisi2+sisi3)

print ("Trapesium")
tinggi =float(input("Masukkan Tinggi Nya :"))
sisi1 =float(input('Masukkan Sisi 1 Nya :'))
sisi2 =float(input('Masukkan Sisi 2 Nya :'))
sisi3 =float(input('Masukkan Sisi 3 Nya :'))
sisi4 =float(input('Masukkan Sisi 4 Nya :'))
print ('Luas = ',0.5*(sisi1+sisi3)*tinggi)
print ('Keliling = ',sisi1+sisi2+sisi2+sisi3+sisi3+sisi4+sisi4+sisi1)

print ("Jajar Genjang")
alas =float(input("Masukkan Alas Nya :"))
tinggi =float(input("Masukkan Tinggi Nya"))
panjang =float(input("Masukkan Panjang Nya"))
lebar =float(input("Masukkan Lebar Nya"))
print ('Luas = ',alas*tinggi)
print ('Keliling = ',2*(panjang+lebar))
#Bangun Ruang
print ("Balok")
panjang =int(input('Masukkan Panjang Nya :'))
lebar =int(input('Masukkan Lebar Nya :'))
tinggi =int(input('Masukkan Tinggi Nya :'))
print ('Luas = ',2*(panjang*lebar+panjang*tinggi+lebar*tinggi))
print ('Volume = ',panjang*lebar*tinggi)
print ("Kubus")
sisi =int(input('Masukkan Sisi Nya :'))
print ('Luas = ',6*sisi**2)
print ('Volume = ',sisi**3)
print ("Bola")
jari =float(input('Masukkan Jari Jari Nya :'))
print ('Luas = ',4*3.14*jari**2)
print ('Volume = ',(4/3)*3.14*jari**3)
print ("Tabung")
jari_alas =float(input('Masukkan Jari Jari Alas Nya : '))
tinggi =float(input("Masukkan Tinggi Nya :"))
print ('Luas = ',2*3.14*jari_alas*(jari_alas + tinggi))
print ('Volume = ',3.14*jari_alas**2*tinggi)
print ("Kerucut")
jari_alas =float(input('Masukkan Jari Jari Alas Nya :'))
garis =float(input('Masukkan Garis Pelukis Nya :'))
tinggi =float(input('Masukkan Tinggi Nya :'))
print ('Luas = ',3.14*jari_alas*(jari_alas+garis))
print ('Volume =',(1/3)*3.14*jari_alas**2*tinggi)
print ('Prisma Segi Lima')
alas =int(input('Masukkan Luas Alas Nya :'))
sisi =int(input('Masukkan Luas Sisi Nya :'))
tinggi =int(input('Masukkan Tinggi Nya :'))
print ('Luas =',alas+(5*sisi))
print ('Volume =',alas*tinggi)
print ('Limas Segitiga')
alas =float(input('Masukkan Luas Alas :'))
panjang =float(input('Masukkan Panjang Keliling Segitiga Alas :'))
garis =float(input('Masukkan Panjang Garis Pelukis :'))
tinggi =float(input('Masukkan Tinggi Limas :'))
print ('Luas =',alas+(0.5)*panjang*alas)
print ('Volume =',(1/3)*alas*tinggi)
#Pengingputan If Or Else Dari Kelipatan 3
bilangan =int(input("Masukkan Bilangan Nya :"))
if bilangan %3 == 0 :
    print ("Bilangan",bilangan, "Adalah Kelipatan 3")
else :
    print("Anda Belum Beruntung")
#Tampilan Pengulangan Menggunakan Do While
text ='Cerdas'
count = 0

while count <4 :
    if count <3:
        print (text, end='+')
    else:
        print (text)
    count +=1
#Pengulangan Angka Menggunakan While
i = 1
end =5
total =0
while i <= end:
    total += i
    print (i, end="")
    if i < end:
        print (" + ",end="")
    i =i + 1
print (" = ", total)
#Pengulangan For
for y in range(4):
    for x in range(1,6):
        print (x, end="")
    print ()
#Pengulangan For
for d in ("abcd"):
    print (d*5)
for x in ("e"):
    print (x*6) 