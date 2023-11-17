#Latihan Perulangan

# jumlah =int(input("Silahkan Masukkan Jumlah ="))
jumlah = 5
count = 1


for x in range (jumlah):
    print ("X"*count)
    count += 1

#menggunakan While
jumlah = 100
count = 1
while True:
    print ("*"*count)
    count += 1

    if count > jumlah:
        break
    
#Hanya Ganjil Saja
jumlah = 20
spasi = int (jumlah/2)
count = 1
while True:
    #jika genap akan menjalankan ini
    if (count %2):
        print (" "*spasi," "*count)
        spasi -= 1
        count += 1
    else:#jika ganjil kembali ke atas
        count += 1
        continue
    #akan beres (break) jika program sudah melakukan apa yang diminta
    if count > jumlah:
        break