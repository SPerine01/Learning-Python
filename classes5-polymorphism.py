# applying polymorphism to classes

# polymorphism is using one object of one particular class as if it were another object of another class

#!/usr/bin/python3
# classes.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com


class Duck:
    def quack(self):
        print('Quaaack!')

    def walk(self):
        print("Walks like a duck.")

    def bark(self):
        print("The duck cannot bark")

    def fur(self):
        print("The duck has feathers")

class Dog:
    def bark(self):
        print("Woof!")

    def fur(self):
        print("The dog has brown and white fur")

    def walk(self):
        print("Walks like a dog")

    def quack(self):
        print("The dog can't quack")

def main():
    donald = Duck()
    fido = Dog()
    in_the_forest(donald)
    # as long sa donald implements whats being used in this function, it will work
    in_the_pond(fido)

    # donald.quack()
    # donald.walk()
    # fido.bark()
    # fido.fur()

def in_the_forest(dog):
    dog.bark()
    dog.fur()
    # this function typically expect a dog, but you can name it anything because its just a variable
    # Python is good with this b/c object in Python don't care what the name of the class is, b/c everything is an object
    # this is also called duck typing b/c if it walks like a duck, you can use it like a duck. Just like its an object
#     you can switch out dog for cat, and it'll still work exactly the same

def in_the_pond(duck):
    duck.quack()
    duck.walk()


    # for o in (donald, fido):
    #     o.quack()
    #     o.walk()
    #     o.fur()
    #     o.bark()
#     calling all 4 functions from both objects, using them exactly the same way
#     python calls the methods without concern of what type of object it is, as long as it exists


if __name__ == "__main__": main()
