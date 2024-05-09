"""
Tuple
Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets.
"""

thistuple = ("apple", "banana", "cherry")
print(thistuple)

#  Tuple items are ordered, unchangeable, and allow duplicate values.

# allow duplicates

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

# Tuple Length

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

# single tuple is required with , at last

thistuple = ("apple",)
print(type(thistuple)) # type

# Tuple Items - Data Types
tuple1 = ("abc", 34, True, 40, "male")

# Access Tuple Items

thistuple = ("apple", "banana", "cherry", "apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[1])

# Negative Indexing
print(thistuple[-1])

# range
print(thistuple[2:5])

# without start value select all up to stop value
print(thistuple[:4])

# range will go on to the end of the tuple:
print(thistuple[2:])

# Check if Item Exists
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

# Change Tuple Values
# Once a tuple is created, you cannot change its values. Tuples are unchangeable
# for changing convert the tuple into a list, change the list, and convert the list back into a tuple.

y = list(thistuple)
y[1] = "kiwi"
x = tuple(y)

print(x)

# Add Items

y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

# Add tuple to a tuple
y = ("orange",)
thistuple = thistuple + y
thistuple += y
print(thistuple)

#Remove Items

y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

#delete the tuple completely:

del thistuple

# Unpacking a Tuple

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, *yellow, red) = fruits

print(green)
print(yellow)
print(red)

# Loop Through a Tuple

thistuple = ("apple", "banana", "cherry", "apple", "banana", "cherry", "orange", "kiwi", "melon", "mango","orange","orange","orange",)
for x in thistuple:
  print(x)

for i in range(len(thistuple)):
  print(thistuple[i])

print()

# Using a While Loop

i = 0
while i < len(thistuple):
    print()
    print(thistuple[i])
    i = i+1

# Join Two Tuples

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

x = thistuple.count("orange")

print(x)