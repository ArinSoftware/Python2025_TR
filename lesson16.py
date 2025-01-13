#For - While Döngüler (Loops)

cities = ["barcelona", "tiflis", "moskova"]

for city in cities:
    print(city)     # Indentation (girinti) önemlidir.

#Indentation (girinti): Bir satırın veya bir grup satırın, kodun geri
#kalanıyla ilişkisini belirlemek için kullanılır.

#for döngüsü sadece listeler için değil sequence (dizi)
#yapıların tamamında kullanılır. (list, tuple, string, range())

for i in range(5): #range fonksiyonu sayılardan oluşan bir dizi oluşturur.
    print(i)

for char in "Python":
    print(char)

#Nested Loop
outer_list = ['A', 'B', 'C']
inner_list = [1, 2, 3]

for outer in outer_list:
    for inner in inner_list:
        print(f"Outer: {outer}, Inner: {inner}")

#While döngüsü koşul doğru olduğu sürece devam eder

count = 0
while count < 5:
    print(count)
    count +=1

#range(start, stop, step)

for i in range(1, 10, 2):  #1,3,5,7,9
    print(i)

#range() ile list oluşturmak
nums = list(range(1,6))
print(nums)