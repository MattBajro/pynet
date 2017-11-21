#!/usr/bin/env python


def func1():
    print "Hello func1"


class MyClass(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def hello(self):
        print "MyClass hello: {}".format(self.x + self.y + self.z)

    def not_hello(self):
        print "MyClass not_hello: {}, {}, {}".format(self.x, self.y, self.z)


class MyChildClass(MyClass):
    def __init__(self, x, y, z):
        super(MyChildClass, self).__init__(x, y, z)
        print "Doing something more in __init__ of child class"

    def hello(self):
        print "MyChildClass hello override: {}".format(self.x - self.y - self.z)


def main():
    print "Do something in Hello"


if __name__ == "__main__":
    main()
