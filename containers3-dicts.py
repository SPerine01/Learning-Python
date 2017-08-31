# organizing data with dictionaries

# dictionaries are hashed arrays
# in dictionaries, indexes are data
# you can store dictionaries within dictionaries, as well as lists and tuples in dictionaries


d = {'one': 1, 'two': 2, 'three': 3}
print(d)

d = dict(one = 1, two = 2, three = 3)
print(d)

print(type(d))


# initialize one dictionary from another
x = dict(four = 4, five = 5, six = 6)
print(x)

d = dict(one = 1, two = 2, three = 3, **x)
print(d)

# test in a value is in a dictionary
print('four' in x)
print('three' in x)

# iterate over a dictionary
for key in d:
    print(key)

# prints keys and values
for k, v in d.items():
    print(k, v)

# to get an item from the dictionary
print(d['three'])
# however, this gives you an error if your dictionary doesn't have that key
# print(x['three'])
# KeyError: 'three'

# to get around this issue, you can use the get() method
d.get('three')
# ^ prints three
x.get('three')
# ^ silently gives you the None value
print(x.get('three', 'not found'))
# ^ will print the default value not found

# to delete an item from the dictionary
del x['four']
print(x)

x.pop('five')
print(x)