# using named function arguments

#!/usr/bin/python3
# functions.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com

def main():
    testfunc(5, 6, 7, 8, 9, 10, one = 1, two = 2, four = 42)
#     passing named parameters into a function
#     these named arguments are being passed by the caller
#     testfunc() calls the function

def testfunc(this, that, other, *args, **kwargs):
    # this is the receiving end of the function, but it also isn't naming the arguments
    # since they're not named on the receiving end, they're called **kwargs, keyword arguments
    # kwargs is a actually dictionary
    # this, that and other arguments will take the place of 5, 6, 7
    # while *args will be 8, 9, 10
    for k in kwargs:
        print(k, kwargs[k])

    for n in args:
        print(n)
    # print('This is a test function',
    #       this, that, other, args,
    #       kwargs['one'], kwargs['two'], kwargs['four'])

if __name__ == "__main__": main()