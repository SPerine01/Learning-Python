list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list)
print(type(list))
print(list[2])
print(list[0:5])
# this prints [1, 2, 3, 4, 5] but not 6, which is the 5th index
# doesn't print the last item in the list
# Python slices only gives up to and not included that index

range(0, 10)
for i in range(0, 10):
    print(i, end='')
# only prints 1 - 9, b/c ranges in Python are non inclusive
# they don't include the last number

list[:] = range(100)
print(list)
print(list[27])
print(list[27:42])
# will print 27 - 41
print(list[27:42:3])
# it skips through the list in steps of 3, steps over 3 elements
print(list[27:43:3])

for i in list[27:42:3]:
    print(i)

list[27:42:3] = (99, 99, 99, 99, 99)
print(list)
# you can assign elements to the slice
# above i assigned 99 to the elements, skipped by 3, 27 - 39
# it will print 26, 99, 28, 29, 99, 31, 32, 99, 34, 35, 99, 37, 38, 99...