#continue_pass_break
#pass berfungsi sebagai dummy, tidak akan di eksekusi

angka = 0

while angka < 10:
    angka += 1
    if angka == 5:
        pass #ini tidak akan dieksekusi
    print (angka)
    
#continue

angka = 0

while angka <5:
    angka += 1
    print (f"Angka Sekarang {angka}")
    
    if angka == 3:
        print ("Nice")
        continue
    print ("IM EMU OTORI")
print ("Free")

#break
data =int(input("Masukkan Angka :"))

angka = 0
while True:
    angka += 1
    print (f"Angka Sekarang{angka}")
    
    if angka == data:
        print ("WONDERHOY!!!!")
        break

    print ("EMU!!!!!!")
print ("MAMAH AKU TAKUT!!!")