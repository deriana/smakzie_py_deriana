print ("Arithemic Operator")
print (10 + 5)
print (10 - 5)
print (10 * 5)
print (10 / 5)
print (10**5)
print (10 // 5)

nilai = float(input ('Masukkan Nilai = '))

if (nilai > 75):
    print ("Anda Lulus")
elif (nilai <= 75 ):
    print ("Anda Remedial")
else :
    print ("Anda gagal harus mengulang")
    
ulang = 6969
print (ulang)

ulang = 1
while (ulang < 9) :
    print ('Perulangan ke :', ulang)
    ulang = ulang + 1
print ("Perulangan Selesai")
    
ulang = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
for x in ulang:
    print ("Saya Piket Di Hari ", x )
    
for x in range (6, 16, 2):
    print ("perulangan ke", x)
    
for i in range (2) :
    for j in range(6,10,1):
        print ("nilai i=",i,"j=", j )

def halo() :
    print ("Halo Dunia, Selamat Bertemu")
    
def luaspersegi (panjang, lebar) :
    luas = panjang * lebar
    print ("Luas Persegi Panjang =", luas)
    