# Simple Class

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("Woof!")

# Creating an instance of the Dog class
my_dog = Dog(name="Buddy", age=3)

# Accessing attributes and calling methods
print("Name:", my_dog.name)
print("Age:", my_dog.age)
my_dog.bark()
