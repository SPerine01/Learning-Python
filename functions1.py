# defining functions

#!/usr/bin/python3
# functions.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com

def main():
    testfunc(42)
    # testfunc(42, 53, 64)

def testfunc(number, another = None, onemore = 64):
    if another is None:
        # this gives the default as 112, but if an argument is passed, another will take on that value
        another = 112
    print('This is a test function', number, another, onemore)
#     if you were to remove this print statement, there would be an error
#     python would think you intended to put the code below inside the testfunc() function

if __name__ == "__main__":
    main()

# if you define 3 arguments into your function, like above, def testfunc(number, another, onemore):
# but don't pass them, you get a TypeError. If you define the arguments, you must pass them
# TypeError: testfunc() missing 2 required positional arguments: 'another' and 'onemore'

# however, you can give your arguments default values if you don't pass them
# however again, if you pass all arguments to the function, it overwrites the default values

