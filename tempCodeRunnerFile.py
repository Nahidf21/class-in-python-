class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)
    
    
p1 = Person("John", 36)
#modify Object Propertices
del p1.age

print(p1.age)