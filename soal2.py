#latihan programing dasar
#Soal 1
print ("Hello Friends!")
#Soal 2
print ("AKU SMAKZIE")
print (2006)
#Soal 3
x = 100
teks = 'ngoding'

print (x)
print (teks)

#Soal 4

firsinteger = 30
secondinteger = '40'

print (f"Jumlah : {firsinteger + int(secondinteger)}")

#Soal 5

firsidecimal = 4.54
seconddecimal = '3.74'

print (f"Jumlah : {firsidecimal + float(seconddecimal)}")

#Soal 6
firststring = 'Hidup '
secondstring = 'adalah perjuaangan'

print (firststring + secondstring)

#Soal 7
nama_barang = 'Kertas'
jumlah_barang = 20
harga_barang = 100000
ketersediaan = True

print (f"Nama Barang : {nama_barang}")
print (f"Jumlah Barang : {jumlah_barang}")
print (f"Harga Barang : {harga_barang}")
print (f"Ketersediaan : {ketersediaan}")

#Soal 8
angka1 =87.77
angka2 =66.50
angka3 =97.5

print (angka1)
print (angka2)
print (angka3)

print (f"Rata Rata dari dua angka: {(angka1+angka2)/2}")
print (f"Rata Rata dari semua nilai : {(angka1+angka2+angka3)/3}")

#Soal 9

kelompok =input("Kelompok :")
asal_daerah =input("Asal Daerah :")
jumlah_tim =input("Jumlah Tim :")

#Soal 10
barang1 =int(input("Masukkan Data 1 :"))
barang2 =int(input("Masukkan Data 2 :"))
barang3 =int(input("Masukkan Data 3 :"))
barang4 =int(input("Masukkan Data 4 :"))

print (f"Hasil Jumlah : {barang1+barang2+barang3+barang4}")

#Soal 11
harga =float(input("Masukkan Harga :"))

if harga >= 100000:
    diskon = harga * 0.05
    print ("Anda Mendapat Potongan Sebesar 5% ")
else:
    diskon = 0
barang = harga - diskon
print (f"Diskon : {diskon}")
print (f"Harga Nya : {barang}")

#Soal 12
bilangan =int(input("Masukkan Bilangan :"))

if bilangan %11 == 0 :
    print ("Anda Beruntung, Ini Kelipatan 11")
else:
    print ("Anda Kurang Beruntung")
  
#Soal 13
angka1 =int(input("Masukkan Angka 1 :"))
angka2 =int(input("Masukkan Angka 2 :"))
angka3 =int(input("Masukkan Angka 3 :"))

angka_terbesar = angka1
angka_terkecil = angka1

if angka2 > angka_terbesar:
    angka_terbesar = angka2
if angka2 < angka_terkecil:
    angka_terkecil = angka2

if angka3 > angka_terbesar:
    angka_terbesar = angka3
if angka3 < angka_terkecil:
    angka_terkecil = angka3
    
print (f"Angka Terbesar : {angka_terbesar}")
print (f"Angka Terkecil : {angka_terkecil}")

#Soal 14
text = 'Cerdas'
count = 0

while count < 4:
    if count < 3:
        print (text, end=" ")
    else:
        print (text)
    count += 1

#Soal 15
awal = 1
akhir = 5
total = 0

while awal <= akhir:
    total += awal
    print (awal,end="")
    if awal < akhir:
        print (" + ",end="")
    awal += 1
print (f" = {total}")

#Soal 16
for x in ("1234"):
    print (x*4)

#Soal 17
for y in ('abcd'):
    print (y*5)
for x in ('e'):
    print (x*6)