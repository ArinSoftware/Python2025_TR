#Dictionary (Sözlük) II

student = {
    'name': 'Elis',
    'age': 8,
    'courses': ['Math', 'Physics', 'Chemistry']
}

#For loop key
for key in student: #for key in student.keys():
    print(key)

#For loop value
for value in student.values():
    print(value)

#For loop key - value
for key, value in student.items():
    print(f"{key} - {value}")

print(dir(dict))
help(dict.pop)

#copy() method "shallow" yüzeysel kopya oluşturur
original = {'name': 'Alice', 'age': 25}
copy_dict = original.copy()

copy_dict['age'] = 30 #original dictionary değişmez.

#fromkeys()
keys = ['name', 'age', 'city']
default_value = 'unknown'
new_dict = dict.fromkeys(keys, default_value)

#Nested dictionary
employee = {
    'name': 'John',
    'contact': {
        'email': 'john@email.com',
        'phone': '111 222 333'
    }
}

print(employee['contact']['email']) #john@email.com