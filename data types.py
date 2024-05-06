"""
Python Data Types
"""

#  Built-in Data Types

"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""

#  Getting the Data Type

x = 5
print(type(x))

# string data type

x = "Hello World"
print(x)
print(type(x))

# int data type

x = 20
print(x)
print(type(x))

# float data type

x = 20.5
print(x)
print(type(x))

# complex data type

x = 1j
print(x)
print(type(x))

# list data type

x = ["apple", 'banana', "cherry"]
print(x)
print(type(x))

# tuple data type

x = ("apple", "banana", "cherry")
print(x)
print(type(x))

# range data type
x = range(6)
print(x)
print(type(x))

# dict data type
x = {"name": "John", "age": 36}
print(x)
print(type(x))

# set data type
x = {"apple", "banana", "cherry"}
print(x)
print(type(x))


# frozenset  data type
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))


# bool data type
x = True
print(x)
print(type(x))



# bytes data type
x = b"Hello"
print(x)
print(type(x))



# bytearray data type
x = bytearray(6)
print(x)
print(type(x))


# memoryview data type
x = memoryview(bytes(5))
print(x)
print(type(x))


# NoneType data type
x = None
print(x)
print(type(x))






