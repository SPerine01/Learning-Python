# understanding inheritance

# a duck is an animal, so it can inherit attributes from animal

#!/usr/bin/python3
# classes.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com

class Animal:
    def talk(self):
        print("I have something to say")

    def walk(self):
        print("Hey! I'm walkin' here!")

    def clothes(self):
        print("I have nice clothes")

class Duck(Animal):
    # by placing there, Duck is inheriting the methods, well, attributes, of the Animal class

    def quack(self):
        print('Quaaack!')

    def walk(self):
        super().walk()
        # this super function accesses the parent class, now donald will do both his walk and his parent's walk
        print('Walks like a duck.')

class Dog(Animal):
    # pass
# pass is a placeholder text when code is required, but you haven't written anything in yet
    def clothes(self):
        print('I have brown and white fur')

def main():
    donald = Duck()
    donald.quack()
    donald.walk()
    # this prints the Duck's walk method and not the Animal's walk method, because Duck's walk method overrides walk in Animal
    # Duck inherits Animal, but Duck defines its own method called walk, so it uses its own instead of its parents
    donald.talk()
    donald.clothes()

    fido = Dog()
    fido.walk()
    fido.talk()
    fido.clothes()

if __name__ == "__main__": main()
