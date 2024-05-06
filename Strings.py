"""
Python Strings
"""
# Strings in python are surrounded by either single quotation marks, or double quotation marks.
# 'hello' is the same as "hello".

print("Hello")
print('Hello')

# Quotes Inside Quotes
# You can use quotes inside a string, as long as they don't match the quotes surrounding the string:

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

# Assign String to a Variable
# Assigning a string to a variable is done with the variable name followed by an equal sign and the string:

a = "Hello"
print(a)

# Multiline Strings
# You can assign a multiline string to a variable by using three quotes:

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

# Strings are Arrays

a = "Hello, World!"
print(a[1])
print()
# Looping Through a String
b = """hello this is for loop in banana
this is example  """
for x in b:
    print(x)

# String Length

a = "Hello, World!"
print(len(a))

# Check String
txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if ("free" in txt):
    print(txt)

# Slicing
# Get the characters from position 2 to position 5 (not included):
b = "Hello, World!"
print(b[1:6])  # slice middle
print(b[:5])  # slice from start
print(b[2:])  # slice to last
print(b[-5:-2])  # native indexing

# Upper Case

a = "   Hello, World!   "
print(a.upper())

# Lower Case

print(a.lower())

# Remove Whitespace

print(a.strip())

# Replace String

print(a.replace("Hello","welcome"))

# Split String

print(a.split(","))

# String Concatenation

a = "Hello"
b = "World"
c = a + b
print(c)

# string Concatenation

a = "Hello"
b = "World"
c = a + " " + b
print(c)

# String Format

age = 36
txt = f"My name is John, I am at {age} {age} {age}"
print(txt)

# Placeholders and Modifiers

price = 59
txt = f"The price is {price} dollars"
print(txt)

price = 59
txt = f"The price is {59:.5f} dollars"
print(txt)

X = 20 * 59

txt = f"The price is {X:.2f} dollars"
print(txt)

# Escape Character

txt = "We are the so-called \"Vikings\" from the north."
print(txt)