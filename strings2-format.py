# formatting strings with str.format

a, b = 5, 42
print(a, b)

print('this is {}, that is {}'.format(a, b))

# the format method also returns a new string

s = 'this is {}, that is {}'
print(s.format(a, b))
print(id(s))

new = s.format(a, b)
print(new)
print(id(new))
# s and new have different ids, because format returns a new string when its used

x = 'he is {}, she is {}'.format(a, b)
y = 'he is {1}, she is {0}'.format(a, b)
print(x)
print(y)
# y prints he is 42, she is 5, because even though we have a and b listed in the method,
# we're telling our string that the 1 index should go first and the 0 index second

q = 'this is {1}, that is {0}, this too is {1}'.format(a, b)
print(q)

# you can also names and name your arguments in format
m = 'this guy is {bob}, and that\'s {fred}'.format(bob = a, fred = b)
print(m)

# you can also put them in a dictionary
d = dict(bob = a, fred = b)
print('this is {bob} and that is {fred}'.format(**d))
