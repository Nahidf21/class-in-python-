#creat a class named person, use the__init__() function to assign values for name and age:

class Person:
    def __init__(self, name , age):
        self.name=name
        self.age=age
p1=Person("John",36)
print(f"name is {p1.name} and age {p1.age}")