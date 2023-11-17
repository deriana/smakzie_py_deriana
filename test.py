awal = 1
akhir = 10
end = 0

while awal <= akhir:
    end += awal
    print (awal,end="")
    if awal < akhir:
        print (" + ", end="")
    awal += 1
print (f" = {end}")