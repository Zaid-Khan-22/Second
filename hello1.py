
users = {
    "user": "user123",
    "pass": "pass@123"
}


username = input("Enter username: ")
password = input("Enter password: ")


if username in users and users[username] == password:
    print("Login successful ")
else:
    print("Invalid username or password ")
