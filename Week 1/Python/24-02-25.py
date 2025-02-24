thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "colors": ["red", "white", {"hex": 1, "cols": [[[[["father"]]]]]}],
}

print(thisdict.get("age"))
print(thisdict)

# len
print(len(thisdict))

# type
print(type(thisdict))

new_dict = dict() # {}
new_dict['str'] = 12
new_dict['str'] = 34
new_dict['strasdad'] = 34
print(new_dict)

thisdict.update({
  'brand': 'Toyota'
})
thisdict['brand'] = 'Toyota'

thisdict.setdefault('brand', 'Lambo')
thisdict.setdefault('brand2', 'Lambo')
print(thisdict)

print(thisdict.popitem())

print(thisdict.pop('colors'))

print(thisdict)

for key, value in thisdict.items():
  print(f'{key}={value}')

# If Else
a = int(input("Enter a value: "))

if a > 100:
  print("A is greater than 100")
elif a > 80:
  print("A is greater than 80 but less than or equal to 100")
else:
  print("A is less than 80")

# While

for i in range(4):  # 0, 1, 2, 3
  print(i)

i = 0
while True:
  if i == 10000:
    break
  print(i)
  i += 1

