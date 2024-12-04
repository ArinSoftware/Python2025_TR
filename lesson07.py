#Veri Tipleri II (Data Types II String - Boolean)

#String bir karakter dizisidir, indexlenebilir.
word = "Python"
print(word[0]) #P
print(word[1]) #y
print(word[-1]) #n

#Slicing - dilimleme
print(word[0:3]) #Pyt
print(word[1:3]) #yt
print(word[:3]) #Pyt
print(word[3:]) #hon
print(word[3:3]) #

#Python stringler için bir çok built-in (gömülü) metod barındırır.
print(word.upper()) #PYTHON
print(word.lower()) #python
print(word.title()) #Python

print(len(word)) #6

#Boolean ikili veri tipi
is_logged_in = True
if is_logged_in:
    print("Welcome")
else:
    print("Login")

#Karar ve karşılaştırma durumlarında kullanılır
print( 5>3 ) #True
print(2 == 3) #False