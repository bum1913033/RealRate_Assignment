# create a class 'Person' with the attributes name, age
class Person:
    # define the constructor method
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # define the greet() method
    def greet(self):
        # format a string based on given example and assign to a variable 'greeting'
        greeting = f'Hello, my name is {self.name} and I am {self.age} years old.'
        print(greeting)
        return greeting

# create two objects of the Person class
person1 = Person("Shubham", 21)
person2 = Person("Kiaan", 17)

# call greet function on both objects
person1.greet()
person2.greet()