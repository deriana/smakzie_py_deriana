#Soal 1 Hello World
print ("Hello World")
print ("===========================")
print ("Hello Algoritma ----------------")

#Soal 2 Program persegi
print ("===================================")
print ("PROGRAM PERSEGI")
print ("===================================")

sisi = int(input("Masukkan Sisi :"))
print (f"Luas : {sisi**2} cm2")
print (f"Keliling : {4*sisi} cm")

#Soal 2 program segitiga
print ("===================================")
print ("PROGRAM SEGITIGA")
print ("===================================")

t =float(input("Masukkan Tinggi :"))
a =float(input("Masukkan Alas: "))
sa =int(input("Masukkan Sisi a"))
sb =int(input("Masukkan Sisi b"))
sc =int(input("Masukkan Sisi c"))
print (f"Luas : {0.5*a*t} cm2")
print (f"Keliling : {sa+sb+sc} cm")

#Soal 2 program lingkaran 
print ("===================================")
print ("Program Lingkaran")
print ("===================================")

phi =3.14
r =float(input("Masukkan jari-jari :"))
d =float(input("Masukkan Diameter : "))
print (f"Luas : {phi*r**2} cm2")
print (f"Keliling : {2*r*d}")

#Soal 3 program konversi suhu
print ("===================================")
print ("Program Konversi Suhu")
print ("===================================")

c =float(input("Masukkan Suhu Dalam Celcius :"))

print (f"Suhu dalam Farenheit :{(c*9/5)+32}")
print (f"Suhu dalam Reamur :{4/5*c}")

#Soal 4 program kelulusan
print ("===================================")
print ("PROGRAM KELULUSAN")
print ("===================================")

nilai =int(input("Masukkan Nilai :"))

if nilai >= 75:
    print ("LULUS")
else:
    print ("TIDAL LULUS")