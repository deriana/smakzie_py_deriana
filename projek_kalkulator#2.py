print("=======================================")
print("Welcome To My Calculator Project :3")
print("-By Hideri")
print("=======================================")

while True:
    print("1. Kalkulator Biasa")
    print("2. Kalkulator Bangun Ruang")
    print("3. Kalkulator Bangun Datar")
    print("4. Konversi Satuan")
    print('5. Keluar')

    pilihan = input("Masukkan Pilihan Anda =")

    if pilihan == '5':
        print("Terima Kasih Telah Menggunakan Kalkulator Saya :)")
        break  # Keluar dari program jika pilihan adalah '5'
       
    # Kalkulator Biasa
    if pilihan == '1':
        print("Anda Memilih Pilihan Yaitu Kalkulator Biasa/Normal :>")
        #Kode Kalkulator Biasa
        def tambah (x,y):
            return x + y
        def kurang (x,y):
            return x - y
        def kali (x,y):
            return x*y
        def bagi (x,y):
            return x/y
        def pangkat (x,y):
            return x**y
        print ("1. Tambah")
        print ("2. Kurang")
        print ("3. Kali")
        print ("4. Bagi")
        print ("5. Pangkat")    
        kalkulator =input("Masukkan Pilihan Anda :")
        if kalkulator == '1':
            print ("Anda Memilih Pertambahan")
            num1 =int(input("Masukkan Bilangan/Angka Pertama :"))
            num2 =int(input("Masukkan Bilangan/Angka Kedua :"))
            print ('Hasil :', tambah(num1,num2))
        elif kalkulator == '2' :
            print ("Anda Memilih Pengurangan")    
            num1 =int(input("Masukkan Bilangan/Angka Pertama :"))
            num2 =int(input("Masukkan Bilangan/Angka Kedua :"))
            print ('Hasil :', kurang(num1,num2))
        elif kalkulator == '3' :
            print ("Anda Memilih Perkalian")
            num1 =int(input("Masukkan Bilangan/Angka Pertama :"))
            num2 =int(input("Masukkan Bilangan/Angka Kedua :"))
            print ('Hasil :', kali(num1,num2))
        elif kalkulator == '4':
            print ("Anda Memilih Pembagian")
            num1 =float(input("Masukkan Bilangan/Angka Pertama :"))
            num2 =float(input("Masukkan Bilangan/Angka Kedua :"))
            print ('Hasil : ', bagi(num1,num2,))
        elif kalkulator == '5' :
            print ("Anda Memilih Perpangkatan")
            num1 =int(input("Masukkan Bilangan/Angka Pertama :"))
            num2 =int(input("Masukkan PangkatNya :"))
            print ('Hasil : ', pangkat(num1,num2))
        else :
            print ("Pilihan Tidak Valid")
    # Kalkulator Bangun Ruang
    elif pilihan == '2':
        print("Anda Memilih Kalkulator Bangun Ruang :3")
        #Kode Kalkulator Bangun Ruang
        print ("1. Kubus")
        print ("2. Balok")
        print ("3. Tabung")
        print ("4. Kerucut")
        print ("5. Bola")
        print ("6. Prisma Segitiga")
        print ("7. Limas Segitiga")
        print ("8. Kubah")
        print ("9. Prisma Segiempat")
        print ("10. Limas Segiempat")
        phi =3.14
        bangun =(input("Masukkan Pilihan Anda : "))
        if bangun == '1':
            print ("Anda Memilih Bangun Ruang Kubus :3")
            sisi =int(input('Silahkan Masukkan Sisi Nya :'))
            print ('Luas = ',6*sisi**2)
            print ('Volume = ',sisi**3)
        elif bangun == '2':
            print ("Anda Memilih Bangun Ruang Balok :3")
            panjang =int(input('Silahkan Masukkan Panjang Nya :'))
            lebar =int(input('Silahkan Masukkan Lebar Nya :'))
            tinggi =int(input('Silahkan Masukkan Tinggi Nya :'))
            print ('Luas = ',2*(panjang*lebar+panjang*tinggi+lebar*tinggi))
            print ('Volume = ',panjang*lebar*tinggi)
        elif bangun == '3':
            print ("Anda Memilih Bangun Ruang Tabung :3")
            alas =float(input("Silahkan Masukkan Alas Nya : "))
            r =float(input("Silahkan Masukkan Jari Jari Nya :"))
            tinggi =float(input("Silahkan Masukkan Tinggi Nya :"))
            print ('Luas = ',2*phi*r*tinggi+2*phi*r**2)
            print ('Volume = ',phi*r**2*tinggi)
        elif bangun == '4':
            print ("Anda Memilih Bangun Ruang Kerucut :3")
            jari =float(input('Silahkan Masukkan Jari Jari Alas Nya :'))
            garis =float(input('Silahkan Masukkan Garis Pelukis Nya :'))
            tinggi =float(input('Silahkan Masukkan Tinggi Nya :'))
            print ('Luas = ',phi*jari*(jari+garis))
            print ('Volume =',(1/3)*phi*jari**2*tinggi)
        elif bangun == '5' :
            print ("Anda Memilih Bangun Ruang Bola :3")
            jari =float(input("Silahkan Masukkan Jari Jari Nya :"))
            print ('Luas = ',4*phi*jari**2)
            print ('Volume = ',(4/3)*phi*jari**2)
        elif bangun == '6' :
            print ("Anda Memilih Bangun Ruang Prisma Segitiga :3")
            ls =float(input("Silahkan Masukkan Luas Segitiga Nya : "))
            ks =float(input("Silahkan Masukkan Keliling Segitiga Nya : "))
            tp =float(input("Silahkan Masukkan Tinggi Prisma Nya :"))
            print ('Luas = ',2*(ls)+(ks*tp))
            print ('Volume = ',ls*tp)
        elif bangun == '7':
            print ("Anda Memilih Bangun Ruang Limas Segitiga :3")
            la =float(input("Silahkan Masukkan Luas Alas Nya :"))
            ls =float(input("Silahka Masukkan Luas Segitiga Nya :"))
            tl =float(input("Silahkan Masukkan Tinggi Limas Nya :"))
            print ('Luas = ',la+3*(ls))
            print ('Volume = ',(la*tl)/3)
        elif bangun == '8':
            print ("Anda Memilih Bangun Ruang Kubah :3")
            sisi =int(input("Silahkan Masukkan Panjang Sisi : "))
            print ('Luas = ',6*sisi**2)
            print ('Volume = ',sisi**3)
        elif bangun == '9':
            print ("Anda Memilih Bangun Ruang Prisma Segiempat :3")
            la =int(input("Silahkan Masukkan Luas Alas Nya : "))
            ka =int(input("Silahkan Masukkan Keliling Alas Nya :"))
            t =int(input("Silahkan Masukkan Tinggi Nya :"))
            print ('Luas = ',2*la*ka*t)
            print ('Volume = ',la*t)
        elif bangun == '10':
            print ("Anda Memilih Bangun Ruang Limas Segiempat :3")
            la =float(input("Silahkan Masukkan Luas Alas Nya :"))
            tg =float(input("Silahkan Masukkan Tinggi Nya :"))
            kl =float(input("Silahkan Masukkan Keliling Alas Nya :"))
            st =float(input("Silahkan Masukkan Sisi Tegak Nya : "))
            print ('Luas = ',la+0.5*kl*st)
            print ('Volume = ',1/3*la*tg)
        else :
            print ("Data Yang Anda Input Tidak Valid")
    # Kalkulator Bangun Datar
    elif pilihan == '3':
        print("Anda Memilih Kalkulator Bangun Datar <3")
        #Kode Kalkulator Bangun Datar
        print ("1. Persegi")
        print ("2. Persegi Panjang")
        print ("3. Segitiga") 
        print ("4. Trapesium") 
        print ("5. Jajar Genjang")      
        print ("6. Lingkaran")
        print ("7. Layang Layang")
        print ("8. Belah Ketupat")
        datar =(input("Masukkan Pilihan Anda :"))
        if datar == '1':
            print ("Anda Memilih Bangun Datar Persegi <3")
            sisi =int(input("Silahkan Masukkan Sisi Nya :"))
            print ('Luas = ',sisi**2)
            print ('Keliling = ',4*sisi)
        elif datar == '2':
            print ("Anda Memilih Bangun Datar Persegi Panjan <3")
            pj =int(input("Silahkan Masukkan Panjang Nya :"))
            lb =int(input("Silahkan Masukkan Lebar Nya : "))
            print ('Luas =',pj*lb)
            print ('Keliling = ',2*(pj*lb))
        elif datar =='3':
            print ("Anda Memilih Bangun Datar Segitiga")
            print ('1. Segitiga Sama Sisi')
            print ('2. Segitiga Sama Kaki')
            print ('3. Segitiga Sembarang')
            segitiga =(input("Masukkan Pilihan Anda :"))
            if pilihan == '1':
                print ("Anda Memilih Segitiga Sama Sisi")
                alas =float(input("Silahkan Masukkan Alas Nya :"))
                tinggi =float(input("Silahkan Masukkan Tinggi Nya :"))
                sisi =float(input("Silahkan Masukkan Sisi Nya"))
                print ("Luas = ",0.5*alas*tinggi)
                print ("Keliling = ",sisi**3)
            elif pilihan == '2':
                print ("Anda Memilih Segitiga Sama Kaki")
                alas =float(input("Silahkan Masukkan Alas Nya :"))
                tinggi =float(input("Silahkan Masukkan Tinggi Nya :"))
                sisi =float(input("Silahkan Masukkan Sisi Nya"))
                print ("Luas = ",0.5*alas*tinggi)
                print ("Keliling = ",sisi**3)
            elif pilihan == '3':
                print ("Anda Memilih Segitiga Sembarang")
                alas =float(input("Silahkan Masukkan Alas Nya :"))
                tinggi =float(input("Silahkan Masukkan Tinggi Nya :"))
                sisia =float(input("Silahkan Masukkan SisiA Nya :"))
                sisib =float(input("Silahkan Masukkan SisiB Nya :"))
                sisic =float(input("Silahkan Masukkan SisiC Nya :"))
                print ('Luas = ',0.5*alas*tinggi)
                print ('Keliling =',sisia+sisib+sisic)
        elif datar == '4':
            print ("Anda Memilih Bangun Datar Trapesium <3")
            tg =float(input("Silahkan Masukkan Tinggi Nya :"))
            sj =float(input("Silahkan Masukkan Sisi Sejajar Nya :"))
            sa =float(input("Silahkan Masukkan SisiA Nya :"))
            sb =float(input("Silahkan Masukkan SisiD Nya :"))
            sc =float(input("Silahkan Masukkan SisiC Nya :"))
            sd =float(input("Silahkan Masukkan SisiD Nya :"))
            print ("Luas = ",0.5*(sj)*tg)
            print ("Keliling = ",sa+sb+sc+sd)
        elif datar == '5':
            print ("Anda Memilih Bangun Datar Jajar Genjang <3")
            alas =float("Silahkan Masukkan Alas Nya :")
            tinggi =float("Silahkan Masukkan Tinggi Nya :")
            s1 =float(input("Silahkan Masukkan Sisi Sejajar 1 Nya :"))
            s2 =float(input("Silahkan Masukkan Sisi Sejajar 2 Nya :"))
            print ('Luas = ',alas*tinggi)
            print ('Keliling = ',2*(s1+s2))
        elif datar == '6':
            print ("Anda Memilih Bangun Datar Lingkaran <3") 
            r =float(input("Silahkan Masukkan Jari Jari Nya :"))
            d =float(input("Silahkan Masukkan Diameter Nya :"))
            print ('Luas = ',3.14*r**2)
            print ('Keliling = ',2*r*d)
        elif datar == '7':
            print ("Anda Memilih Bangun Datar Layang Layang <3")
            dg1 =float(input("Silahkan Masukkan Diagonal Pertama Nya :"))
            dg2 =float(input("Silahkan Masukkan Diagonal Kedua Nya :"))
            ps1 =float(input("Silahkan Masukkan Panjang Sisi Pertama Nya :"))
            ps2 =float(input("Silahkan Masukkan Panjang Sisi Kedua Nya"))
            print ('Luas = ',0.5(dg1*dg2))
            print ('Keliling = ',2*(ps1*ps2))
        elif datar == '8':
            print ("Anda Memilih Bangun Datar Belah Ketupat <3")
            dg1 =float(input("Silahkan Masukkan Diagonal Pertama Nya :"))
            dg2 =float(input("Silahkan Masukkan Diagonal Kedua Nya :"))
            sisi =float(input("Silahkan Masukkan Sisi Nya"))
            print ('Luas = ',(dg1*dg2)/2)
            print ('Keliling = ',4*sisi)
        else:
            print("Data Yang Anda Input Tidak Valid")
    # Konversi Satuan
    elif pilihan == '4':
        print("Anda Memilih Konversi Satuan :o")
        #Kode Konversi Satuan

    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

    kembali = input("Ketik 'iya' untuk kembali atau 'keluar' untuk keluar: ")
    
    if kembali.lower() == 'keluar':
        print("Terima Kasih Telah Menggunakan Kalkulator Saya :)")
        print("Maafkan Bila Ada Kurang Dan Salah Soalnya Masih Pelajar Juga :v")
        print("#MASIH_BERKARYA")
        break  # Keluar dari program jika pengguna memilih 'keluar'
