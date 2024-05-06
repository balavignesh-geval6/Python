"""
Boolean Values
"""

print(10 > 9)
print(20 != 10)
print(10 < 9)
print(20 == 20)
print("\n")
#  Print a message based on whether the condition is True or False:
print()
print("Print a message based on whether the condition is True or False:")
a = 120
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# Evaluate Values and Variables

print(bool("Hello"))
print(bool(15))
print(bool(""))
print(bool(0))
print(bool(False))
print(bool())

print("\n")


class myclass():
    def __len__(self):
        return 1


myobj = myclass()
print(bool(myobj))


# Functions can Return a Boolean

def myFunction():
    return True


print(myFunction())

if (myFunction() == False):
    print("YES!")
else:
    print("NO!")

# Check if an object is a fixed data type

x = 200
print(isinstance(x, int))

print(isinstance(x, str))

x = "hello"
print(isinstance(x, str))

print("\n")
x = 20.225
print(isinstance(x, float))