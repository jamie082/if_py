#!/usr/bin/python3

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)
        print(self.age)


# Create a new Person object
p1 = Person("John", 36)

# Call myfunct() method
p1.myfunc()


# Create another Person object
# and create a new attrtibute 'attr'
p2 = Person("Bob", 100)
p2.attr = 100
