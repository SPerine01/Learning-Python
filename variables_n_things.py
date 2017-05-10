
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