# understanding classes and objects

# Classes are how you create your own objects
# classes themselves are the blueprint of an object
# an object is an instance of a class
# when you create an object, it's built from the blueprint of the class, but it's its own object


#!/usr/bin/python3
# classes.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com

class Duck:
    # the class keyword introduces the definition of a class
    # Duck is the name of the class
    def quack(self):
        # the function quack and because it has self as its first argument, is actually a method of the class
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

def main():
    donald = Duck()
    # we create the object donald and we create the object donald by assigning it from Duck
    # so, donald is an object of the class Duck, the instance of Duck
    donald.quack()
    donald.walk()

if __name__ == "__main__": main()