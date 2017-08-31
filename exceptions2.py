#!/usr/bin/python3
# exceptions.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Gorup, LLC

def main():
    # fh = open('lines.txt')
    try:
        for line in readfile('xlines.doc'): print(line.strip())
    except IOError as e:
        print('Cannot read file', e)
    except ValueError as e:
        print('Bad filename', e)

def readfile(filename):
    if filename.endswith('.txt'):
        fh = open(filename)
        return fh.readlines()
    else:
        raise ValueError('Filename must end with .txt')
# the readlines method is an iterator

if __name__ == "__main__": main()
