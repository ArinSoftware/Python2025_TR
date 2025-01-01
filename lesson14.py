#Python Liste (List)

#Liste Oluşturma
empty_list = []
nums = [3,6,5,4]
mixed_list = ["tokyo", 4, True, 3.14]
nested_list = [[1,2], [3,4]]

#Liste elemanlarına ulaşmak
cities = ["barcelona", "roma", "istanbul", "moskova", "tahran"]
cities[0] #barcelona
cities[-2] #moskova

#Liste dilimleme (slicing)
cities[1:3] # [roma, istanbul]
cities[1:] # [roma, istanbul, moskova, tahran]

#Liste metodları
cities.append(10) # [barcelona, roma, istanbul, moskova, tahran, 10]
print(cities.count("barcelona")) # 1

#Metodları incelemek bilgi almak
print(dir(list))
help(list.count)

l1 = ["a", "b", "c", "d"]
l1.pop(1)
print(l1) # ['a', 'c', 'd']

l1.remove('c')
print(l1) # ['a', 'd']

l1.insert(0, "test")
print(l1) # ['test', 'a', 'd']

l1.extend([1, 2])
print(l1) # ['test', 'a', 'd', 1, 2]