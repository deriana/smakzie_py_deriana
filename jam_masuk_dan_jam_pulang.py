#Input Jam Masuk Dan Jam Pulang
jam_masuk =int(input("Silahkan Masukkan Jam Masuk Anda (1-12) :"))
jam_pulang =int(input("Silahkan Masukkan Jam Pulang Anda (1-12) :"))

#Kondisi
if jam_masuk < 1 or jam_masuk > 12 or jam_pulang < 1 or jam_pulang >12 :
    print ("====================================================")
    print ("Authentication Eror Please Enter The Correct Data")
    print ("====================================================")
    #Menghitung Lama Bekerja
else:
    if jam_pulang > jam_masuk:
        lama_bekerja =jam_pulang - jam_masuk
    else:
        lama_bekerja = (12-jam_masuk) + jam_pulang
        
    print(f"Lama Bekerja Seorang Pekerja {lama_bekerja} Jam.")