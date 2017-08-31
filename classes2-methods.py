# using methods

#!/usr/bin/python3
# classes.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com

# quack and walk are indented under the class Duck, therefore they're methods of the class Duck

class Duck:
    def __init__(self, value):
        self._val = value
    #     def __init__(self) is a constructor method
    # constructors initialize data, and allow you to build your
    #  this gets called every time you create an object based on this class
    # self._val creates a local variable that's an attribute of the object

    def quack(self):
        # self is a reference of the object quack, not the class Duck
        print('Quaaack!', self._val)

    def walk(self):
        print('Walks like a duck.', self._val)

def main():
    donald = Duck(55)
    frank = Duck(151)
    donald.quack()
    donald.walk()
#     we're calling the quack method and the walk method on the object donald
#   calls are done using the dot . operator, which is a reference to an attribute of the object
#   in this case, the attribute is a method and its called with the () as you would call a function
#  these are actually functions, but they're function that are attributes of an object
    frank.quack()
    frank.walk()
if __name__ == "__main__": main()

# all in all, when the object calls a method (the function of the class) that self variable gets passed,
# and that's a reference to the object. everything attached to the object, its methods, attributes, data, are carried there
# methods are defined like functions, but its first argument is ALWAYS self and isn't passed explicitly
# its passed implicitly through the dot operator
# the constructor is to initialize whatever needs to be initialized when you create the object based on the class
