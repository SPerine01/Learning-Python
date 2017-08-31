# using object data

#!/usr/bin/python3
# classes.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com

# this code is highly scalable
class Duck:
    def __init__(self, **kwargs):
        self.variables = kwargs

    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

    # def set_color(self, color):
    #     self.variables['color'] = color
    #
    # def get_color(self):
    #     return self.variables.get('color', None)

    def set_variable(self, k, v):
        self.variables[k] = v

    def get_variable(self, k):
        return self.variables.get(k, None)


def main():
    donald = Duck(feet = 2)
    donald.set_variable('color', 'blue')
    print(donald.get_variable('feet'))
    print(donald.get_variable('color'))
    # print(donald.get_color())
    # donald.set_color('blue')
    # print(donald.get_color())
    # donald.quack()
    # donald.walk()

if __name__ == "__main__":
    main()
