print("\033[92m=======================================")
print("Welcome To My Calculator Project\t")
print("-By Hideri :3")
print("=======================================")

while True:
    print("1. Kalkulator Bangun Ruang\t")
    print("2. Kalkulator Bangun Datar\t")
    print("3. Keluar\t")
    
    pilihan = int(input("Masukkan Pilihan Anda ="))
    
    if pilihan == 1:
        print ("=========================================")
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
        print ("=========================================")        
        phi =3.14
        bangun =(input("Masukkan Pilihan Anda : "))
        
        if bangun == '1':
            print ("=========================================")
            print ("Anda Memilih Bangun Ruang Kubus :3")
            print ("1. Luas")
            print ("2. Volume")
            print ("=========================================")
            kubus =input("Silahkan Masukkan Pilihan Anda :")
            if kubus == '1':
                print ("=========================================")
                print ("Anda Memilih Luas")
                print ("=========================================") 
                luaskubus =lambda s:6*s**2
                sisi =int(input("Silahkan Masukkan Sisi :"))
                print (f"Luas Kubus Adalah ={luaskubus(sisi)}")
            elif kubus == '2':
                print ("=========================================")
                print ("Anda Memilih Volume")
                print ("=========================================")
                volumekubus =lambda s:s**3
                sisi =int(input("Silahkan Masukkan Sisi :"))
                print (f"Volume Kubus Adalah ={volumekubus(sisi)}")
            else:
                print ("========================================")
                print ("====Data Yang Anda Input Tidak Valid====")
                print ("========================================")
                
        elif bangun == '2':
            print ("=========================================")
            print ("Anda Memilih Bangun Ruang Balok :3")
            print ("1. Luas")
            print ("2. Volume")
            print ("=========================================")
            balok =input("Silahkan Masukkan Pilihan Anda :")
            if balok == '1':
                print ("=========================================")
                print ("Anda Memilih luas")
                print ("=========================================")
                luasbalok =lambda p,l,t: 2*(p*l+p*t+t*l)
                panjang =int(input('Silahkan Masukkan Panjang Nya :'))
                lebar =int(input('Silahkan Masukkan Lebar Nya :'))
                tinggi =int(input('Silahkan Masukkan Tinggi Nya :'))
                print (f"Luas Balok Adalah ={luasbalok(panjang,lebar,tinggi)}")
            elif bangun == '2':
                print ("=========================================")
                print ("Anda Memilih Volume")
                print ("=========================================")
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
            print ("=========================================")
            print ("Anda Memilih Bangun Ruang Tabung :3")
            print ("1. Luas")
            print ("2. Volume")
            print ("=========================================")
            tabung =input("Silahkan Masukkan Pilihan Anda :")
            if tabung == '1':
                print ("=========================================")
                print ("Anda Memilih Luas")
                print ("=========================================")
                luastabung =lambda a,r,t: 2*phi*r*t+2*phi*r**2
                alas =float(input("Silahkan Masukkan Alas Nya : "))
                r =float(input("Silahkan Masukkan Jari Jari Nya :"))
                tinggi =float(input("Silahkan Masukkan Tinggi Nya :"))
                print (f"Luas Tabung Adalah ={luastabung(alas,r,tinggi)}")
            elif tabung == '2':
                print ("=========================================")
                print ("Anda Memilih Volume")
                print ("=========================================")
                volumetabung =lambda r,t:phi*r**2*t
                r =float(input("Silahkan Masukkan Jari Jari Nya :"))
                tinggi =float(input("Silahkan Masukkan Tinggi Nya :"))
                print (f"Volume Tabung Adalah ={volumetabung(r,tinggi)}")
            else:
                print ("========================================")
                print ("====Data Yang Anda Input Tidak Valid====")
                print ("========================================")
                
        elif bangun == '4':
            print ("=========================================")
            print ("Anda Memilih Bangun Ruang Kerucut :3")
            print ("1. Luas")
            print ("2. Volume")
            print ("=========================================")
            kerucut =input("Silahkan Masukkan Pilihan Anda :")
            if kerucut == '1':
                print ("=========================================")
                print ("Anda Memilih Luas")
                print ("=========================================")
                luaskerucut =lambda r,g:phi*r*(r+g)
                jari =float(input('Silahkan Masukkan Jari Jari Alas Nya :'))
                garis =float(input('Silahkan Masukkan Garis Pelukis Nya :'))
                print (f"Luas Kerucut Adalah ={luaskerucut(jari,garis,)}")
            elif kerucut == '2':
                print ("=========================================")
                print ("Anda Memilih Volume")
                print ("=========================================")
                volumekerucut =lambda r,t: (1/3)*phi*r**2*t
                jari =float(input('Silahkan Masukkan Jari Jari Alas Nya :'))
                tinggi =float(input('Silahkan Masukkan Tinggi Nya :'))
                print (f"Volume Kerucut Adalah ={volumekerucut(jari,tinggi)}")
            else:
                print ("========================================")
                print ("====Data Yang Anda Input Tidak Valid====")
                print ("========================================")
                
        elif bangun == '5' :
            print ("=========================================")
            print ("Anda Memilih Bangun Ruang Bola :3")
            print ("1. Luas")
            print ("2. Volume")
            print ("=========================================")
            bola =input("Silahkan Masukkan Pilihan Anda :")
            if bola ==  '1' :
                print ("=========================================")
                print ("Anda Memilih Luas")
                print ("=========================================")
                luasjari =lambda r:r*phi*r**2
                jari =float(input("Silahkan Masukkan Jari Jari Nya :"))
                print (f"Luas Bola Adalah {luasjari(jari)}")
            elif bola == '2' :
                print ("=========================================")
                print ("Anda Memilih Volume")
                print ("=========================================")
                volumejari =lambda r:(4/3)*phi*r**2
                jari =float(input("Silahkan Masukkan Jari Jari Nya :"))
                print (f"Volume Bola Adalah ={volumejari(jari)}")
            else:
                print ("========================================")
                print ("====Data Yang Anda Input Tidak Valid====")
                print ("========================================")
                    
        elif bangun == '6' :
            print ("=========================================")
            print ("Anda Memilih Bangun Ruang Prisma Segitiga :3")
            print ("1. Luas ")
            print ("2. Volume")
            print ("=========================================")
            prisma =input("Silahkan Masukkan Pilihan Anda")
            if prisma == '1':
                print ("=========================================")
                print ("Anda Memilih Luas")
                print ("=========================================")
                luasprismasegitiga =lambda l,k,t:2*(l)+(k*t)
                ls =float(input("Silahkan Masukkan Luas Segitiga Nya : "))
                ks =float(input("Silahkan Masukkan Keliling Segitiga Nya : "))
                tp =float(input("Silahkan Masukkan Tinggi Prisma Nya :"))
                print (f"Luas Prisma Segitiga Adalah ={luasprismasegitiga(ls,ks,tp)}")
            elif prisma == '2':
                print ("=========================================")
                print ("Anda Memilih Volume")
                print ("=========================================")
                volumeprismasegitiga =lambda l,t:l*t
                ls =float(input("Silahkan Masukkan Luas Segitiga Nya : "))
                tp =float(input("Silahkan Masukkan Tinggi Prisma Nya :"))
                print (f"Volume Prisma Segitiga Adalah ={volumeprismasegitiga(ls,tp)}")
            else:
                print ("========================================")
                print ("====Data Yang Anda Input Tidak Valid====")
                print ("========================================")
                    
        elif bangun == '7':
            print ("=========================================")
            print ("Anda Memilih Bangun Ruang Limas Segitiga :3")
            print ("1. Luas")
            print ("2. Volume")
            print ("=========================================")
            limas =input("Silahkan Masukkan Pilihan Anda :")
            if limas == '1':
                print ("=========================================")
                print ("Anda Memilih Luas")
                print ("=========================================")
                luaslimassegitiga =lambda la,ls: ls+3*la
                la =float(input("Silahkan Masukkan Luas Alas Nya :"))
                ls =float(input("Silahka Masukkan Luas Segitiga Nya :"))
                print (f"Luas Limas Segitiga Adalah ={luaslimassegitiga(la,ls)}")
            elif limas =='2':
                print ("=========================================")
                print ("Anda Memilih Volume")
                print ("=========================================")
                volumelimassegitiga =lambda l,t:(l*t)/3
                la =float(input("Silahkan Masukkan Luas Alas Nya :"))
                tl =float(input("Silahkan Masukkan Tinggi Limas Nya :"))
                print (f"Volume Limas Segitiga ={volumelimassegitiga(la,tl)}")
            else:
                print ("========================================")
                print ("====Data Yang Anda Input Tidak Valid====")
                print ("========================================")
                
        elif bangun == '8':
            print ("=========================================")
            print ("Anda Memilih Bangun Ruang Kubah :3")
            print ("1. Luas")
            print ("2. Volume")
            print ("=========================================")
            kubah =input("Silahkan Masukkan Pilihan Anda :")
            if kubah == '1':
                print ("=========================================")
                print ("Anda Memilih Luas")
                print ("=========================================")
                luaskubah =lambda s:6*s**2
                sisi =int(input("Silahkan Masukkan Panjang Sisi : "))
                print (f"Luas Kubah Adalah ={luaskubah(sisi)}")
            elif kubah == '2':
                print ("=========================================")
                print ("Anda Memilih Volume")
                print ("=========================================")
                volumekubah =lambda s:s**3
                sisi =int(input("Silahkan Masukkan Panjang Sisi : "))
                print (f"Volume Luas Kubah Adalah ={volumekubah(sisi)}")
            else:
                print ("========================================")
                print ("====Data Yang Anda Input Tidak Valid====")
                print ("========================================")
                
        elif bangun == '9':
            print ("=========================================")
            print ("Anda Memilih Bangun Ruang Prisma Segiempat :3")
            print ("1. Luas")
            print ("2. Volume")
            print ("=========================================")
            prisma =input("Silahkan Masukkan Pilihan Anda")
            if prisma == '1':
                print ("=========================================")
                print ("Anda Memilih Luas")
                print ("=========================================")
                luasprismasegiempat =lambda l,k,t:2*l*k*t
                la =int(input("Silahkan Masukkan Luas Alas Nya : "))
                ka =int(input("Silahkan Masukkan Keliling Alas Nya :"))
                t =int(input("Silahkan Masukkan Tinggi Nya :"))
                print (f"Luas Prisma SegiEmpat Adalah ={luasprismasegiempat(la,ka,t)}")
            elif prisma == '2':
                print ("=========================================")
                print ("Anda Memilih Volume")
                print ("=========================================")
                volumeprismasegiempat =lambda l,t:l*t
                la =int(input("Silahkan Masukkan Luas Alas Nya : "))
                t =int(input("Silahkan Masukkan Tinggi Nya :"))
                print (f"Volume Prisma Segiempat Adalah ={volumeprismasegiempat(la,t)}")
            else:
                print ("========================================")
                print ("====Data Yang Anda Input Tidak Valid====")
                print ("========================================")
                
        elif bangun == '10':
            print ("=========================================")
            print ("Anda Memilih Bangun Ruang Limas Segiempat :3")
            print ("1. Luas")
            print ("2. Volume")
            print ("=========================================")
            limas =input("Silahkan Masukkan Pilihan Anda :")
            if limas == '1':
                print ("=========================================")
                print ("Anda Memilih Luas")
                print ("=========================================")
                luaslimassegiempat =lambda k,s:k+0.5*k*s
                la =float(input("Silahkan Masukkan Luas Alas Nya :"))
                kl =float(input("Silahkan Masukkan Keliling Alas Nya :"))
                st =float(input("Silahkan Masukkan Sisi Tegak Nya : "))
                print (f"Luas Limas SegiEmpat Adalah ={luaslimassegiempat(la,kl,st)}")
            elif limas == '2':
                print ("=========================================")
                print ("Anda Memilih Volume")
                print ("=========================================")
                volumelimassegiempat =lambda l,t:1/3 *l*t
                la =float(input("Silahkan Masukkan Luas Alas Nya :"))
                tg =float(input("Silahkan Masukkan Tinggi Nya :"))
                print (f"Volume Limas SegiEmpat Adalah {volumelimassegiempat(la,tg)}")
            else:
                print ("========================================")
                print ("====Data Yang Anda Input Tidak Valid====")
                print ("========================================")
                
        elif bangun == '11':
            print ("=========================================")
            print ("Anda Memilih Bangun Ruang Silinder :3")
            print ("1. Luas")
            print ("2. Volume")
            print ("=========================================")
            silinder =input("Silahkan Masukkan Pilihan Anda : ")
            if silinder == '1':
                print ("=========================================")
                print ("Anda Memilih Luas")
                print ("=========================================")
                luassilinder = lambda r,t:2*phi*r*(r+t)
                jari_jari =float(input("Silahkan Masukkan Jari Jari Nya :"))
                tinggi =float(input("Silahkan Masukkan Tinggi Nya:"))
                print (f"Luas Silinder Adalah ={luassilinder(jari_jari,tinggi)}")
            elif silinder == '2':
                print ("=========================================")
                print ("Anda Memilh Volume")
                print ("=========================================")
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
    elif pilihan == 2:
        print ("=========================================")
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
        print ("=========================================")
        
        datar =(input("Masukkan Pilihan Anda :"))
        
        if datar == '1':
            print ("=========================================")
            print ("Anda Memilih Bangun Datar Persegi <3")
            print ("1. Luas")
            print ("2. Keliling")
            print ("=========================================")
            persegi =input("Silahkan Masukkan Pilihan Anda :")
            if persegi == '1':
                print ("=========================================")
                print ("Anda Memlih Luas")
                print ("=========================================")
                luaspersegi =lambda s:s**2
                sisi =int(input("Silahkan Masukkan Sisi Nya :"))
                print (f"Luas Persegi Adalah ={luaspersegi(sisi)}")
            elif persegi == '2':
                print ("=========================================")
                print ("Anda Memilih Keliling")
                print ("=========================================")
                kelilingpersegi =lambda s:4*s
                sisi =int(input("Silahkan Masukkan Sisi Nya :"))
                print (f"Keliling Persegi Adalah ={kelilingpersegi(sisi)}")
            else:
                print ("========================================")
                print ("====Data Yang Anda Input Tidak Valid====")
                print ("========================================")
                
        elif datar == '2':
            print ("=========================================")
            print ("Anda Memilih Bangun Datar Persegi Panjang <3")
            print ("1. Luas")
            print ("2. Keliling")
            print ("=========================================")
            panjang =input("Silahkan Masukkan PIlihan Anda")
            if panjang == '1':
                print ("=========================================")
                print ("Anda Memilih Luas")
                print ("=========================================")
                luaspersegi =lambda p,l:p*l
                pj =int(input("Silahkan Masukkan Panjang Nya :"))
                lb =int(input("Silahkan Masukkan Lebar Nya : "))
                print (f"Luas Persegi Adalah ={luaspersegi(pj,lb)}")
            elif panjang == '2':
                print ("=========================================")
                print ("Anda Memilih Keliling")
                print ("=========================================")
                kelilingpersegi =lambda p,l:2*(p*l)
                pj =int(input("Silahkan Masukkan Panjang Nya :"))
                lb =int(input("Silahkan Masukkan Lebar Nya : "))
                print (f"Keliling Persegi Adalah ={kelilingpersegi (pj,lb)}")
            else:
                print ("========================================")
                print ("====Data Yang Anda Input Tidak Valid====")
                print ("========================================")
                
        elif datar =='3':
            print ("=========================================")
            print ("Anda Memilih Bangun Datar Segitiga")
            print ('1. Segitiga Sama Sisi')
            print ('2. Segitiga Sama Kaki')
            print ('3. Segitiga Sembarang')
            print ("=========================================")
            segitiga =(input("Masukkan Pilihan Anda :"))
            if pilihan == '1':
                print ("=========================================")
                print ("Anda Memilih Segitiga Sama Sisi")
                print ("1. Luas")
                print ("2. Keliling")
                print ("=========================================")
                segi =input("Silahkan Masukkan Pilihan Anda :")
                if segi == '1':
                    print ("=========================================")
                    print ("Anda Memilih Luas")
                    print ("=========================================")
                    luassegitigasamasisi =lambda a,t:0.5*alas*tinggi
                    alas =int(input("Silahkan Masukkan Alas Nya :"))
                    tinggi =int(input("Silahkan Masukkan Tinggi Nya :"))
                    print (f"Luas Segitiga Sama Sisi Adalah ={luassegitigasamasisi(alas,tinggi)}")
                elif segi == '2':
                    print ("=========================================")
                    print ("Anda Memilih Keliling")
                    print ("=========================================")
                    kelilingsegitigasamasisi =lambda s:s**3
                    sisi =int(input("Silahkan Masukkan Sisi Nya"))
                    print (f"Keliling Segitiga Sama Sisi Adalah ={kelilingsegitigasamasisi(sisi)}")
                else:
                    print ("========================================")
                    print ("====Data Yang Anda Input Tidak Valid====")
                    print ("========================================")
            elif pilihan == '2':
                print ("=========================================")
                print ("Anda Memilih Segitiga Sama Kaki")
                print ("1. Luas")
                print ("2. Keliling")
                print ("=========================================")
                segi =input("Silahkan Masukkan Pilihan Anda :")
                if segi == '1':
                    print ("=========================================")
                    print ("Anda Memilih Luas")
                    print ("=========================================")
                    luassegitgasamakaki =lambda a,t:0.5*a*t
                    alas =int(input("Silahkan Masukkan Alas Nya :"))
                    tinggi =int(input("Silahkan Masukkan Tinggi Nya :"))
                    print (f"Luas Segitiga Sama Kaki Adalah ={luassegitgasamakaki(alas,tinggi)}")
                elif segi == '2':
                    print ("=========================================")
                    print ("Anda Memilih Keliling")
                    print ("=========================================")
                    kelilingsegitigasamakaki =lambda s:s**3
                    sisi =int(input("Silahkan Masukkan Sisi Nya"))
                    print (f"Keliling Segitiga Sama Kaki Adalah ={kelilingsegitigasamakaki(sisi)}")
                else:
                    print ("========================================")
                    print ("====Data Yang Anda Input Tidak Valid====")
                    print ("========================================")
            elif pilihan == '3':
                print ("=========================================")
                print ("Anda Memilih Segitiga Sembarang")
                print ("1. Luas")
                print ("2. Keliling")
                print ("=========================================")
                segi =input("Silahkan Masukkan Pilihan Anda :")
                if segi == '1':
                    print ("=========================================")
                    print ("Anda Memilih Luas")
                    print ("=========================================")
                    luassegitigasembarang =lambda a,t:0.5*a*t
                    alas =int(input("Silahkan Masukkan Alas Nya :"))
                    tinggi =int(input("Silahkan Masukkan Tinggi Nya :"))
                    print (f"Luas Segitiga Sembarang Adalah ={luassegitigasembarang(alas,tinggi)}")
                elif segi == '2':
                    print ("=========================================")
                    print ("Anda Memilih keliling")
                    print ("=========================================")
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
            print ("=========================================")
            print ("Anda Memilih Bangun Datar Trapesium <3")
            print ("1. Luas")
            print ("2. Keliling")
            print ("=========================================")
            trapesium =input("Silahkan Masukkan Pilihan Anda :")
            if trapesium == '1':
                print ("=========================================")
                print("Anda Memilih Luas")
                print ("=========================================")
                luastrapesium =lambda t,s:0.5*(s)*t
                tg =int(input("Silahkan Masukkan Tinggi Nya :"))
                sj =int(input("Silahkan Masukkan Sisi Sejajar Nya :"))
                print (f"Luas Trapesium Adalah ={luastrapesium(sj,tg)}")
            elif trapesium == '2':
                print ("=========================================")
                print ("Anda Memilih Keliling")
                print ("=========================================")
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
            print ("=========================================")
            print ("Anda Memilih Bangun Datar Jajar Genjang <3")
            print ("1. Luas")
            print ("2. Keliling")
            print ("=========================================")
            jajar =input("Silahkan Masukkan Pilihan Anda")
            if jajar == '1':
                print ("=========================================")
                print ("Anda Memilih Luas")
                print ("=========================================")
                luasjajargenjang =lambda a,t:a*t
                alas =int("Silahkan Masukkan Alas Nya :")
                tinggi =int("Silahkan Masukkan Tinggi Nya :")
                print (f"Luas JajarGenjang Adalah ={luasjajargenjang(alas,tinggi)}")
            elif jajar == '2':
                print ("=========================================")
                print ("Anda Memilih Keliling")
                print ("=========================================")
                kelilingjajargenjang =lambda s1,s2:2*(s1+s2)
                s1 =int(input("Silahkan Masukkan Sisi Sejajar 1 Nya :"))
                s2 =int(input("Silahkan Masukkan Sisi Sejajar 2 Nya :"))
                print (f"Keliling JajarGenjang Adalah ={kelilingjajargenjang(s1,s2)}")
            else:
                print ("========================================")
                print ("====Data Yang Anda Input Tidak Valid====")
                print ("========================================")
                
        elif datar == '6':
            print ("=========================================")
            print ("Anda Memilih Bangun Datar Lingkaran <3") 
            print ("1. Luas")
            print ("2. Keliling")
            print ("=========================================")
            lingkaran =input("Silahkan Masukkan Pilihan Anda :")
            if lingkaran == '1':
                print ("=========================================")
                print ("Anda Memilih Luas")
                print ("=========================================")
                luaslingkaran =lambda r:phi*r**2
                r =float(input("Silahkan Masukkan Jari Jari Nya :"))
                print (f"luas Lingkaran Adalah ={luaslingkaran(r)}")
            elif lingkaran == '2':
                print ("=========================================")
                print ("Anda Memilih Keliling")
                print ("=========================================")
                kelilinglingkaran =lambda r,d:2*r*d
                r =int(input("Silahkan Masukkan Jari Jari Nya :"))
                d =int(input("Silahkan Masukkan Diameter Nya :"))
                print (f"Keliling Lingkaran Adalah ={kelilinglingkaran(r,d)}")
            else:
                print ("========================================")
                print ("====Data Yang Anda Input Tidak Valid====")
                print ("========================================")
                
        elif datar == '7':
            print ("=========================================")
            print ("Anda Memilih Bangun Datar Layang Layang <3")
            print ("1. Luas")
            print ("2. Keliling")
            print ("=========================================")
            layang =input("Silahkan Masukkan Pilihan Anda :")
            if layang == '1':
                print ("=========================================")
                print ("Anda Memilih Luas")
                print ("=========================================")
                luaslayang =lambda d1,d2:0.5*(d1*d2)
                dg1 =int(input("Silahkan Masukkan Diagonal Pertama Nya :"))
                dg2 =int(input("Silahkan Masukkan Diagonal Kedua Nya :"))
                print (f"Luas Layang Adalah ={luaslayang (dg1,dg2)}")
            elif layang == '2' :
                print ("=========================================")
                print ("Anda Memilih Keliling")
                print ("=========================================")
                kelilinglayang =lambda p1,p2:2*(p1*p1)
                ps1 =int(input("Silahkan Masukkan Panjang Sisi Pertama Nya :"))
                ps2 =int(input("Silahkan Masukkan Panjang Sisi Kedua Nya"))
                print (f"Keliling Lingkaran Adalah ={kelilinglayang(ps1,ps2)}")
            else:
                print ("========================================")
                print ("====Data Yang Anda Input Tidak Valid====")
                print ("========================================")
                
        elif datar == '8':
            print ("=========================================")
            print ("Anda Memilih Bangun Datar Belah Ketupat <3")
            print ("1. Luas")
            print ("2. Keliling")
            print ("=========================================")
            ketupat =input("Silahkan Masukkan Pilihan Anda :")
            if ketupat == '1':
                print ("=========================================")
                print ("Anda Memilih Luas")
                print ("=========================================")
                luasbelahketupat =lambda d1,d2:(d1*d2)/2
                dg1 =int(input("Silahkan Masukkan Diagonal Pertama Nya :"))
                dg2 =int(input("Silahkan Masukkan Diagonal Kedua Nya :"))
                print (f"Luas Belah Ketupat Adalah ={luasbelahketupat (dg1,dg2)}")
            elif ketupat == '2':
                print ("=========================================")
                print ("Anda Memilih Keliling")
                print ("=========================================")
                kelilingbelahketupat =lambda s:4*sisi            
                sisi =int(input("Silahkan Masukkan Sisi Nya"))
                print (f"Keliling Belah Ketupat Adalah ={kelilingbelahketupat(sisi)}")
                
        elif datar == '9':
            print ("=========================================")
            print ("Anda Memilih Bangun Datar Segi Enam <3")
            print ("1. Luas")
            print ("2. Keliling")
            print ("=========================================")
            segienam =input("Silahkan Masukkan Pilihan Anda :")
            if segienam == '1':
                print ("=========================================")
                print ("Anda Memilih Luas")
                print ("=========================================")
                luassegienam =lambda a,s:(6*a*s)*0.5
                ampotem =float(input("Silahkan Masukkan Apotem Nya :"))
                sisi =float(input("Silahkan Masukkan Sisi Nya :"))
                print (f"Luas Segi Enam Adalah ={luassegienam(ampotem,sisi)}")
            elif segienam == '2':
                print ("=========================================")
                print ("Anda Memilih Keliling")
                print ("=========================================")
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
            
    elif pilihan == 3:
        print ("====================================================================")
        print("Terima Kasih Telah Menggunakan Kalkulator Saya :)")
        print("Maafkan Bila Ada Kurang Dan Salah Soalnya Masih Pelajar Juga :v")
        print("#SIBUK_BERKARYA😎😎😎😎")
        print ("-DERIANA MARUF")
        print ("====================================================================")
        break
    
    else:
        print ("=====================================")
        print ("=========Authentication Eror=========")
        print ("=====================================")
    
    kembali = input("Ketik 'apapun' untuk kembali atau 'keluar' untuk keluar [Yakin mau keluar :((( ] : ")
    if kembali.lower() == 'keluar':
        print ("====================================================================")
        print("Terima Kasih Telah Menggunakan Kalkulator Saya :)")
        print("Maafkan Bila Ada Kurang Dan Salah Soalnya Masih Pelajar Juga :v")
        print("#SIBUK_BERKARYA😎😎😎😎")
        print ("-DERIANA MARUF")
        print ("====================================================================")
        break