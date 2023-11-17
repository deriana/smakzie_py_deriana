#lambda Rumus Bangun Ruang Dan Datar
#kubus
luaskubus =lambda s:6*s**2
volumekubus =lambda s:s**3
#balok
luasbalok =lambda p,l,t: 2*(p*l+p*t+t*l)
p = 5
l = 3
t = 2
print (luasbalok(p,l,t))


volumebalok =lambda p,l,t: p*l*t
#tabung
luastabung =lambda r,t: 2*3.14*r*t+2*3.14*r**2
volumetabung =lambda r,t: 3.14*r**2
r =float(input("Silahkan Masukkan Jari Jari:"))
print (luastabung)