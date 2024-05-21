# F-Strings

txt = F"The price is 49 dollars"
print(txt)

price = 59
txt = F"The price is {price} dollars"
print(txt)


txt = F"The price is {price:.2F} dollars"
print(txt)

txt = f"The price is {95:.2f} dollars"
print(txt)

# operation

txt = f"The price is {20 * 59} dollars"
print(txt)


tax = 0.25
txt = f"The price is {price + (price * tax)} dollars"
print(txt)

txt = f"It is very {'Expensive' if price>50 else 'Cheap'}"

print(txt)

fruit = "apples"
txt = f"I love {fruit.upper()}"
print(txt)

def myconverter(x):
  return x * 0.3048

txt = f"The plane is flying at a {myconverter(30000)} meter altitude"
print(txt)