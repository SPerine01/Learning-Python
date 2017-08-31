#!/usr/bin/python3
# break.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    s = 'this is a string'
    for c in s:
        if c == 's':
            continue
        #     continue shortcuts , the loop and goes back to the beginning
        # in this case, looping through the string and not printing s
        print(c, end='')

# continue and break ONLY pertain to for/while loops
# else pertains to if statements as well as for/while loops

if __name__ == "__main__": main()

# displaying break
x = 'this is a string'
for y in x:
    if y == 's':
        break
        #     break terminates the loop entirely
        # once the loop reaches s, it breaks and doesn't print s
    print(y)


# displaying else
m = 'this is a string'
for n in m:
    print(n, end='')
else:
    print(" i shall print something else")
#     else runs when the for loop is false
# or when the for loop is out of stuff to iterate


# it works on while loops as well
u = 'this is a string'
i = 0
while i < len(u):
    print(u[i], end='')
    i += 1
else:
    print("else")
