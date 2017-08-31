#!/usr/bin/python3
# variables.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    n = 42
    s = r"This is a \n {} string!".format(n)
    # .format() method is a method of the string object
    # r is for "raw string", its for regular expression

    s2 = '''\
    this is useful
    if you have
    line after line
    of text
    '''
    print(s)
    print(s2)

if __name__ == "__main__": main()