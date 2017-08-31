#!/usr/bin/python3
# regex.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Gorup, LLC

import re

def main():
    fh = open('raven.txt')
    for line in fh:
        # print(re.sub('(Len|Neverm)ore', '###', line), end='')

        # if re.search('(Len|Neverm)ore', line):
            # re.sub is the search and replace method
            # sub may stand for substitute
            # print(line, end='')

        match = re.search('(Len|Neverm)ore', line)
        if match:
            print(line.replace(match.group(), '###'), end='')
#         just printing the lines where we replaced the string with '###'

if __name__ == "__main__": main()
