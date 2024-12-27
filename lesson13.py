""" 1
Vücut kitle endeksi hesaplama agirlik (kg)/ (boy (m) karesi) 
agirlik ve boy kullanicidan alinacak.

weight = float(input("Enter your wight (kg): "))
height = float(input("Enter your height (m): "))

bmi = weight / ( height ** 2)

print(f"Your BMI is: {bmi:.2f}")
"""

""" 2
daire alani ve çevresini yaricapi kullanicidan alarak yaziniz. PI = 3.14159
radius = float(input("Enter radius: "))
PI = 3.14159

area, circumference = PI * (radius ** 2), 2 * PI * radius
print(f"Area: {area:.2f}, Circumnference: {circumference:.2f}")
"""

""" 3
Kullanicidan aldiğiniz Celcius sicaklik birimin Fahrenheit 
ve Kelvin birimlerine çeviriniz. f = (c * 9/5) + 32 - K = C + 273

celcius = int(input("Enter temperature in Celcius: "))
fahrenheit = (celcius * 9 / 5) + 32
kelvin = celcius + 273

print(f"{celcius} C = {fahrenheit} F")
print(f"{celcius} C = {kelvin} K")

"""


"""4
İkinci dereceden denklemin genel formülü: ax² + bx + c = 0
Kök formülleri: (-b ± √(b² - 4ac)) / 2a

2x² - 7x + 3 = 0 denkleminin kökleri nedir?
a = 2
b = -7
c = 3

X1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
X2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
print(f"X1: {X1}")
print(f"X2: {X2}")
"""



