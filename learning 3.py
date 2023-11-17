def halo() :
    print ("Halo Dunia, Selamat Bertemu")
    
def luaspersegi (panjang, lebar) :
    luas = panjang * lebar
    print ("Luas Persegi Panjang =", luas)

def halo ():
    print ("Halo dunia selamat bertemu")
    print ("Salam dari Cianjur")
    
#memanggil fungsi
halo ()

#fungsi dengan paramater
def luaspersegipanjang (panjang, lebar):
    luas = panjang * lebar
    print ("LuasPersegi panjang : %d" % luas)
    
luaspersegipanjang (4, 6)
luaspersegipanjang (696969, 69696969)

#fungsi mengembalikan nilai
def luaspersegipanjang (panjang, lebar):
    luas = panjang * lebar
    return luas 

print ("Luas : %d" % luaspersegipanjang (6,3))

def faktorial (n):
    if n <= 1:
        return 1
    else:
        return n * faktorial (n-1)
    
i = 0
n = int (input("Berapa Faktorial : "))

while i<=n :
    print (i, '! = ', faktorial(i))
    i += 1
    #Variabel global & lokal
nama = "Alvin Agusta"
alamat = "Expo"
def testing () :
    #ini variabel lokal
    nama = "Navida Wahyu"
    alamat ="Bocu"
    #mengakses variabel lokal
    print ("Nama : %s " % nama)
    print ("Alamat : %s" % alamat)
#mengakses variabel global
print ("VARIABEL GLOBAL")
print ("Nama : %s " % nama)
print ("Alamat : %s " % alamat)

#memanggil fungsi testing lokal ()
print ("VARIABEL LOKAL")
testing ()