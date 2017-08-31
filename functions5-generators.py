# creating a sequence with a generator function
# a generator function is a function that returns an iterator object
#

#!/usr/bin/python3
# generator.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com


def main():
    print("This is the functions.py file.")
    for i in inclusive_range():
        # range can be called with one argument, stop variable will use 25, start and step will default to 0 and 1

        print(i, end = ' ')

# def inclusive_range(start, stop, step):

def inclusive_range(*args):
    numargs = len(args)
    if numargs < 1:
        raise TypeError('requires at least one argument')
    elif numargs == 1:
        stop = args[0]
        start = 0
        step = 1
    elif numargs == 2:
        (start, stop) = numargs
        step = 1
    elif numargs == 3:
        (start, stop, step) = args
    else:
        raise TypeError('inclusive_range expected at most 3 arguments, got {}'.format(numargs))
    i = start
    while i <= stop:
        yield i
        # yield returns i, but will be incremented by step
        i += step


if __name__ == "__main__": main()
