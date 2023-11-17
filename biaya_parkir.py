#Input Jam Masuk Dan Jam Keluar
jam_masuk =int(input("Silahkan Masukkan Jam Masuk Anda (1-12):"))
jam_keluar =int(input("Silahkan Masukkan Jam Keluar Anda (1-12):"))

#Kondisi
if jam_masuk <1 or jam_masuk >12 or jam_keluar <1 or jam_keluar>12:
    print ("====================================================")
    print ("Authentication Eror Please Enter The Correct Data")
    print ("====================================================")
    #Menghitung lama/Waktu Parkir
else:
    if jam_keluar > jam_masuk:
        lama =jam_keluar - jam_masuk
    else:
        lama=(12 - jam_masuk) + jam_keluar
    #Menghitung Biaya Parkir
    biaya_pertama = 2000
    biaya_selanjutnya = 500
    if lama <=2:
        biaya_total = biaya_pertama
    else:
        biaya_total = biaya_pertama +(lama - 2)*biaya_selanjutnya

print (f"Lama Parkir : {lama} Jam.")
print (f"Biaya Parkir : Rp.{biaya_total}")