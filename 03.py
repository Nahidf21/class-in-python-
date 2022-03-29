#object Methodes

class Person:
#he self parameter is a reference to the current instance of the class, 
# and is used to access variables that belongs to the class.
    def __init__(self, name ,age): 
        self.name=name
        self.age=age

    def myFunction(self):
        print(f"Hello my name is {self.name}")

p1=Person("John",36)
p1.myFunction()