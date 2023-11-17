#type data
#tipe data : Angka satuan yang gak ada 
# koma nya (integer)
data_integer = 11
print ("data : ", data_integer)
print ("- bertipe : ", type(data_integer))

#tipe data :Angka dengan koma (float)
data_float = 1.5
print ("data : ", data_float)
print ("- bertipe : ", type(data_float))

#tipe data :Kumpulan karakter (string)
data_string = "Asep"
print ("data : ", data_string)
print ("- bertipe : ", type(data_string))

#tipe data :Biner dengan true/false (boolean)
data_bool = True
print ("data : ", data_bool)
print ("- bertipe : ", type(data_bool))

data_bool = False
print ("data : ", data_bool)
print ("- bertipe : ", type(data_bool))

#tipe data :khusus 
#bilangan complex
data_complex = complex(5,5)
print ("data : ", data_complex)
print ("- bertipe : ", type(data_complex))

#tipe data dari bahasa c
from ctypes import c_double

data_c_double = c_double(10,5)
print ("data : ", data_c_double)
print ("- bertipe : ", type(data_c_double))