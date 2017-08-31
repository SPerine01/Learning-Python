#!/usr/bin/python3
# modules.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com


import sys
# sys is for specific parameters and functions
# module provides access to some variables used or maintained by the interpreter and to functions that interact
# strongly with the interpreter
# it also gets the python version


def main():
    print('Python version {}.{}.{}'.format(*sys.version_info))
    print(sys.platform)
#     prints the category of the operating system, not the actual os

    import urllib.request
    page = urllib.request.urlopen('https://bw.org')
    for line in page:
        print(str(line, encoding= 'utf_8'), end= '')


    import os
#   you can import the os in a function, without having to import it above
    print(os.name)
    print(os.getenv('PATH'))
    print(os.getcwd())
    print(os.urandom(25))


    import random
    print(random.randint(1, 1000))

    import random
    x = list(range(25))
    print(x)
    random.shuffle(x)
    print(x)


    import datetime
    now = datetime.datetime.now()
    print(now)
    print(now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond)

if __name__ == "__main__": main()
