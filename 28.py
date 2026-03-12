class BankAccount:
    bank_name = "National Bank"
    total_accounts = 0
    total_bank_balance = 0

    def __init__(self):
        self.bank_name = "National Bank"
        self.total_accounts = 0
        self.total_bank_balance = 0

    def deposit(self, amount):
        self.total_bank_balance += amount
        print("Successful")

    def withdraw(self, amount):
        if self.total_bank_balance > amount:
            self.total_bank_balance -= amount
            print("Successful")
        else:
            print("Invalid Balance")

p = BankAccount()
while True:
    c = int(input("Enter"))
    if c == 1:
        a = int(input("Amount"))
        p.deposit(a)
    if c == 2:
        a = int(input("Amount"))
        p.withdraw(a)