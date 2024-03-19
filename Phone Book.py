#Michelle Banwag
#Phone Book

phone_book = {}
def add_contact(name, number):
    phone_book[name] = number
    print("Contact added successfully.")

def look_up_contact(name):
    if name in phone_book:
        print( f"{name}'s phone number is {phone_book[name]}.")
    else:
        print("Contact not found.")

def delete_contact(name):
    if name in phone_book:
        del phone_book[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

while True:
    print("Phone Book:")
    print("1. Add contact")
    print("2. Look up contact")
    print("3. Delete contact")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        name = input("Enter contact name: ")
        number = input("Enter phone number: ")
        add_contact(name, number)

    elif choice == '2':
        name = input("Enter contact name: ")
        look_up_contact(name)
        
    elif choice == '3':
        name = input("Enter contact name: ")
        delete_contact(name)
    elif choice =='4':
        break
    else:
        print("Invalid choice. Please try again.")
