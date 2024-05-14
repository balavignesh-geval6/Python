"""
Python Inheritance
"""


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

x = Person("John", "Doe")
x.printname()

class Student(Person):
    pass
student = Student("John", "Doe")
student.printname()

class Student(Person):
  def __init__(self, fname, lname, year):
    Person.__init__(self, fname, lname)
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
      print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)


def __str__(self):
      return self.graduationyear

newobject = Student("bala","vignesh",1995)
newobject.printname()
newobject.welcome()