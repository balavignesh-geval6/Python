"""
Python Try Except
"""
x = 5 # if x is present try part is executed
try:
  print(x)
except:
  print("An exception occurred")

# print(y) code will stop after error

# if y is present except part is executed

try:
  print(y)
except:
  print("An exception occurred")

# specify the msg if variable is created or not for their error.
try:
  print(y)
except NameError:
  print("Variable y is not defined")
except:
  print("Something else went wrong")

print()

# else code will be executed if no error is found.
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

print()
try:
  print(x)
except:
  print("Something went wrong")
else:
  print("nothing wrong")
finally:
  print("The 'try except' is finished")

# print(d)