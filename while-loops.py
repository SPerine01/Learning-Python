#!/usr/bin/python3
# while.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    # simple fibonacci series
    # the sum of two elements defines the next set
    a, b = 0, 1
    while b < 250:
        print(b, end=' ')
        a, b = b, a + b

if __name__ == "__main__": main()

# while loops will evaluate while the expression is true
# fibonnacci adds the previous number to itself
# b is displayed, 1. then a + b, 0 + 1 = 1
# a then becomes 1, be is 1, a + b = 2
# a is 1 + b being 2 makes 3
# a is now 2 + b being 3 makes 5
# a is 3 + b being 5 makes 8
# a is 5 + b being 8 makes and so on