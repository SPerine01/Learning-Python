#string and variable manipulation

parrot = "African Grey Parrot"
print(parrot)
#prints the string, duh

print(parrot[0])
#prints the first letter in string, A

print(parrot[-1])
#prints last letter, t

print(parrot[0:6])
#prints the range from 0 index to 6 index, prints Africa

print(parrot[6:])
#prints n Grey Parrot

number = "9,223,472,098,326,775,804"
print(number[1::4])
# prints ,,,,,,

numbers = "1, 2, 3, 4, 5, 6, 7, 8, 9"
print(numbers[0::3])
#prints 123456789

#multiplying strings
print("Hello " * 5)
#prints Hello Hello Hello Hello Hello 

today = "sunday"
print("day" in today)
# prints True

print("fri" in today)
#prints False

print("sun" in today)
#prints True

print("thurs" in today)
#prints False

filename = "weather_1901"
table = "temperature"
year = "1901"

realyear = 2017
print(type(realyear))
# prints out the type of object it is, in this case, an integer

price = 109.5
amount = 3
print(type(amount), type(price))
# prints out the object types for each, amount is an integer, while price is a float
