print("=========================")
print("=====Rumussegitiga=======")
print("=========================")
S1 = int(input("keliling segitiga 1:"))
S2 = int(input("keliling segitiga 2:"))
S3 = int(input("keliling segitiga 3:"))
Tinggi = int(input("tinggi :"))
luas_alas = int(input("luas alas :"))
alas = int(input("alas :"))
print ("==================================")
luas_selimut =( S1 + S2 + S3 ) * Tinggi
luas_permukaan =( S1 + S2 + S3 ) * Tinggi + alas * Tinggi
volume = 1 / 3 * luas_alas * Tinggi
print ("==================================")
print ('luas segitiga adalah : ', (luas_selimut))
print ('luas alas adalah : ' , (luas_permukaan))
print ("volume adalah : ", (volume))