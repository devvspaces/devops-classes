# Favorite food list
# Create a program that allows  the user to input their favorite foods
# Store these foods in a list and then display them back to the user.
# Allow the user to remove a food from the list and display the updated list

fav_food=[]

# for i in range(4):
#   food=input('Enter food item: ')
#   fav_food.append(food)

while True:
  food=input('Enter food item: ')
  if food == "":
    break
  fav_food.append(food)

print('Your favourite foods are', fav_food)

remove_food = input("Enter the food item you want to remove: ")

rm_index = fav_food.index(remove_food)
fav_food.pop(rm_index)

print("Item has been removed, the remaining foods are:", fav_food)
