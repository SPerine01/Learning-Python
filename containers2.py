# operating on sequences with built-in methods

t = tuple(range(25))
print(t)
print(type(t))
print(10 in t)
print(50 in t)
print(65 not in t)
print(t[10])
print(len(t))

for i in t:
    print(i)

x = list(range(20))
print(x)
print(type(x))
print(25 in x)
print(27 not in x)

# t[20] = 11
# TypeError: 'tuple' object does not support item assignment

x[15] = 11
print(x)

print(t.count(5))
# counts how many of the particular integer is there
print(t.index(5))
# finds the index

# print(t.append(100))
# AttributeError: 'tuple' object has no attribute 'append'

x.append(100)
print(x)
print(len(x))
x.extend(range(20))
# extend method allows you to extend the list with any iterable object
print(x)

x.insert(0, 25)
# inserts an element in the index where you choose
print(x)

x.remove(0)
# removes the item with the value 0
print(x)

del x[12]
# deletes the element at index 12
print(x)

x.pop()
# removes nd returns the last object from the list
print(x)

# to pop from the beginning, you specify the index
x.pop(0)
print(x)