#Tulis Angka 1500 + 2700 yang bisa dibagi 5 dan 7
#Tulis Program dengan Construct * dengan loop

for x in range(1500, 2700):
    if x%7 == 0 and x%5 == 0:
        print(x)

n =int(input("Silahkan Masukkan Baris Yang Anda Mau :"))
tipe =str(input("Silahkan Masukkan Bentuk Data/Tampilan Data :"))

for i in range(1,n):
    print('*' * i)
for i in range(n - 1, 0, -1):
    print('*' * i)

n =int(input("Silahkan Masukkan Baris Yang Anda Mau :"))
tipe =str(input("Silahkan Masukkan Bentuk Data/Tampilan Data:"))

for i in range(0, n + 1):
    for j in range(n - i):
        print(' ', end='')
    for k in range(2 * i - 1):
        print(tipe , end='')
    print()