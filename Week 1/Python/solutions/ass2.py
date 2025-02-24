#Create a program that allows the user to store names and phonenumbers 
# in alist of dictionaries
#The user can add a new contact and view all contacts
#Allow the user to search for a contact by name

contacts = []

num_of_contacts = int(input("Enter amount of contacts you want to add: "))

for i in range(num_of_contacts):
  name = input("Enter contact name: ")
  phone = input("Enter contact phone: ")
  contacts.append({
    "name": name,
    "phone": phone
  })

print("Your contacts are: ")
for contact in contacts:
  print(f"Name: {contact.get('name')}")
  print(f"Phone: {contact.get('phone')}")
  print("=" * 20)

search = input("Enter name to search: ")
search = search.lower()
print("Searching your contacts for:", search)

for contact in contacts:
  name = contact.get('name')
  if name.lower().find(search) != -1:
    print("Found contact:")
    print("Name: ", name)
    print("Phone: ", contact.get('phone'))
