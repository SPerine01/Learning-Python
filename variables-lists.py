#!/usr/bin/python3
# variables.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    # x = 1, 2, 3  # this is a tuple
    # print(type(x), x)

    x = [1, 2,3]
    x.append(5)
    x.insert(2, 7)
    print(type(x), x)

if __name__ == "__main__": main()

m = "string"
print(type(m), m[2:4])