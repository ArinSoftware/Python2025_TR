#VERİ TİPLERİ I (DATA TYPES I)

book_count = 25
print(type(book_count)) #<class 'int'>

book_price = 19.94
print(type(book_price)) #<class 'float'>

book_name = "Clean Code"
print(type(book_name)) #<class 'str'>

is_available = True
print(type(is_available)) #<class 'bool'>

#Aynı değerler farklı veri tilerine sahip olabilirler.
val1 = "123"
val2 = 123
val3 = 123.0
print(type(val1)) #<class 'str'>
print(type(val2)) #<class 'int'>
print(type(val3)) #<class 'float'>

#Bir değerin tipi onun özelliklerini ve onunla ilgili yapabileceğimiz işlemleri belirler
name = "python"
print(name.upper()) #PYTHON
num = 10
print(num.upper()) #Error!

#Pythonda herşeyin bir tipi vardır. Çünkü Python da her şey bir nesnedir.
print(type(print)) # <class 'builtin_function_or_method'>





