#Soal 10

kalimat = input("Masukkan Kalimat : ")

kata_pertama = kalimat.split()[0].lower()

if kata_pertama != 'apakah':
    kalimat = "Apakah " + kalimat
    
tanda_akhir =kalimat [-1]
if tanda_akhir not in ['.', '!','?']:
    kalimat += "?"
    
print (kalimat)