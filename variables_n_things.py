
greeting = "Hello there"
name = "Dan"
age = 35

print(greeting + " " + name + ", you're" + age + " right?")

# this produces an error, you can't concatenate a string and an integer

a = 12
# a regular integer, a whole number
b = 3

q = 8.4
# a float is a number with a decimal

print(a + b)
print(a - b)
print(a * b)
print(a / b)
# ^ this / always returns a float
print(a // b)
# ^ this // returns a whole number
print(a % b)
# this % returns the remainder

print(a + b / 3 - 4 * 12)
# ^ messy

print((((a + b) / 3)- 4) * 12)

# or

# c = a + b
# d = c /3
# e = d - 4
print(e * 12)
# much better, 12.0

# ---------

bird = "Nightingale"
print(bird)
print(bird[2:8])
# prints ghting

print(bird[:6])
# prints Nighti

print(bird[-4:-2])
# prints ga

print(bird[0:6:3])
# prints Nh


numbers = "1, 2, 3, 4, 5, 6, 7, 8, 9"
print(numbers[0::3])
# prints 123456789

print("Hello " * 5)
# prints Hello 5x, obviously

# the in operator checks if there is a substring in a string
today = "Sunday"
print("day" in today)
print("Sun" in today)
print("Thur" in today)
print("Hello" in numbers) 
