"""
Python Lists
"""

# Lists are used to store multiple items in a single variable.
# Lists are created using square brackets:

List = ["apple","banana","cherry" ]
print(List)

# List items are ordered, changeable, and allow duplicate values.
# Ordered
# Changeable
# Allow Duplicates


list3 = ["apple","banana","apple","banana","orange",]
print(list)

x = "good morning"
print(len(x))

# List Length

print(len(list3))

# List Items - Data Types
list2 = ["apple",25,30.001,True,1]
print(list2)


print(type(list))

# The list() Constructor
list1 = list(("apple", "orage", "pinapple"))
print(list1)

# Access Items
list4 = ["apple", "banana", "cherry","kivi"]
print(list4[1],list4[2])

# Negative Indexing

print(list4[-1])
print(list4[-2])

# Range of Indexes

print(list4[0:7])
print(list4[:20])
print("\n")
print(list4[:])


# Range of Negative Indexes

thislist4 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist4[-4:-1])

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

# Change Item Value

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# Change a Range of Item Values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# Insert Items

thislist = ["apple", "banana", "cherry"]
thislist.insert(0, "watermelon")
print(thislist)

# Python - Add List Items

thislist.append("orange")
print(thislist)

# Insert Items
thislist.insert(1, "papaya")
print(thislist)

# Extend List
thislist1 = ["apple", "banana", "cherry"]
tropical2 = ["mango", "pineapple", "papaya"]
thislist1.extend(tropical2)
print(thislist1)
print(tropical2)
tropical2.extend(thislist1)
print(tropical2)

# Add Any Iterable
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)


# Remove Specified Item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# Remove the first occurance of "banana":
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

# Remove Specified Index
thislist.pop(0)
print(thislist)

# The del keyword also removes the specified index:

thislist = ["apple", "banana", "cherry"]
del thislist[2]
print(thislist)

# delete entire list
thislist = ["apple", "banana", "cherry"]
del thislist

# Clear the List

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# Loop Through a List

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

# Loop Through the Index Numbers

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(i)

print(range(len(thislist)))


# Using a While Loop

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

# Looping Using List Comprehension
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#List Comprehension
# create a new list based on the values of an existing list.

fruits = ["apple", "banana", "cherry", "kiwi", "mango",""]
newlist = []
print()
print(fruits[1:5])

for x in fruits:
  if "a" not in x:
    newlist.append(x)

print(newlist)

for i in range(len(fruits)):
    print(fruits[i])


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x if x == "banana" else "hello" for x in fruits]

print(newlist)
