"""
Python If ... Else
"""

a = 33
b = 200
if b > a:
  print("b is greater than a")

# Elif
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

# Else
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")


if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

# Short Hand If
if a > b: print("a is greater than b")

# Short Hand If ... Else
print("A") if a > b else print("B")

# Nested If
if a > 10:
  print("Above ten,")
  if b > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

# The pass Statement
if b > a:
  pass