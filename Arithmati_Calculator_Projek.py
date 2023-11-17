print("\033[92m=======================================")
print("Welcome To My Calculator Project\t")
print("-By Hideri :3")
print("=======================================")

while True:
    print("1. Kalkulator Biasa\t")
    print("2. Kalkulator Bangun Ruang\t")
    print("3. Kalkulator Bangun Datar\t")
    print("4. Konversi Satuan\t")
    print("5. Keluar\t")
    
    pilihan = input("Masukkan Pilihan Anda =")

    if pilihan == '5':
        print("Terima Kasih Telah Menggunakan Kalkulator Saya :)")
        print("Maafkan Bila Ada Kurang Dan Salah Soalnya Masih Pelajar Juga :v")
        print("#SIBUK_BERKARYA😎😎😎😎")
        print ("-DERIANA MARUF")
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
            print ("========================================")
            print ("====Data Yang Anda Input Tidak Valid====")
            print ("========================================")
            
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
        print ("11. Silinder")        
        phi =3.14
        bangun =(input("Masukkan Pilihan Anda : "))
        
        if bangun == '1':
            print ("Anda Memilih Bangun Ruang Kubus :3")
            print ("1. Luas")
            print ("2. Volume")
            kubus =input("Silahkan Masukkan Pilihan Anda :")
            if kubus == '1':
                print ("Anda Memilih Luas") 
                luaskubus =lambda s:6*s**2
                sisi =int(input("Silahkan Masukkan Sisi :"))
                print (f"Luas Kubus Adalah ={luaskubus(sisi)}")
            elif kubus == '2':
                print ("Anda Memilih Volume")
                volumekubus =lambda s:s**3
                sisi =int(input("Silahkan Masukkan Sisi :"))
                print (f"Volume Kubus Adalah ={volumekubus(sisi)}")
            else:
                print ("========================================")
                print ("====Data Yang Anda Input Tidak Valid====")
                print ("========================================")
                
        elif bangun == '2':
            print ("Anda Memilih Bangun Ruang Balok :3")
            print ("1. Luas")
            print ("2. Volume")
            balok =input("Silahkan Masukkan Pilihan Anda :")
            if balok == '1':
                print ("Anda Memilih luas")
                luasbalok =lambda p,l,t: 2*(p*l+p*t+t*l)
                panjang =int(input('Silahkan Masukkan Panjang Nya :'))
                lebar =int(input('Silahkan Masukkan Lebar Nya :'))
                tinggi =int(input('Silahkan Masukkan Tinggi Nya :'))
                print (f"Luas Balok Adalah ={luasbalok(panjang,lebar,tinggi)}")
            elif bangun == '2':
                print ("Anda Memilih Volume")
                volumebalok =lambda p,l,t: p*l*t
                panjang =int(input('Silahkan Masukkan Panjang Nya :'))
                lebar =int(input('Silahkan Masukkan Lebar Nya :'))
                tinggi =int(input('Silahkan Masukkan Tinggi Nya :'))
                print (f"Volume Balok Adalah ={volumebalok(panjang,lebar,tinggi)}")
            else:
                print ("========================================")
                print ("====Data Yang Anda Input Tidak Valid====")
                print ("========================================")
                    
        elif bangun == '3':
            print ("Anda Memilih Bangun Ruang Tabung :3")
            print ("1. Luas")
            print ("2. Volume")
            tabung =input("Silahkan Masukkan Pilihan Anda :")
            if tabung == '1':
                print ("Anda Memilih Luas")
                luastabung =lambda a,r,t: 2*phi*r*t+2*phi*r**2
                alas =float(input("Silahkan Masukkan Alas Nya : "))
                r =float(input("Silahkan Masukkan Jari Jari Nya :"))
                tinggi =float(input("Silahkan Masukkan Tinggi Nya :"))
                print (f"Luas Tabung Adalah ={luastabung(alas,r,tinggi)}")
            elif tabung == '2':
                print ("Anda Memilih Volume")
                volumetabung =lambda r,t:phi*r**2*t
                r =float(input("Silahkan Masukkan Jari Jari Nya :"))
                tinggi =float(input("Silahkan Masukkan Tinggi Nya :"))
                print (f"Volume Tabung Adalah ={volumetabung(r,tinggi)}")
            else:
                print ("========================================")
                print ("====Data Yang Anda Input Tidak Valid====")
                print ("========================================")
                
        elif bangun == '4':
            print ("Anda Memilih Bangun Ruang Kerucut :3")
            print ("1. Luas")
            print ("2. Volume")
            kerucut =input("Silahkan Masukkan Pilihan Anda :")
            if kerucut == '1':
                print ("Anda Memilih Luas")
                luaskerucut =lambda r,g:phi*r*(r+g)
                jari =float(input('Silahkan Masukkan Jari Jari Alas Nya :'))
                garis =float(input('Silahkan Masukkan Garis Pelukis Nya :'))
                print (f"Luas Kerucut Adalah ={luaskerucut(jari,garis,)}")
            elif kerucut == '2':
                print ("Anda Memilih Volume")
                volumekerucut =lambda r,t: (1/3)*phi*r**2*t
                jari =float(input('Silahkan Masukkan Jari Jari Alas Nya :'))
                tinggi =float(input('Silahkan Masukkan Tinggi Nya :'))
                print (f"Volume Kerucut Adalah ={volumekerucut(jari,tinggi)}")
            else:
                print ("========================================")
                print ("====Data Yang Anda Input Tidak Valid====")
                print ("========================================")
                
        elif bangun == '5' :
            print ("Anda Memilih Bangun Ruang Bola :3")
            print ("1. Luas")
            print ("2. Volume")
            bola =input("Silahkan Masukkan Pilihan Anda :")
            if bola ==  '1' :
                print ("Anda Memilih Luas")
                luasjari =lambda r:r*phi*r**2
                jari =float(input("Silahkan Masukkan Jari Jari Nya :"))
                print (f"Luas Bola Adalah {luasjari(jari)}")
            elif bola == '2' :
                print ("Anda Memilih Volume")
                volumejari =lambda r:(4/3)*phi*r**2
                jari =float(input("Silahkan Masukkan Jari Jari Nya :"))
                print (f"Volume Bola Adalah ={volumejari(jari)}")
            else:
                print ("========================================")
                print ("====Data Yang Anda Input Tidak Valid====")
                print ("========================================")
                    
        elif bangun == '6' :
            print ("Anda Memilih Bangun Ruang Prisma Segitiga :3")
            print ("1. Luas ")
            print ("2. Volume")
            prisma =input("Silahkan Masukkan Pilihan Anda")
            if prisma == '1':
                print ("Anda Memilih Luas")
                luasprismasegitiga =lambda l,k,t:2*(l)+(k*t)
                ls =float(input("Silahkan Masukkan Luas Segitiga Nya : "))
                ks =float(input("Silahkan Masukkan Keliling Segitiga Nya : "))
                tp =float(input("Silahkan Masukkan Tinggi Prisma Nya :"))
                print (f"Luas Prisma Segitiga Adalah ={luasprismasegitiga(ls,ks,tp)}")
            elif prisma == '2':
                print ("Anda Memilih Volume")
                volumeprismasegitiga =lambda l,t:l*t
                ls =float(input("Silahkan Masukkan Luas Segitiga Nya : "))
                tp =float(input("Silahkan Masukkan Tinggi Prisma Nya :"))
                print (f"Volume Prisma Segitiga Adalah ={volumeprismasegitiga(ls,tp)}")
            else:
                print ("========================================")
                print ("====Data Yang Anda Input Tidak Valid====")
                print ("========================================")
                    
        elif bangun == '7':
            print ("Anda Memilih Bangun Ruang Limas Segitiga :3")
            print ("1. Luas")
            print ("2. Volume")
            limas =input("Silahkan Masukkan Pilihan Anda :")
            if limas == '1':
                print ("Anda Memilih Luas")
                luaslimassegitiga =lambda la,ls: ls+3*la
                la =float(input("Silahkan Masukkan Luas Alas Nya :"))
                ls =float(input("Silahka Masukkan Luas Segitiga Nya :"))
                print (f"Luas Limas Segitiga Adalah ={luaslimassegitiga(la,ls)}")
            elif limas =='2':
                print ("Anda Memilih Volume")
                volumelimassegitiga =lambda l,t:(l*t)/3
                la =float(input("Silahkan Masukkan Luas Alas Nya :"))
                tl =float(input("Silahkan Masukkan Tinggi Limas Nya :"))
                print (f"Volume Limas Segitiga ={volumelimassegitiga(la,tl)}")
            else:
                print ("========================================")
                print ("====Data Yang Anda Input Tidak Valid====")
                print ("========================================")
                
        elif bangun == '8':
            print ("Anda Memilih Bangun Ruang Kubah :3")
            print ("1. Luas")
            print ("2. Volume")
            kubah =input("Silahkan Masukkan Pilihan Anda :")
            if kubah == '1':
                print ("Anda Memilih Luas")
                luaskubah =lambda s:6*s**2
                sisi =int(input("Silahkan Masukkan Panjang Sisi : "))
                print (f"Luas Kubah Adalah ={luaskubah(sisi)}")
            elif kubah == '2':
                print ("Anda Memilih Volume")
                volumekubah =lambda s:s**3
                sisi =int(input("Silahkan Masukkan Panjang Sisi : "))
                print (f"Volume Luas Kubah Adalah ={volumekubah(sisi)}")
            else:
                print ("========================================")
                print ("====Data Yang Anda Input Tidak Valid====")
                print ("========================================")
                
        elif bangun == '9':
            print ("Anda Memilih Bangun Ruang Prisma Segiempat :3")
            print ("1. Luas")
            print ("2. Volume")
            prisma =input("Silahkan Masukkan Pilihan Anda")
            if prisma == '1':
                print ("Anda Memilih Luas")
                luasprismasegiempat =lambda l,k,t:2*l*k*t
                la =int(input("Silahkan Masukkan Luas Alas Nya : "))
                ka =int(input("Silahkan Masukkan Keliling Alas Nya :"))
                t =int(input("Silahkan Masukkan Tinggi Nya :"))
                print (f"Luas Prisma SegiEmpat Adalah ={luasprismasegiempat(la,ka,t)}")
            elif prisma == '2':
                print ("Anda Memilih Volume")
                volumeprismasegiempat =lambda l,t:l*t
                la =int(input("Silahkan Masukkan Luas Alas Nya : "))
                t =int(input("Silahkan Masukkan Tinggi Nya :"))
                print (f"Volume Prisma Segiempat Adalah ={volumeprismasegiempat(la,t)}")
            else:
                print ("========================================")
                print ("====Data Yang Anda Input Tidak Valid====")
                print ("========================================")
                
        elif bangun == '10':
            print ("Anda Memilih Bangun Ruang Limas Segiempat :3")
            print ("1. Luas")
            print ("2. Volume")
            limas =input("Silahkan Masukkan Pilihan Anda :")
            if limas == '1':
                print ("Anda Memilih Luas")
                luaslimassegiempat =lambda k,s:k+0.5*k*s
                la =float(input("Silahkan Masukkan Luas Alas Nya :"))
                kl =float(input("Silahkan Masukkan Keliling Alas Nya :"))
                st =float(input("Silahkan Masukkan Sisi Tegak Nya : "))
                print (f"Luas Limas SegiEmpat Adalah ={luaslimassegiempat(la,kl,st)}")
            elif limas == '2':
                print ("Anda Memilih Volume")
                volumelimassegiempat =lambda l,t:1/3 *l*t
                la =float(input("Silahkan Masukkan Luas Alas Nya :"))
                tg =float(input("Silahkan Masukkan Tinggi Nya :"))
                print (f"Volume Limas SegiEmpat Adalah {volumelimassegiempat(la,tg)}")
            else:
                print ("========================================")
                print ("====Data Yang Anda Input Tidak Valid====")
                print ("========================================")
                
        elif bangun == '11':
            print ("Anda Memilih Bangun Ruang Silinder :3")
            print ("1. Luas")
            print ("2. Volume")
            silinder =input("Silahkan Masukkan Pilihan Anda : ")
            if silinder == '1':
                print ("Anda Memilih Luas")
                luassilinder = lambda r,t:2*phi*r*(r+t)
                jari_jari =float(input("Silahkan Masukkan Jari Jari Nya :"))
                tinggi =float(input("Silahkan Masukkan Tinggi Nya:"))
                print (f"Luas Silinder Adalah ={luassilinder(jari_jari,tinggi)}")
            elif silinder == '2':
                print ("Anda Memilh Volume")
                volume_silinder = lambda r,t:phi*r**2*t
                jari_jari =float(input("Silahkan Masukkan Jari Jari Nya :"))
                tinggi =float(input("Silahkan Masukkan Tinggi Nya:"))
                print (f"Luas Silinder Adalah ={volume_silinder(jari_jari,tinggi)}")
            else:
                print ("========================================")
                print ("====Data Yang Anda Input Tidak Valid====")
                print ("========================================")
                
        else :
            print ("========================================")
            print ("====Data Yang Anda Input Tidak Valid====")
            print ("========================================")

            
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
        print ("9. Segi Enam")
        
        datar =(input("Masukkan Pilihan Anda :"))
        
        if datar == '1':
            print ("Anda Memilih Bangun Datar Persegi <3")
            print ("1. Luas")
            print ("2. Keliling")
            persegi =input("Silahkan Masukkan Pilihan Anda :")
            if persegi == '1':
                print ("Anda Memlih Luas")
                luaspersegi =lambda s:s**2
                sisi =int(input("Silahkan Masukkan Sisi Nya :"))
                print (f"Luas Persegi Adalah ={luaspersegi(sisi)}")
            elif persegi == '2':
                print ("Anda Memilih Keliling")
                kelilingpersegi =lambda s:4*s
                sisi =int(input("Silahkan Masukkan Sisi Nya :"))
                print (f"Keliling Persegi Adalah ={kelilingpersegi(sisi)}")
            else:
                print ("========================================")
                print ("====Data Yang Anda Input Tidak Valid====")
                print ("========================================")
                
        elif datar == '2':
            print ("Anda Memilih Bangun Datar Persegi Panjang <3")
            print ("1. Luas")
            print ("2. Keliling")
            panjang =input("Silahkan Masukkan PIlihan Anda")
            if panjang == '1':
                print ("Anda Memilih Luas")
                luaspersegi =lambda p,l:p*l
                pj =int(input("Silahkan Masukkan Panjang Nya :"))
                lb =int(input("Silahkan Masukkan Lebar Nya : "))
                print (f"Luas Persegi Adalah ={luaspersegi(pj,lb)}")
            elif panjang == '2':
                print ("Anda Memilih Keliling")
                kelilingpersegi =lambda p,l:2*(p*l)
                pj =int(input("Silahkan Masukkan Panjang Nya :"))
                lb =int(input("Silahkan Masukkan Lebar Nya : "))
                print (f"Keliling Persegi Adalah ={kelilingpersegi (pj,lb)}")
            else:
                print ("========================================")
                print ("====Data Yang Anda Input Tidak Valid====")
                print ("========================================")
                
        elif datar =='3':
            print ("Anda Memilih Bangun Datar Segitiga")
            print ('1. Segitiga Sama Sisi')
            print ('2. Segitiga Sama Kaki')
            print ('3. Segitiga Sembarang')
            segitiga =(input("Masukkan Pilihan Anda :"))
            if pilihan == '1':
                print ("Anda Memilih Segitiga Sama Sisi")
                print ("1. Luas")
                print ("2. Keliling")
                segi =input("Silahkan Masukkan Pilihan Anda :")
                if segi == '1':
                    print ("Anda Memilih Luas")
                    luassegitigasamasisi =lambda a,t:0.5*alas*tinggi
                    alas =int(input("Silahkan Masukkan Alas Nya :"))
                    tinggi =int(input("Silahkan Masukkan Tinggi Nya :"))
                    print (f"Luas Segitiga Sama Sisi Adalah ={luassegitigasamasisi(alas,tinggi)}")
                elif segi == '2':
                    print ("Anda Memilih Keliling")
                    kelilingsegitigasamasisi =lambda s:s**3
                    sisi =int(input("Silahkan Masukkan Sisi Nya"))
                    print (f"Keliling Segitiga Sama Sisi Adalah ={kelilingsegitigasamasisi(sisi)}")
                else:
                    print ("========================================")
                    print ("====Data Yang Anda Input Tidak Valid====")
                    print ("========================================")
            elif pilihan == '2':
                print ("Anda Memilih Segitiga Sama Kaki")
                print ("1. Luas")
                print ("2. Keliling")
                segi =input("Silahkan Masukkan Pilihan Anda :")
                if segi == '1':
                    print ("Anda Memilih Luas")
                    luassegitgasamakaki =lambda a,t:0.5*a*t
                    alas =int(input("Silahkan Masukkan Alas Nya :"))
                    tinggi =int(input("Silahkan Masukkan Tinggi Nya :"))
                    print (f"Luas Segitiga Sama Kaki Adalah ={luassegitgasamakaki(alas,tinggi)}")
                elif segi == '2':
                    print ("Anda Memilih Keliling")
                    kelilingsegitigasamakaki =lambda s:s**3
                    sisi =int(input("Silahkan Masukkan Sisi Nya"))
                    print (f"Keliling Segitiga Sama Kaki Adalah ={kelilingsegitigasamakaki(sisi)}")
                else:
                    print ("========================================")
                    print ("====Data Yang Anda Input Tidak Valid====")
                    print ("========================================")
            elif pilihan == '3':
                print ("Anda Memilih Segitiga Sembarang")
                print ("1. Luas")
                print ("2. Keliling")
                segi =input("Silahkan Masukkan Pilihan Anda :")
                if segi == '1':
                    print ("Anda Memilih Luas")
                    luassegitigasembarang =lambda a,t:0.5*a*t
                    alas =int(input("Silahkan Masukkan Alas Nya :"))
                    tinggi =int(input("Silahkan Masukkan Tinggi Nya :"))
                    print (f"Luas Segitiga Sembarang Adalah ={luassegitigasembarang(alas,tinggi)}")
                elif segi == '2':
                    print ("Anda Memilih keliling")
                    kelilingsegitigasembarang =lambda sa,sb,sc:sa+sb+sc
                    sisia =int(input("Silahkan Masukkan SisiA Nya :"))
                    sisib =int(input("Silahkan Masukkan SisiB Nya :"))
                    sisic =int(input("Silahkan Masukkan SisiC Nya :"))
                    print (f"Keliling Segitiga Sembarang Adalah ={kelilingsegitigasembarang(sisia,sisib,sisic)}")
                else:
                    print ("========================================")
                    print ("====Data Yang Anda Input Tidak Valid====")
                    print ("========================================")
            else:
                print ("========================================")
                print ("====Data Yang Anda Input Tidak Valid====")
                print ("========================================")
                    
        elif datar == '4':
            print ("Anda Memilih Bangun Datar Trapesium <3")
            print ("1. Luas")
            print ("2. Keliling")
            trapesium =input("Silahkan Masukkan Pilihan Anda :")
            if trapesium == '1':
                print("Anda Memilih Luas")
                luastrapesium =lambda t,s:0.5*(s)*t
                tg =int(input("Silahkan Masukkan Tinggi Nya :"))
                sj =int(input("Silahkan Masukkan Sisi Sejajar Nya :"))
                print (f"Luas Trapesium Adalah ={luastrapesium(sj,tg)}")
            elif trapesium == '2':
                print ("Anda Memilih Keliling")
                kelilingtrapesium =lambda sa,sb,sc,sd:sa+sb+sc+sd
                sa =int(input("Silahkan Masukkan SisiA Nya :"))
                sb =int(input("Silahkan Masukkan SisiD Nya :"))
                sc =int(input("Silahkan Masukkan SisiC Nya :"))
                sd =int(input("Silahkan Masukkan SisiD Nya :"))
                print (f"Keliling Trapesium Adalah ={kelilingtrapesium(sa,sb,sc,sd)}")
            else:
                print ("========================================")
                print ("====Data Yang Anda Input Tidak Valid====")
                print ("========================================")
                
        elif datar == '5':
            print ("Anda Memilih Bangun Datar Jajar Genjang <3")
            print ("1. Luas")
            print ("2. Keliling")
            jajar =input("Silahkan Masukkan Pilihan Anda")
            if jajar == '1':
                print ("Anda Memilih Luas")
                luasjajargenjang =lambda a,t:a*t
                alas =int("Silahkan Masukkan Alas Nya :")
                tinggi =int("Silahkan Masukkan Tinggi Nya :")
                print (f"Luas JajarGenjang Adalah ={luasjajargenjang(alas,tinggi)}")
            elif jajar == '2':
                print ("Anda Memilih Keliling")
                kelilingjajargenjang =lambda s1,s2:2*(s1+s2)
                s1 =int(input("Silahkan Masukkan Sisi Sejajar 1 Nya :"))
                s2 =int(input("Silahkan Masukkan Sisi Sejajar 2 Nya :"))
                print (f"Keliling JajarGenjang Adalah ={kelilingjajargenjang(s1,s2)}")
            else:
                print ("========================================")
                print ("====Data Yang Anda Input Tidak Valid====")
                print ("========================================")
                
        elif datar == '6':
            print ("Anda Memilih Bangun Datar Lingkaran <3") 
            print ("1. Luas")
            print ("2. Keliling")
            lingkaran =input("Silahkan Masukkan Pilihan Anda :")
            if lingkaran == '1':
                print ("Anda Memilih Luas")
                luaslingkaran =lambda r:phi*r**2
                r =float(input("Silahkan Masukkan Jari Jari Nya :"))
                print (f"luas Lingkaran Adalah ={luaslingkaran(r)}")
            elif lingkaran == '2':
                print ("Anda Memilih Keliling")
                kelilinglingkaran =lambda r,d:2*r*d
                r =int(input("Silahkan Masukkan Jari Jari Nya :"))
                d =int(input("Silahkan Masukkan Diameter Nya :"))
                print (f"Keliling Lingkaran Adalah ={kelilinglingkaran(r,d)}")
            else:
                print ("========================================")
                print ("====Data Yang Anda Input Tidak Valid====")
                print ("========================================")
                
        elif datar == '7':
            print ("Anda Memilih Bangun Datar Layang Layang <3")
            print ("1. Luas")
            print ("2. Keliling")
            layang =input("Silahkan Masukkan Pilihan Anda :")
            if layang == '1':
                print ("Anda Memilih Luas")
                luaslayang =lambda d1,d2:0.5*(d1*d2)
                dg1 =int(input("Silahkan Masukkan Diagonal Pertama Nya :"))
                dg2 =int(input("Silahkan Masukkan Diagonal Kedua Nya :"))
                print (f"Luas Layang Adalah ={luaslayang (dg1,dg2)}")
            elif layang == '2' :
                print ("Anda Memilih Keliling")
                kelilinglayang =lambda p1,p2:2*(p1*p1)
                ps1 =int(input("Silahkan Masukkan Panjang Sisi Pertama Nya :"))
                ps2 =int(input("Silahkan Masukkan Panjang Sisi Kedua Nya"))
                print (f"Keliling Lingkaran Adalah ={kelilinglayang(ps1,ps2)}")
            else:
                print ("========================================")
                print ("====Data Yang Anda Input Tidak Valid====")
                print ("========================================")
                
        elif datar == '8':
            print ("Anda Memilih Bangun Datar Belah Ketupat <3")
            print ("1. Luas")
            print ("2. Keliling")
            ketupat =input("Silahkan Masukkan Pilihan Anda :")
            if ketupat == '1':
                print ("Anda Memilih Luas")
                luasbelahketupat =lambda d1,d2:(d1*d2)/2
                dg1 =int(input("Silahkan Masukkan Diagonal Pertama Nya :"))
                dg2 =int(input("Silahkan Masukkan Diagonal Kedua Nya :"))
                print (f"Luas Belah Ketupat Adalah ={luasbelahketupat (dg1,dg2)}")
            elif ketupat == '2':
                print ("Anda Memilih Keliling")
                kelilingbelahketupat =lambda s:4*sisi            
                sisi =int(input("Silahkan Masukkan Sisi Nya"))
                print (f"Keliling Belah Ketupat Adalah ={kelilingbelahketupat(sisi)}")
                
        elif datar == '9':
            print ("Anda Memilih Bangun Datar Segi Enam <3")
            print ("1. Luas")
            print ("2. Keliling")
            segienam =input("Silahkan Masukkan Pilihan Anda :")
            if segienam == '1':
                print ("Anda Memilih Luas")
                luassegienam =lambda a,s:(6*a*s)*0.5
                ampotem =float(input("Silahkan Masukkan Apotem Nya :"))
                sisi =float(input("Silahkan Masukkan Sisi Nya :"))
                print (f"Luas Segi Enam Adalah ={luassegienam(ampotem,sisi)}")
            elif segienam == '2':
                print ("Anda Memilih Keliling")
                kelilingsegienam =lambda s:6*s
                sisi =int(input("Silahkan Masukkan Panjang Sisi Nya :"))
                print (f"Keling Dari Segi Enam Adalah ={kelilingsegienam(sisi)}")
            else:
                print ("========================================")
                print ("====Data Yang Anda Input Tidak Valid====")
                print ("========================================")
                    
        else:
            print ("========================================")
            print ("====Data Yang Anda Input Tidak Valid====")
            print ("========================================")
                       
    # Konversi Satuan
    elif pilihan == '4':
        print("Anda Memilih Konversi Satuan :o")
        #Kode Konversi Satuan
        print ("1. Konversi Panjang")
        print ("2. Konversi Suhu")
        print ("3. Konversi Berat")
        print ("4. Konversi Volume")
        print ("5. Konversi Kecepatan")
        print ("6. Konversi Waktu")
        konversi =input("Masukkan Pilihan Anda :")
        
        if konversi == '1':
            print ("Anda Memilih Konversi Panjang :o")
            def meter_ke_kilometer(meter):
                return meter / 1000
            def meter_ke_sentimeter(meter):
                 return meter * 100
            def kilometer_ke_meter(kilometer):
                 return kilometer * 1000
            def kilometer_ke_mil(kilometer):
                 return kilometer * 0.621371
            def sentimeter_ke_meter(sentimeter):
                 return sentimeter / 100
            def sentimeter_ke_inci(sentimeter):
                 return sentimeter * 0.393701
            print("\nKalkulator Konversi Panjang:")
            print("1. Meter ke Kilometer")
            print("2. Meter ke Sentimeter")
            print("3. Kilometer ke Meter")
            print("4. Kilometer ke Mil")
            print("5. Sentimeter ke Meter")
            print("6. Sentimeter ke Inci")
            pilihan_menu = int(input("Masukkan Pilihan Anda: "))
    
            if pilihan_menu == 1:
                meter = float(input("Masukkan panjang dalam meter: "))
                kilometer = meter_ke_kilometer(meter)
                print(f"{meter} meter = {kilometer} kilometer")
            elif pilihan_menu == 2:
                meter = float(input("Masukkan panjang dalam meter: "))
                sentimeter = meter_ke_sentimeter(meter)
                print(f"{meter} meter = {sentimeter} sentimeter")
            elif pilihan_menu == 3:
                kilometer = float(input("Masukkan panjang dalam kilometer: "))
                meter = kilometer_ke_meter(kilometer)
                print(f"{kilometer} kilometer = {meter} meter")
            elif pilihan_menu == 4:
                kilometer = float(input("Masukkan panjang dalam kilometer: "))
                mil = kilometer_ke_mil(kilometer)
                print(f"{kilometer} kilometer = {mil} mil")
            elif pilihan_menu == 5:
                sentimeter = float(input("Masukkan panjang dalam sentimeter: "))
                meter = sentimeter_ke_meter(sentimeter)
                print(f"{sentimeter} sentimeter = {meter} meter")
            elif pilihan_menu == 6:
                sentimeter = float(input("Masukkan panjang dalam sentimeter: "))
                inci = sentimeter_ke_inci(sentimeter)
                print(f"{sentimeter} sentimeter = {inci} inci")
            else :
                print ("========================================")
                print ("====Data Yang Anda Input Tidak Valid====")
                print ("========================================")
                
        elif konversi == '2':
            print ("Anda Memilih Konversi Suhu :o")
            def celsius_ke_fahrenheit(celsius):
                return (celsius * 9/5) + 32

            def celsius_ke_kelvin(celsius):
                return celsius + 273.15
            def fahrenheit_ke_celsius(fahrenheit):
                return (fahrenheit - 32) * 5/9
            def fahrenheit_ke_kelvin(fahrenheit):
                return (fahrenheit - 32) * 5/9 + 273.15
            def kelvin_ke_celsius(kelvin):
                return kelvin - 273.15
            def kelvin_ke_fahrenheit(kelvin):
                return (kelvin - 273.15) * 9/5 + 32        
            print("\nKalkulator Konversi Suhu:")
            print("1. Celsius ke Fahrenheit")
            print("2. Celsius ke Kelvin")
            print("3. Fahrenheit ke Celsius")
            print("4. Fahrenheit ke Kelvin")
            print("5. Kelvin ke Celsius")
            print("6. Kelvin ke Fahrenheit")
            pilihan_menu = int(input("Masukkan Pilihan Anda: "))
            if pilihan_menu == 1:
                celsius = float(input("Masukkan suhu dalam Celsius: "))
                fahrenheit = celsius_ke_fahrenheit(celsius)
                print(f"{celsius} °C = {fahrenheit} °F")
            elif pilihan_menu == 2:
                celsius = float(input("Masukkan suhu dalam Celsius: "))
                kelvin = celsius_ke_kelvin(celsius)
                print(f"{celsius} °C = {kelvin} K")
            elif pilihan_menu == 3:
                fahrenheit = float(input("Masukkan suhu dalam Fahrenheit: "))
                celsius = fahrenheit_ke_celsius(fahrenheit)
                print(f"{fahrenheit} °F = {celsius} °C")
            elif pilihan_menu == 4:
                fahrenheit = float(input("Masukkan suhu dalam Fahrenheit: "))
                kelvin = fahrenheit_ke_kelvin(fahrenheit)
                print(f"{fahrenheit} °F = {kelvin} K")
            elif pilihan_menu == 5:
                kelvin = float(input("Masukkan suhu dalam Kelvin: "))
                celsius = kelvin_ke_celsius(kelvin)
                print(f"{kelvin} K = {celsius} °C")
            elif pilihan_menu == 6:
                kelvin = float(input("Masukkan suhu dalam Kelvin: "))
                fahrenheit = kelvin_ke_fahrenheit(kelvin)
                print(f"{kelvin} K = {fahrenheit} °F")
            else:
                print ("========================================")
                print ("====Data Yang Anda Input Tidak Valid====")
                print ("========================================")
                
        elif konversi == '3':
            print ("Anda Memilih Konversi Berat :o")
            def kilogram_ke_pon(kilogram):
                return kilogram * 2.20462
            def kilogram_ke_ons(kilogram):
                return kilogram * 35.27396
            def pon_ke_kilogram(pon):
                    return pon / 2.20462
            def ons_ke_kilogram(ons):
                return ons / 35.27396
            print("\nKalkulator Konversi Berat:")
            print("1. Kilogram ke Pon")
            print("2. Kilogram ke Ons")
            print("3. Pon ke Kilogram")
            print("4. Ons ke Kilogram")
            pilihan_menu = int(input("Masukkan Pilihan Anda: "))
            if pilihan_menu == 1:
                kilogram = float(input("Masukkan berat dalam kilogram: "))
                pon = kilogram_ke_pon(kilogram)
                print(f"{kilogram} kg = {pon} pon")
            elif pilihan_menu == 2:
                kilogram = float(input("Masukkan berat dalam kilogram: "))
                ons = kilogram_ke_ons(kilogram)
                print(f"{kilogram} kg = {ons} ons")
            elif pilihan_menu == 3:
                pon = float(input("Masukkan berat dalam pon: "))
                kilogram = pon_ke_kilogram(pon)
                print(f"{pon} pon = {kilogram} kg")
            elif pilihan_menu == 4:
                ons = float(input("Masukkan berat dalam ons: "))
                kilogram = ons_ke_kilogram(ons)
                print(f"{ons} ons = {kilogram} kg")
            else:
                print ("========================================")
                print ("====Data Yang Anda Input Tidak Valid====")
                print ("========================================")
            
        elif konversi == '4':
            print("Anda Memilih Konversi Volume :o")
            def liter_ke_galon(liter):
                return liter * 0.264172
            def liter_ke_meter_kubik(liter):
                return liter / 1000
            def galon_ke_liter(galon):
                return galon / 0.264172
            def meter_kubik_ke_liter(meter_kubik):
                return meter_kubik * 1000
            print("\nKalkulator Konversi Volume:")
            print("1. Liter ke Galon")
            print("2. Liter ke Meter Kubik")
            print("3. Galon ke Liter")
            print("4. Meter Kubik ke Liter")
            pilihan_menu = int(input("Masukkan Pilihan Anda: "))
            if pilihan_menu == 1:
                liter = float(input("Masukkan volume dalam liter: "))
                galon = liter_ke_galon(liter)
                print(f"{liter} liter = {galon} galon")
            elif pilihan_menu == 2:
                liter = float(input("Masukkan volume dalam liter: "))
                meter_kubik = liter_ke_meter_kubik(liter)
                print(f"{liter} liter = {meter_kubik} m³")
            elif pilihan_menu == 3:
                galon = float(input("Masukkan volume dalam galon: "))
                liter = galon_ke_liter(galon)
                print(f"{galon} galon = {liter} liter")
            elif pilihan_menu == 4:
                meter_kubik = float(input("Masukkan volume dalam meter kubik: "))
                liter = meter_kubik_ke_liter(meter_kubik)
                print(f"{meter_kubik} m³ = {liter} liter")
            else:
                print ("========================================")
                print ("====Data Yang Anda Input Tidak Valid====")
                print ("========================================")
                
        elif konversi == '5' :
            print ("Anda Memilih Konversi Kecepatan :o")
            def km_per_jam_ke_mph(km_per_jam):
                return km_per_jam * 0.621371
            def km_per_jam_ke_m_per_detik(km_per_jam):
                return km_per_jam * 1000 / 3600
            def mph_ke_km_per_jam(mph):
                return mph / 0.621371
            def m_per_detik_ke_km_per_jam(m_per_detik):
                return m_per_detik * 3600 / 1000
            print("\nKalkulator Konversi Kecepatan:")
            print("1. Kilometer per Jam ke Mil per Jam")
            print("2. Kilometer per Jam ke Meter per Detik")
            print("3. Mil per Jam ke Kilometer per Jam")
            print("4. Meter per Detik ke Kilometer per Jam")
            pilihan_menu = int(input("Masukkan Pilihan Anda: "))
            if pilihan_menu == 1:
                km_per_jam = float(input("Masukkan kecepatan dalam kilometer per jam: "))
                mph = km_per_jam_ke_mph(km_per_jam)
                print(f"{km_per_jam} km/h = {mph} mph")
            elif pilihan_menu == 2:
                km_per_jam = float(input("Masukkan kecepatan dalam kilometer per jam: "))
                m_per_detik = km_per_jam_ke_m_per_detik(km_per_jam)
                print(f"{km_per_jam} km/h = {m_per_detik} m/s")
            elif pilihan_menu == 3:
                mph = float(input("Masukkan kecepatan dalam mil per jam: "))
                km_per_jam = mph_ke_km_per_jam(mph)
                print(f"{mph} mph = {km_per_jam} km/h")
            elif pilihan_menu == 4:
                m_per_detik = float(input("Masukkan kecepatan dalam meter per detik: "))
                km_per_jam = m_per_detik_ke_km_per_jam(m_per_detik)
                print(f"{m_per_detik} m/s = {km_per_jam} km/h")
            else:
                print ("========================================")
                print ("====Data Yang Anda Input Tidak Valid====")
                print ("========================================")
                
        elif konversi == '6':
            print ("Anda Memilih Konversi Waktu :o")
            def jam_ke_menit(jam):
                return jam * 60
            def jam_ke_detik(jam):
                return jam * 3600
            def menit_ke_detik(menit):
                return menit * 60
            def menit_ke_jam(menit):
                return menit / 60
            def detik_ke_jam(detik):
                return detik / 3600
            def detik_ke_menit(detik):
                return detik / 60
            
            print ("\nKalkulator Konversi Waktu")
            print ("1. Jam Ke Menit")
            print ("2. Jam Ke Detik")
            print ("3. Menit Ke Detik")
            print ("4. Menit Ke jam")
            print ("5. Detik Ke Jam")
            print ("6. Detik Ke Menit")
            pilihan_menu =int(input("Silahkan Masukkan Pilihan Anda :"))

            if pilihan_menu == 1:
                jam =int(input("Masukkan jam ke menit :"))
                menit = jam_ke_menit(jam)
                print(f"{jam} jam = {menit} menit")
            elif pilihan_menu == 2:
                jam =int(input("Masukkan jam ke detik :"))
                detik =jam_ke_detik(jam)
                print (f"{jam} jam = {detik} detik")
            elif pilihan_menu == 3:
                menit =int(input("Masukkan menit ke detik :"))
                detik =menit_ke_detik(menit)
                print (f"{menit} menit = {detik} detik")
            elif pilihan_menu == 4:
                menit =float(input("Masukkan menit ke jam :"))
                jam =menit_ke_jam(menit)
                print (f"{menit} menit = {jam} jam")
            elif pilihan_menu == 5:
                detik =float(input("Masukkan detik ke jam :"))
                jam =detik_ke_jam(detik)
                print (f"{detik} detik = {jam} jam")
            elif pilihan_menu == 6:
                detik =float(input("Masukkan detik ke menit :"))
                menit =detik_ke_menit(detik)
                print (f"{detik} detik = {menit} menit")
            else:
                print ("========================================")
                print ("====Data Yang Anda Input Tidak Valid====")
                print ("========================================")
        else :
            print ("========================================")
            print ("====Data Yang Anda Input Tidak Valid====")
            print ("========================================")
                
    else :
        print("Pilihan tidak valid. Silakan coba lagi.")
    
    kembali = input("Ketik 'iya' untuk kembali atau 'keluar' untuk keluar: ")
    if kembali.lower() == 'keluar':
        print ("====================================================================")
        print("Terima Kasih Telah Menggunakan Kalkulator Saya :)")
        print("Maafkan Bila Ada Kurang Dan Salah Soalnya Masih Pelajar Juga :v")
        print("#SIBUK_BERKARYA😎😎😎😎")
        print ("-DERIANA MARUF")
        print ("====================================================================")
    break  # Keluar dari program jika pengguna memilih 'keluar' 