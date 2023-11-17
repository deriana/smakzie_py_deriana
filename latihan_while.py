#tuliskan bilangan genap 0 - 100

x = 0
while x <= 100:
    print (x, end=" ")
    x += 2
#tuliskan bilangan kelipatan 5 dan 20 dari 0 sampai 100
x = 0
while 100 >= x:
    if x %5 == 0 and x %20 == 0:
        print (x,end=" ")
    x += 1
#tuliskan jumlah deret 1 - 10
i = 1
end = 10
total = 0
while i <= end:
    total += i
    print (i, end="")
    if i < end:
        print (" + ",end="")
    i =i + 1
print (" = ", total)
#tuliskan perkalian 1 sampai 10
i = 1
end = 20
while i <= end:
    print (f"{i} x {i} = {i*(i+1)}")
    i += 1