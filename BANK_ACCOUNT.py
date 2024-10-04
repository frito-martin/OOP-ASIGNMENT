class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited:{amount}. New balance: {self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance:   {self.balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def check_balance(self):
            print(f"Your current balance is: {self.balance}")

account1 = BankAccount("muzei", 1000)
account2 = BankAccount("mary")

# Test the methods
account1.deposit(500)
account1.withdraw(200)
account1.check_balance()

account2.deposit(100)
account2.withdraw(200)  
account2.check_balance()
