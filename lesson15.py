#Python Liste II (List II)
l1 = [1,2,3]
print(l1)
print(id(l1))

l1.append(4)
print(l1)
print(id(l1))

#Python listeleri değiştirilebilir (Mutable)

#Strings - Tuple - Boolean - Integer - Float (Immutable)
#List - Dictionary - Set (Mutable)

cities = ["barcelona", "tokyo", "istanbul"]
print(len(cities)) #3
print(cities[4]) #Index Error

#sort vs sorted

#sort() metodu bir listenin yerinde sıralanmasını sağlar. 
numbers = [5, 2, 9, 1, 7]
numbers.sort()  # Orijinal listeyi artan sıraya göre sıralar
print(numbers)  # [1, 2, 5, 7, 9]

#sorted
#sorted(), bir diziyi sıralanmış bir kopyasını oluşturur. Orijinal liste değiştirilmez.
numbers = [5, 2, 9, 1, 7]
sorted_numbers = sorted(numbers)  # Yeni bir sıralanmış liste döner
print(sorted_numbers)  # [1, 2, 5, 7, 9]
print(numbers)  # Orijinal liste değişmez: [5, 2, 9, 1, 7]


