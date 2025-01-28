#Dictionary (Sözlük) Python

person = {
    'name': 'Arin',
    'city': 'Balıkesir'
}

print(person)
print(type(person))

#Python dictionary karışık veri tiplerini barındırabilirler.

data = {
    'integer': 100,
    'boolean': True,
    'list': [1,2,3],
    'nested_dict': {'a': 1, 'b': 2}
}

#Dictionary keyleri immutable veri tiplerinden oluşur.

nums = {
    1: 'one',
    2: 'two',
    3: 'three'
}

#Dictionary dict() constructor fonksiyonu da kullanılarak oluşturulabilir.
person = dict(name = 'Arin', age = 10, city = 'Balıkesir')

#boş empty dictionary
person = {}

#key - value çifti eklemek
person['name'] = 'Arin'
person['age'] = 10

#dictionary elemanlarına ulaşmak
print(person['name']) # 'Arin
print(person['city']) # KeyError

#get() safe access kullanımı
print(person.get('city', 'Not Found'))

#dictionary elemanlarını güncellemek
person['age'] = 11
person['city'] = 'İstanbul'

#update()
#dictionary i, güncellemek istediği dictionary ile merge işlemine sokuyor
person.update({'age':12, 'city': 'Ankara'})
print(person)

#dictionary elemenlarının silinmesi
# del
del person['city']

# pop()
removed_value = person.pop('age')
print(removed_value)
print(person)

#popitem()
last_item = person.popitem()
print(last_item)
print(person)

#clear()
person.clear()