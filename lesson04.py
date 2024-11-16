##DEĞİŞKENLER I (VARIABLES I)

#Değişken oluşturma
name = 'John'
print(name) # John

age = 43
print(age) # 43

#Python birden fazla değişken atamayı destekler
is_married, num = True, 10
print(is_married, num) # True, 10

num1 = num2 = num3 = 100
print(num1, num2, num3) # 100, 100, 100

#Python'da bir değişkeni tanımlamadan önce kullanamayız
print(surname)
surname = 'Doe' # NameError: name 'surname' is not defined

#Neden değişkenlere ihtiyacımız var?
player_health = 100
player_gold = 10

#Canavar saldırısı
player_health = player_health - 30

#Bir altın satma
player_gold = player_gold - 1
player_health = player_health + 20

print(player_health, player_gold) # 90, 9

#Python'da yorum satırları

#Bu bir tek satırlık yorum

x = 5  # Bu bir satır içi yorum

#Bu
#birden fazla
#satırlık yorumdur

"""
docstring
çok satırlı yorum
çift tırnak ile
"""

'''
docstring
çok satırlı yorum
tek tırnak ile
'''


