contacts = {}

while True:
    print("1 Add Contact")
    print("2 Search Contact")
    print("3 Delete Contact")
    print("4 Display Contacts")
    print("5 Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        name = input("Enter name: ")
        num = input("Enter number: ")
        contacts[name] = num
        print("Contact saved")

    elif ch == 2:
        name = input("Enter name to search: ")
        if name in contacts:
            print("Number:", contacts[name])
        else:
            print("Not found")

    elif ch == 3:
        name = input("Enter name to delete: ")
        if name in contacts:
            contacts.pop(name)
            print("Deleted")
        else:
            print("Not found")

    elif ch == 4:
        if len(contacts) == 0:
            print("No contacts")
        else:
            for i in contacts:
                print(i, ":", contacts[i])

    elif ch == 5:
        break

    else:
        print("Wrong choice")
