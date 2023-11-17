while True:
    
    teks =str(input("Masukkan Kata Yang Mau DiReverse/Tidak :"))
    pilihan =str(input("Apakah Mau Diulang (Y/N) :"))
    
    if pilihan == 'Y' or 'y':
        print ("Diulang")
        print (len(teks)) 
        for x in range(len(teks)-1,-1,-1):
            print (teks[x],end="")
    elif pilihan == 'N' or 'n':
        print ("Tidak Diulang")
        print (teks)
    else:
        break