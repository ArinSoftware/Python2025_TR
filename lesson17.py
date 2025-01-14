#IF - ELSE Koşullu İfadeler

#Temel IF Koşulu
x = 10
if x > 5:
    print("x is greater than 5")

#IF - ELSE
x = 3
if x > 5:
    print("x is greater than 5")
else:
    print("x is smaller than 4")

#IF -ELIF - ELSE
x = 5
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equals to 5")
else:
    print("x is smaller than 5")

#Nested IF
x = 10
if x > 5:
    if x % 2 == 0:
        print("x is greater than 5 and even")

#Shorthand ternary
x = 10
result = "even" if x % 2 == 0 else "odd"

#break ve continue ifadeleri
for num in range(1, 10):
    if num == 5:
        continue #bu iterasyonu atla
    print(num) 

for num in range(1, 10):
    if num == 5:
        break #döngüden çıkış
    print(num) 

#pass
n = 20
if n > 10:
    pass #yer tutucu
