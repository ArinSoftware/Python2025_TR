#print() - input() - f-string

#print() kullanımı

print("Heelo World")
print(12)
print(5 + 8)

#print() - değişken kullanımı
name = "Ahmet"
age = 21
print("My name is:", name, "and I am", age, "years old")

#intput() kullanımı
name = input("Enter your name")
print("Hello", name)

num1 = int(input("Enter first number"))
num2 = int(input("Enter second num"))
print("Sum:", num1 + num2)

#F-String (formatted string) kullanımı
name = "Ahmet"
age = 21
greeting = f"My name is {name} and I am {age} years old."
print(greeting)

a = 10
b = 5
result = f"{a} + {b} = {a + b}"
print(result)

PI = 3.14159265
formmatted_PI = f"Pi: {PI:.2f}"
print("for", formmatted_PI)

name = "Ahmet"
formatted_name = f"Name: {name.capitalize()}"
