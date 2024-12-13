#Veri Dönüşümü (Type Conversion, Type Casting)

# str ==> int
num_str = "123"
num_int = int(num_str)
print(num_int, type(num_int)) #explicit type conversion

#float ==> int
num_float= 3.1459
num_int = int(num_float)
print(num_int, type(num_int))

#Type conversion için kullanılan built-in (gömülü) metodlar
# int(), float(), str(), dict(), set(), list(), tuple()

#int ==> str
num_int = 42
num_str = str(num_int)
print(num_str, type(num_str))

#Value Error!
value = "test"
int_value = int(value) #value error!

#Type Error!
num_str = "123"
print(len(num_str)) #3
num_int(int(num_str))
print(len(num_int)) #type error

# Implicit type conversion
int_val = 10
float_val = 5.5
result = int_val + float_val
print(result, type(result))


