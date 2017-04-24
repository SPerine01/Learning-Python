# strings support indexing just like lists and tuples do
filelist = list(range(2000, 2020, 2))
print(filelist)
# this list prints a range of 2000 to 2020, with a step of 2 (2000, 2002, 2004, etc)
# they are still 0 indexed, 0 being 2000, 9 being 2018

filelist[2]
# prints 2004

filelist[7]
# prints 2014

# if you want to access a slice of the range, the number you include in the last index isn't included in the slice
filelist[1:6]
# this will print from the 0 index to the 5th index [2002, 2004, 2006, 2008, 2010], excluding the 6th index

# accessing only the first 3 items
filelist[:3]

# accessing a slice of the range after the 2nd index
filelist[2:]

# accessing last 2 items of the list
filelist[8:]

# accessing a slice of the list, with the exception of the last 2 items
filelist[:-2]

# you can also create slices with strings
aString = "Something here"
aString[5]
# prints 'h'

aString[4:]
# prints 'thing here'


# slices also work for tuples
aTuple = (1, 2, 3, 4, 5, 86, 89)
aTuple[4:]
# prints 5, 86, 89

aTuple[-2:]
# prints 86, 89
