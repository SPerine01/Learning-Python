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

for i in range(1, 12):
	print("No. {0:2} squared is {1:4} and cubed is {2:4} ".format(i, i**2, i**3))
# the first number is the replacement field number, while the :2 adds 2 spaces in the line and the :4 adds 4 spaces in the line, for neatness


for i in range(1, 12):
	print("No. {} squared is {} and cubed is {:4} ".format(i, i**2, i**3))
# you don't have to place anything in the {}, but the values will take the place of the field that is to be replaced, in the order starting from 0)
# this method of using replacement fields cannot be used more than once, because it has no initial value
