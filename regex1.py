#!/usr/bin/python3
# regex.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Gorup, LLC

import re
# the re module allows of us to search regex with the re.search method

def main():
    fh = open('raven.txt')
    for line in fh:
        match = re.search('(Len|Neverm)ore', line)
        if match:
            print(match.group())
        #     the group function get all of the Len|Neverm)ore words we matched

        # if re.search('(Len|Neverm)ore', line):
            # re.search method allows us to search with reg expressions
            # does regex search through "The Raven" to find Lenore and Nevermore
            # print(line, end='')

if __name__ == "__main__": main()
