#konversi suhu
print ("Konversi Suhu")
def farenheit_ke_celcius (farenheit):
    return (farenheit - 32) * 5/9
def celcius_ke_farenheit (celcius):
    return (celcius * 9/5) +32

print ("1. Farenheit Ke Celcius")
print ("2. Celcius Ke Farenheit")
suhu = int(input ("Masukkan Pilihan :"))
if suhu == 1:
    suhu =float(input("Masukkan suhu dalam farenheit  :"))
    farenheit = (farenheit_ke_celcius(suhu))
    print (f"{suhu} °F = {farenheit} °C")
elif suhu == 2:
    suhu = float(input("Masukkan suhu dalam Celcius  :"))
    celcius = (celcius_ke_farenheit(suhu))
    print (f"{suhu} °C = {celcius} °F")
else:
    print ("====")
    print ("Eror")
    print ("====")