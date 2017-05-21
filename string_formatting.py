_author_ = 'dev'
age = 25
print('My age is ' + age + ' years old')
#this will produce an error in idle3, TypeError: Can't convert 'int' object to str implicitly
# it must be coverted into a string

print('My age is ' + str(age) + ' years old')
# prints My age is 25 years

# replacement fields

print("My age is {0} years".format(age))
# prints My age is 25 years

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7} ".format(31,
"January", "March", "May", "July", "August", "October", "December"))
# with replacement fields, the initial values are replaced with the newer values
# it sort of sits in a list and the new values (31, January, March) replace the previous values {0}, {1}, {2}

# here's another form of replacement fields, but on multiple lines
print("""January: {2}
February: {0}
March: {2}
April: {1}
May: {2}
June: {1}
July: {2}
August: {2}
September: {1}
October: {2}
November: {1}
December: {2}""".format(28, 30, 31))
