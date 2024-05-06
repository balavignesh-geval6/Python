"""
Python Numbers

There are three numeric types in Python:

int
float
complex

"""

x = 1
y = 2.8
z = 1j

print(type(x))
print(type(y))
print(type(z))


# Int

x = 1
y = -200
z = int(200.10005)
print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z))

# floot

x = 1.10
y = float(1)
z = -35.59
print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z))


x = 35e3
y = 12E71
z = -87.7e100
print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z))


#  Complex

x = 3+5j
y = 5j
z = -5j
print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z))


#  Type Conversion

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#  Random Number
import random

print(random.randrange(1, 10))