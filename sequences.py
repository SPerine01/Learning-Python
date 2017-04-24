# lists and tuples, they're sequences of objects

# lists are like arrays, they are zero index based and they use the [] brackets. They can be changed
# lists can contain strings, numbers, files and other data types
filelist = [2015, 2017, 2019]
# a list of 3 elements 2015, 2017, 2019

filelist[0]
# prints the first element in the list, 2015

filelist.append(2021)
# use . notation
# appends 2021 to end of list

filelist[1] - 2000
# removes 2000 and prints 17


# tuples are similar to lists, but they're immutable, can't change them
filetuple = (2015, 2017, 2019)
filetuple[2]
# prints 2019 in the python shell

filetuple.append(2021)
# prints error because the tuple object is immutable and doens't have the attribute 'append'