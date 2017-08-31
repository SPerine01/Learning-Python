# creating sequences with tuples and lists

# tuples are immutable, lists are mutable

t = 1, 2, 3, 4, 5
print(t)
# tuples aren't created with the (), they're created with the comma , operator
print(t[0])
# tuples are also 0 indexed
print(t[-1])
# another way to get the last element
print(len(t))
#  prints the length of the tuple, which has 5 elements
print(min(t))
# prints the smallest number
print(max(t))
# prints the largest number

print(type(t))

tup = (1,)
print(tup)
# how to create a tuple with just one element
print(type(tup))

x = [1, 2, 3, 4, 5]
print(x)
print(x[1])
print(max(x))
print(len(x))
print(min(x))

tups = tuple(range(25))
print(tups)
# tups[10] = 99
# ^ this won't work, since you can't change the tuple

lis = list(range(25))
print(lis)
lis[10] = 99
print(lis)