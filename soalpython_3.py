#Soal 3
phi =3.14
volume_tabung =lambda r,t:phi*r**2*t

r =float(input("Masukkan Jari-Jari :"))
t =float(input("Masukkan Tinggi :"))

print (f"Volume = {volume_tabung(r,t)} cm")