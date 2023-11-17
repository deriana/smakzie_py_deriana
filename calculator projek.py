print("=======================================")
print("Welcome To My Calculator Project :3")
print("-By Hideri")
print("=======================================")

while True:
    print("1. Kalkulator Biasa")
    print("2. Kalkulator Bangun Ruang")
    print("3. Kalkulator Bangun Datar")
    print("4. Konversi Satuan")
    print("5. Con Sin Tan")
    print('6. Keluar')

    pilihan = input("Masukkan Pilihan Anda =")

    if pilihan == '6':
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
        print ("1. Konversi Panjang")
        print ("2. Konversi Suhu")
        print ("3. Konversi Berat")
        print ("4. Konversi Volume")
        print ("5. Konversi Kecepatan")
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
            pilihan_menu = int(input("Masukkan nomor menu: "))
    
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
                print("Data Yang Anda Input Tidak Valid")
        if konversi == '2':
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
            pilihan_menu = int(input("Masukkan nomor menu: "))
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
        if konversi == '3':
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
            pilihan_menu = int(input("Masukkan nomor menu: "))
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
        if konversi == '4':
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
            pilihan_menu = int(input("Masukkan nomor menu: "))
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
        if konversi == '5' :
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
            pilihan_menu = int(input("Masukkan nomor menu: "))
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
    else :
        print("Pilihan tidak valid. Silakan coba lagi.")
    kembali = input("Ketik 'iya' untuk kembali atau 'keluar' untuk keluar: ")
    
    if kembali.lower() == 'keluar':
        print("Terima Kasih Telah Menggunakan Kalkulator Saya :)")
        print("Maafkan Bila Ada Kurang Dan Salah Soalnya Masih Pelajar Juga :v")
        print("#MASIH_BERKARYA")
        print ("DERIANA MARUF")
        break  # Keluar dari program jika pengguna memilih 'keluar 
    if pilihan == '5':
        print ("Anda Memilih Sin Cos Tan")
        print ("1. Sin")
        print ("2. Cos")
        print ("3. Tan")
        math =input("Masukkan Pilihan Anda : ")
            