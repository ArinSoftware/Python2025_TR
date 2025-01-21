""" 1
Kullanicidan sayisal notunu alip karsiliğinda harf notunu yazalim.
A: 100 - 85
B: 70 - 84
C: 55 - 69
D: 45 - 54
F: 0 - 44


score = int(input("Enter your score (0 - 100): "))

if score >= 85:
    print("Your grade is: A")
elif score >= 70:
    print("Your grade is: B")
elif score >= 55:
    print("Your grade is: C")
elif score >= 45:
    print("Your grade is: D")
else:
    print("Your grade is F")

"""

""" 2
Asağidaki listelerden sadece tekil elemanlardan oluşan tek bir liste oluşturunuz.
list1 = [1, 3, 5, 3]
list2 = [5, 1, 4, 3, 2]

list1 = [1, 3, 5, 3]
list2 = [5, 1, 4, 3, 2]

list1.extend(list2)

unique_list = []

for num in list1:
    if num not in unique_list:
        unique_list.append(num)

print("Unique List: ", unique_list)
"""

""" 3
Kullanicidan başlangic ve bitis sinirlarini alarak aradaki asal sayilari liste olarak yazdiriniz.



start = int(input("Enter your start num: "))
end = int(input("Enter your end num: "))

primes = []

for num in range(start, end+1):
    if num <= 1:
        continue
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)



print(f"Prime numbers in the range {start} - {end}: {primes}")
"""

""" 4
Asagida listede bulunan sayilardan yalnizca 5 ten büyük ve çift sayilari yazdiriniz.
nums = [9, 2, 7, 6, 1, 8, 3, 10]
Mantiksal Operatöyle üzerine konusalim and - or - not

#logical and
#her iki durumda True - True sonuc True olur
#herhangi bir koşul False ise False dönecek

#logical or
#herhangi bir koşul True ise True
#tüm koşullar False ise False dönecek

#logical not
#not True, False döner
#not False True döner

nums = [9, 2, 7, 6, 1, 8, 3, 10]

for num in nums:
    if num > 5 and num % 2 == 0:
        print(num)
"""
        
""" 5
Basit bir hesap makinesi olusturunuz. 
1 +
2 -
3 *
4 /
5 exit

1-2-3-4-5 haricinde girdi olduğunda hata ver
numeric input olmadiğinda hata ver
"""

print("Welcome to the Calculator!")
print("Options:")
print("1 for Addition (+)")
print("2 for Subtraction (-)")
print("3 for Multiplication (*)")
print("4 for Division (/)")
print("5 for Exit")

while True:

    operation = input("Please choose an operation (1/2/3/4/5): ")

    #validate operation input
    if operation not in ["1", "2", "3", "4", "5"]:
        print("Invalid Choice! Please select a valid option")
        continue

    #exit from the Calculator
    if operation == "5":
        print("Existing from the Calculator, bye bye")
        break

    num1 = input("Enter your first number: ")
    num2 = input("Enter your second number: ")

    #validate numeric input
    if not (num1.isdigit() and num2.isdigit()):
        print("Invalid Input! Enter numeric values only")
        continue

    #convert inputs to numbers
    num1 = float(num1)
    num2 = float(num2)

    #perform the operation
    if operation == "1":
        result = num1 + num2
        print(f"The result is: {result}")

    elif operation == "2":
        result = num1 - num2
        print(f"The result is: {result}")

    elif operation == "3":
        result = num1 * num2
        print(f"The result is: {result}")

    elif operation == "4":
        if num2 == 0:
            print("Error: Division by zero")
        else:
            result = num1 / num2
            print(f"The result is: {result}")