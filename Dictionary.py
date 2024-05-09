"""
Python Dictionaries
"""

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

print(thisdict["brand"])

# Duplicates Not Allowed
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
print(len(thisdict))
x = thisdict.get("model")
print(x)


x = thisdict.values()
print(x)

x = thisdict.items()
print(x)

if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

# Change Values

thisdict["year"] = 2018
print(thisdict.items())


# Update Dictionary
thisdict.update({"color": "red"})
print(thisdict.items())

thisdict.pop("model")
print(thisdict)

thisdict.popitem()
print(thisdict)

del thisdict
# print(thisdict) gives error
