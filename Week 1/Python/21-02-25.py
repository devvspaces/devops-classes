# Strings are arrays

# a = "Hello, World!"

# print(a[1]) # e

# print(a[2:5]) # llo
# print(a[:5]) # Hello
# print(a[:len(a)]) # Hello, World!
# print(a[:13]) # Hello, World!
# print(a[:]) # Hello, World!
# print(a[0:5:2]) # Hlo
# print(a[5:0:-1]) # ,olle
# print(a[::-1]) # !dlroW ,olleH
# print(''.join(list(a)[::-1])) # !dlroW ,olleH

# looper = iter("Cat")
# print(next(looper)) # C
# print(next(looper)) # a
# print(next(looper)) # t

# Looping through a string
# for <> in Y:
#     print(<>)

for x in "Cat":
  print(x)
print("Done")

print(len("Catdddddddddddddddddddddddddddddd")) # 3

txt = "The best things in life are free!"
print("Monkey" in txt)


# Lists
fruits = ["apple", "banana", "cherry"]
print(fruits[0]) # apple

fruits[0] = "kiwi"
print(fruits) # kiwi, banana, cherry

fruits.append("orange")
fruits.append("pineapple")
print(fruits) # kiwi, banana, cherry, orange, pineapple

fruit = fruits.pop()
print(fruit) # pineapple

fruit = fruits.pop(1)
print(fruit) # banana

for x in fruits:
  print(x)
  print(1 + 1)

numbers = [1, 2, 3, 4, 5]
squares = []

for num in numbers:
  squares.append(num ** 2)

print(squares)

# List comprehension
squares2 = [num ** 2 for num in numbers]
print(squares2)

# Sorting a list
x = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

print("Using sorted function:")
print(sorted(x))
print(x)

print("Using .sort method")
x.sort()
print(x)

a = 4
b = a

print("ID of a", id(a), a)
print("ID of b", id(b), b)

b = 5
print("ID of a", id(a), a)
print("ID of b", id(b), b)


c = [2, 4]
d = c

print("ID of c", id(c), c)
print("ID of d", id(d), d)

d[0] = 1
print("ID of c", id(c), c)
print("ID of d", id(d), d)

# Shallow copy
c = [2, 4]
# d = c.copy()
d = [x for x in c]

print("ID of c", id(c), c)
print("ID of d", id(d), d)

d[0] = 1
print("ID of c", id(c), c)
print("ID of d", id(d), d)

# Joining lists
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)

a.extend(b)
print(a)

# Calculator
a = input("Enter number: ")
b = input("Enter number: ")
print(int(a) * int(b))
