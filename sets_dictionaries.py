# set is an unordered collection of unique items, no duplicates
fileset = {2015, 2017, 2019}

filelist = [2015, 2017, 2017]

# you can convert a list into an object with the set method
filelist = set(filelist)
# it converts filelist object into a set object and gets rid of any duplicate values

print(type(filelist))
# prints <class 'set'>

# you can also convert a set back into a list 
filelist = list(filelist)
print(filelist)

print(type(filelist))
# <class 'list'>


# dictionary is a key/value pair object. like objects in javascript
# an object constructed with pairs of keys and values
filedict = {"last year": 2016, "this year": 2017, "next year": 2018}

# you can access dictionary values using corresponding keys
filedict["this year"]
# it will returb 2017
