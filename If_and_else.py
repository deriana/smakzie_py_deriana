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

while True:
    print("\nKalkulator Konversi Panjang:")
    print("1. Meter ke Kilometer")
    print("2. Meter ke Sentimeter")
    print("3. Kilometer ke Meter")
    print("4. Kilometer ke Mil")
    print("5. Sentimeter ke Meter")
    print("6. Sentimeter ke Inci")
    print("7. Keluar")
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
    elif pilihan_menu == 7:
        break
    else:
        print("Pilihan menu tidak valid.")
