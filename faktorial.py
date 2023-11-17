def faktorial (n) :
    if n <= 1:
        return 1
    else :
        return n *faktorial (n -1)
    
i = 0
n = int(input('berapa faktorial'))

while i<=n :
    print (i, '! = ', faktorial (i))
    i += 1