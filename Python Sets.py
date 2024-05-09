"""
Python Sets
Sets are used to store multiple items in a single variable.

Set is one of 4 built-in data types in Python used to store collections of data,
the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
"""

myset = {"apple", "banana", "cherry"}

print(myset)

# Duplicates Not Allowed

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

# true and 1 are same

thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

thisset = {"apple", "banana", "cherry"}

print(len(thisset))

# Access Items
# can't access item

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

print()
print("banana" in thisset)

print()
print("banana" not in thisset)

# Python - Add Set Items
print()

thisset.add("orange")
print(thisset)

tropical = {"pineapple", "mango", "papaya"}
print()

thisset.update(tropical)

mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

# Python - remove Set Items

thisset.remove("banana")

print(thisset)

# thisset.remove("banana") give error it item not present
print(thisset)

thisset.discard("banana")
print(thisset)

x = thisset.pop() # reomve random item
print(x)
print(thisset)

thisset.clear()
print(thisset)

del thisset
# print(thisset) gives error thisset is deleted

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

# Union

set1 = {"a", "b", "c","a","b"}
set2 = {1, 2, 3,"b","d"}



set1.update(set2)
print(set1)

set3 = set1.union(set2)
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)