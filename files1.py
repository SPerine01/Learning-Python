#!/usr/bin/python3
# files.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    f = open('lines.txt')
    # by default, the open() function opens the file in read mode
    # if you don't specify, read mode is the default
    # f = open('lines.txt', 'r') this is what read mode looks like
    # there r for read, w for write and a for append
    # append is a special write mode that sets its current position to the end of the file
    # so everything you write will be appended to the file

    # r+ will open it for both read and write
    # rt for text file mode and rb for binary mode

    # the open function returns the file handle
    # its an iterable object and in iteration mode, it gives you one line of the file at a time
    # the readlines method does the same thing
    for line in f:
        print(line, end = '')

if __name__ == "__main__": main()
