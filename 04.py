class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)
    print(f"Hello my age is {abc.age}" )
    
p1 = Person("John", 36)
p1.age=40
p2=Person("nahid",32)
p1.myfunc()
p2.myfunc()