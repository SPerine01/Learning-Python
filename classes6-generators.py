# using generators

#!/usr/bin/python3
# classes.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com

class inclusive_range:
    def __init__(self, *args):
        # our constructor
        numargs = len(args)
        if numargs < 1:
            raise TypeError('requires at least one argument')
        elif numargs == 1:
            self.stop = args[0]
            self.start = 0
            self.step = 1
        elif numargs == 2:
            (self.start, self.stop) = args
            self.step = 1
        elif numargs == 3:
            (self.start, self.stop, self.step) = args
        else:
            raise TypeError("expected at most 3 arguments, got {}".format(numargs))
        pass

    def __iter__(self):
        # this makes the object an iterable object
        i = self.start
        while i <= self.stop:
            yield i
            i += self.step


def main():
    o = inclusive_range(0,25, 5)
    # the range's start and step are already specified at 0 and 1, unless you explicitly change it
    for i in o:
        print(i, end = " ")

if __name__ == "__main__": main()
