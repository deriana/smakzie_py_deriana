nilai = int(input ('Masukkan Nilai = '))

if (nilai > 75):
    print ("Anda Lulus")
else :
    print ("Anda gagal harus mengulang")
    
    barang =float (input('Masukkan Harga Barang :'))
if (barang >=100000):
    diskon = barang*0.05
    print ("Anda Mendapat Diskon 5%")
else :
    diskon = 0
harga = barang - diskon
print ("Diskon : Rp", diskon)
print ("Total Yang Harus Dibayar Rp", harga)