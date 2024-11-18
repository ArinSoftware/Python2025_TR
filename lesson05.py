#DEĞİŞKENLER II (VARIABLES II)

#Değişken - Hafıza İlişkisi
num1 = 10
print(num1) #10
print(id(num1)) #140717020013768 (Değişebilir)

num2 = num1
print(num2) #10
print(id(num2))  #140717020013768 (Değişebilir)
# num1 ve num2 hafızada bulunan aynı 10 değerine referans verir

#Aynı değişkene farklı bir değer atanabilir.
x = 10
print(x) # 10
print(id(x)) #140717020013768

x = 'John'
print(x) #John
print(id(x)) #2260343042576 (Hafızadaki yer değişiyor)
#Python yeni bir string nesnesi oluşturulur.

#String veriler için tek ve çift tırnak kullanılabilir.
x = "John"
x = 'John'

#Değişken isimlendirme kuralları
#Değişken adı bir harfle yada altçizgi karakteriyle başlayabilir. name, _value uygundur
#Değişken adı sayı ile başlayamaz. 1name uygun değildir
#Değişken adları alfanümerik karakterler ve altçizgi içerebilir. (A-z, 0-9, ve _ ) 
#Değişken adları büyük/küçük harf duyarlıdır. Age, age değişkenleri farklıdır
#Değişken adları arasında boşluk bulunamaz. first_name (first name hatalıdır)
#Python anahtar kelimeleri değişken ismi olarak kullanılamaz.