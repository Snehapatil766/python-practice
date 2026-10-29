
class BankAccount:
    counter = 1000

    def __init__(self, account_holder):
        BankAccount.counter += 1
        self.account_number = BankAccount.counter
        self.account_holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposited:", amount)
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount")
        elif self.balance >= amount:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance!")

    def display_balance(self):
        print("Account Holder:", self.account_holder)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)

    def transfer(self, amount, other_account):
        if amount <= 0:
            print("Invalid transfer amount")
        elif self.balance >= amount:
            self.balance -= amount
            other_account.balance += amount
            print("Transfer successful:", amount)
        else:
            print("Insufficient balance for transfer!")


# Create two accounts
a1 = BankAccount("Rahul")
a2 = BankAccount("Priya")

# Perform transactions
a1.deposit(5000)
a1.withdraw(1000)
a1.transfer(1500, a2)

# Display balances
print("\nAccount 1 Details:")
a1.display_balance()

print("\nAccount 2 Details:")
a2.display_balance()
