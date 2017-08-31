#!/usr/bin/python3
# string objects
# understanding strings as objects

str = 'This is a string'
print(str)
print(str.upper())
# prints in uppercase

str1 = 'THIS IS ANOTHER STRING'
print(str1.lower())


str2 = 'This is one more string {}'.format(42)
print(str)

print('===' * 15)
# working with common string methods

s = 'my string'
print(s.capitalize())
# capitalizes the first letter of the string

print(s.upper())
# capitalizes every letter

print(s.lower())
# every letter is lowercase

a = 'my STRINGY STRING string'
print(a.swapcase())
# swaps prints the opposite case, MY stringy string STRING

print(a.find('my'))
# finds which position it's in, in this case 0 (0 indexed)

print(id(a))
# finds the id of the variable

print(a.replace("my", "our"))
# replaces text within the string

print(id(a))
# still has the same id

newstring = a.upper()
print(newstring)
print(id(newstring))
# since we assigned a.upper to the newstring variable, this new variable has a new place in memory
# a still has the same id, same place in memory

z = " here is my CRAZY string   "
print(z.strip())
# strip() strips out a particular sequence of chars from the end and beginning of the string
# by default, it gets rid of additional whitespace

print(z.rstrip('\n'))
# specifies what you exactly want to be stripped

print(z.isalnum())
# isalnum checks if the string has all alphanumberic chars in it. it prints False, because it has spaces in it as well

x = 'HereIsAnotherString'
print(x.isalnum())
# prints True b/c it's all alphanumeric

print(x.isalpha())
# checks if the string has alpha chars, letters a - z

print(x.isdigit())
# checks if the string has just digits

y = '12345'
print(y.isdigit())
# prints True

print(y.isprintable())
# isprintable check if the strings can be printed.
# if chars occupy printing space on the screen, they are known as printable chars
# this is True

q = "Testing out some strings"
print(q.center(80))
# centers the string based on the length you give it