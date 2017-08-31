# returning values from functions

#!/usr/bin/python3
# functions.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com

def main():
    for n in testfunc():
        print(n, end=' ')
   # print(testfunc())

def testfunc():
    # return 'This is a test function'
    return range(25)

if __name__ == "__main__": main()

# the return statement returns the value from a function
# return without an expression argument returns None