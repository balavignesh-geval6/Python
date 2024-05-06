# Creating Variables

#  Variables are containers for storing data values.

"""
A variable is created the moment you first assign a value to it.
"""

x = 5
y = "John"
print(x)
print(y)

# data types can be changed

x = 4
print(x)
x = "Sally"
print(x)

# data type can be specified with casting

x = int(10)
print(x)
x = float("1")
print(x)
x = str(12)
print(x)

# get the data type

X = 10
Y = "good"
Z = 10.25
print(type(X))
print(type(Y))
print(type(Z))

# Single or Double Quotes

name = 'bala'
name2 = "vignesh"

print(name + ' ' + name2)

#  Case-Sensitive

A = "Nane"
a = "number"

print(a)
print(A)
# A & a are different variable


"""
Variable Names
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
"""

# accepted variable names


myvar = "bala"
My_var = "vignesh"
MYVAR = "VIGNESH"
_MY_VAT = "vignesh"
myvar1 = "bala"

'''

# unaccepted variable names

2myvar = "bala"
My-var = "vignesh"
MY VAR = "VIGNESH"

'''

# Multi Words Variable Names

# Camel Case

myVariableName = "bala"

# Pascal Case

MyVariableName = "bala"

#  Snake Case

my_variable_name = "bala"

# Python Variables - Assign Multiple Values

fruitName1 , fruitname2 , fruitname3 = "Apple" , "orange" , "grape"

print(fruitName1)
print(fruitname2)
print(fruitname3)


# One Value to Multiple Variables

Fruit1 = fruit2 = fruit3 = "kivi"
print(Fruit1)
print(fruit2)
print(fruit3)

# Unpack a Collection

Fruits = ["mango","papaya","kivi"]
ArrayFruit1 , ArrayFruit2 , ArrayFruit3 = Fruits

print(ArrayFruit1)
print(ArrayFruit2)
print(ArrayFruit3)


# In the print() function, you output multiple variables, separated by a comma:

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

# You can also use the + operator to output multiple variables:

print(x + " " + y + " " + z)

# For numbers, the + character works as a mathematical operator:

x = 5
y = 10
print(x + y)

# The best way to output multiple variables in the print() function is to separate them with commas, which even
# support different data types:

x = 5
y = "John"
print(x, y)

# Global Variables

GlobalVariable1 = "python"

def myFunction():
    print("welocme to ",GlobalVariable1)

myFunction()

GlobalVariable2 = "awesome"

def myfun2():
    GlobalVariable2 = "fantastic"
    print("python is " + GlobalVariable2)

myfun2()

print("python is " + GlobalVariable2)


# To change the value of a global variable inside a function, refer to the variable by using the global keyword:

GlobalVariable3 = "awesome"
def myfun3():
    global GlobalVariable3
    GlobalVariable3 = "fantastic"
    print("python is " + GlobalVariable3)

myfun3()

print("python is " + GlobalVariable3)
















exit()
