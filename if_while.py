# #Short Hand Statement
# a = 10
# b = 20
# if a < b: print("Aku Kaya")
# a = 200     
# b = 330
# print("A") if a > b else print("B")
# a = 330
# b = 330
# print("A") if a > b else print("=") if a == b else print("B")

# a =int,input("Masukkan")
# b =int,input("Masukkan")

# if not a > b: print("Aku Kaya")

# a = 10
# b = 12

# if a != b: print ("Tidak Sama")

# x = 41

# if x > 10:
#     print ("Above Ten")
#     if x > 20:
#         print ("Anda Also Above 20")
#     else :
#         print ("but no above 20")
# a = 33
# b = 200

# if b > a:
#   pass  
#While And For

count = 0
while count <= 100:
    print(f"Perulangan ke-{count}")
    count += 1
    
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
i = 1
while i < 6:
  print(i)
  i += 1    
else:
  print("i tidak lebih dari 6")