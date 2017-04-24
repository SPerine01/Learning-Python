# sets and dictionares, they're referred to as collections
# they're unordered collections of items

# a set is an unordered collection of unique items, not duplicates
# sets are created with {} brackets
fileset = {2015, 2017, 2019}

filelist = [2015, 2017, 2017]

# you can convert a list object into a set object and get rid of the duplicates 
filelist = set(filelist)
print(filelist)
# the new filelist will produce a set and it'll remove dupes

print(type(filelist))
# <class 'set'>

# you can also make a set into a list
filelist = list(filelist)
print(type(filelist))
# <class 'list'>



# dictionares are key value pairs, like objects in javascript and hashes in ruby, they also use the {} brackets
filedict = {
	"last year": 2016,
	"this year" 2017,
	"next year": 2018
}
