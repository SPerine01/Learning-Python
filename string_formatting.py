_author_ = 'dev'
age = 24
print('My age is ' + age + ' years old')
#this will produce an error in idle3, TypeError: Can't convert 'int' object to str implicitly
# it must be coverted into a string

print('My age is ' + str(age) + ' years old')