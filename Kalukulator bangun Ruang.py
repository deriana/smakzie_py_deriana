print ("Selamat Datang Di Kakulator Bangun ruang")

#RUMUS KUBUS
print("1 Kubus")
sisi = input('Masukkan sisi =')
sisi = int(sisi)
print ('Volume = ', sisi*sisi*sisi)
print ('Luas = ', 6*sisi*sisi)
#RUMUS BALOK
print ("2 Balok")
panjang =int(input('Masukkan panjang ='))
lebar =int(input('Masukkan lebar ='))
tinggi =int(input('Masukkan tinggi = '))
print ('Volume = ', panjang*lebar*tinggi)
print ('Luas =',2*(panjang*lebar+tinggi*lebar+panjang*tinggi))
#RUMUS KERUCUT
print ("3 Kerucut")
r =float(input('Masukkan Jari jari ='))
t =float(input('Masukkan Tinggi ='))
print ('Volume = ', 1/3*3/14*r*r*t )
print ('Luas = ', 3/14*r**2)