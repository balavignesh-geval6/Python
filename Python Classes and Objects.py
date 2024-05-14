"""
Python Classes/Objects
"""

class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)

#  The __init__() Function

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

print(p1)


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  print("welcome ")

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)

# Object Methods

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(name):
    print("Hello my name is " + name.name)

p1 = Person("John", 36)
p1.myfunc()

# Delete Objects
# del p1.name
p1.myfunc()


del p1
print(p1)