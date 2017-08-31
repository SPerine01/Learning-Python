x = 42
print(id(x), x)
print(type(42))
# x has a value of 42, but its id, its place in memory, is 4297547872

y = 42
print(id(y), y)
# y also has the id of 4297547872
print(type(y))

print(x == y)
# this is true
# the == compares values. both values are 42, so its true


print(x is y)
# this is true as well
# is operator compares ids, to see if they refer to the same object

a = dict( a = 42)
print(id(a), a)

b = dict(a = 42)
print(id(b), b)
# a and b have 2 different ids because they are mutable and point to different places in memory

print(a == b)
# prints true because they have he same value
print(a is b)
# prints false because they have different ids


# True and False are objects of the bool class, they are immutable
c, d = 0, 1
print(c == d)
print(c < d)

c = True
print(type(c), c)

d = True
print(id(c))
print(id(d))
print(id(True))
# they will print the same id, because True is stored in memory by that id


