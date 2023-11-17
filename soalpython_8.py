#Soal 8

angka =int(input("Masukkan Angka :"))

angka =len(str(angka))

if angka == 3:
    print ("Angka Bersifat Ratusan")
elif angka == 4:
    print ("Angka Bersifat Ribuan")
elif angka == 5:
    print ("Angka Bersifat Jutaan")
else:
    print ("EROR")