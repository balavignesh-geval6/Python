"""
RegEx in Python
"""

import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")

# findall() Function

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())


txt = "The rain in Spain"
x = re.split('\s', txt)
print(x)

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)


x = re.sub("\s", "9", txt, 2)
print(x)

x = re.search("ai", txt)
print(x) #this will print an object