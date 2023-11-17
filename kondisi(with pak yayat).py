#operator aritmatika
# + - / * %(Mod (Sisa Bagi Dari Sebuah Operasi Matematika))
#operator perbandingan
#== >< =< >= !=
#gerbang logika and
#gerbang logika or
# warna =input("Silahkan Masukkan Warna :")
# if warna == 'merah':
#     print ("INDONESIA BERDARAH MERAH!!!!!!!!!!!!!!")
# elif warna == 'putih':
#     print ("INDONESIA BERWARNA PUTIH!!!!!!!!!!!!!!!")
# else :
#     print("Anda Tidak Nasionalis")

# nama =input("Masukkan Nama Murid :")
# print ("Nama :",nama)
# nilai =int(input("Masukkan Nilai :"))
# if nilai >= 75:
#     print(nama,"Anda Lulus Hore !!!! 😎")
# else :
#     print(nama,"Anda Tidak Lulus NOOOOO😭")

hari =int(input("Silahkan Masukkan Angka Hari :"))
if hari == 1:
    print ("Hari Senin")
elif hari == 2:
    print ("Hari Selasa")
elif hari == 3:
    print ("Hari Rabu")
elif hari == 4:
    print ("Hari Kamis")
elif hari == 5:
    print ("Hari Jumat")
elif hari == 6:
    print ("Hari Sabtu")
elif hari == 7:
    print ("Hari Minggu")
else:
    print ("Bukan Angka Hari")

USERNAME = 'admin'
PW ='nimda123'
user_input =(input("Silahkan Masukkan Username:"))
pw_input =input("silahkan Masukkan Password :")

if user_input == USERNAME and pw_input == PW:
    print ("Authentication Succses")
else:
    print ("Authentication Failed")
    
    