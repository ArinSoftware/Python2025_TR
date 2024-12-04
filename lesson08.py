#Veri Tipleri III (Data Types III Integer - Float)

#INT, tam sayı değerlerini ifade eder.
num1 = 10
num2 = -10
num3 = 0

print(type(num1), type(num2), type(num3))

#FLOAT, tam sayı değerlerini ifade eder.
num4 = 3.14
num5 = -3.14
num6 = 3.0

print(type(num4), type(num5), type(num6))

#ilgili metodları görebilmek için
print(dir(int))
print(dir(float))

#help kullanımı
help(int.is_integer())

#as integer ration
num7 = 0.75
print(num7.as_integer_ratio()) # (3, 4)

#Float hassasiyet
print(0.1 + 0.2) #0.30000000004