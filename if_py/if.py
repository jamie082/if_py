#!/usr/bin/python3
    
class Program:

    def __init__(self, a = 1200, b = 2200):

p1 = Program(1200, 2200)

    def get_method (self):
        print("Getting value...")
        return self._method

    def set_method (self, value): # if method
        print("Outputting print value...")
        if value > 1:
            print("Answer:" , p1.a , "is greater than", p1.b ,)
        self._method = value

class Program_2:

class CoralReef (Program, Program_2):
    pass

human = Program(20)

# Get the to_fahrenheit method
print(human.to_fahrenheit())

human.temperature = -200
