# using lists of arguments

#!/usr/bin/python3
# functions.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com



def main():
    testfunc(1, 2, 3, 42, 43, 45, 46)
#     give additional optional arguments for your *args argument

def testfunc(this, that, other, *args):
    # the asterisk is special in that it is just a list of optional arguments

    print(this, that, other, args)
#     this prints a tuple with the additional args
    for n in args:
        print(n, end= ' ')
#         prints the additional arguments on another line

if __name__ == "__main__": main()