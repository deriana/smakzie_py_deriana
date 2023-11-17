suhu =input('Masukkan suhu dalam celcius (C or c) atau farenheit (f or F) atau kelvin (k or K) :')
#mendapatkan karakter terakhir
jenis =suhu [-1]
#karakter semua selain karakter terakir
suhu =float(suhu[:-1])

if jenis == 'f' or 'F':
    konversi = suhu *9/5 + 32
    print (f"{suhu} {jenis} = {konversi} C")
elif jenis == 'c' or 'C':
    konversi =(suhu -32)*5/9
    print (f"{suhu} {jenis} = {konversi} F")
