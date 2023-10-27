class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account {self.account_number}: Balance ${self.balance}"


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number):
        if account_number not in self.accounts:
            account = Account(account_number)
            self.accounts[account_number] = account
            return account
        else:
            print("Account already exists.")
            return None

    def get_account(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]
        else:
            print("Account not found.")
            return None

    def transfer(self, from_account_number, to_account_number, amount):
        from_account = self.get_account(from_account_number)
        to_account = self.get_account(to_account_number)

        if from_account and to_account:
            if from_account.get_balance() >= amount:
                from_account.withdraw(amount)
                to_account.deposit(amount)
                print("Transfer successful.")
            else:
                print("Insufficient balance for transfer.")
        else:
            print("Unable to complete transfer.")


# Create a bank instance
bank = Bank()

while True:
    print("\nBanking Menu:")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transfer")
    print("5. Exit")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        account_number = input("Enter account number: ")
        bank.create_account(account_number)

    elif choice == '2':
        account_number = input("Enter account number: ")
        account = bank.get_account(account_number)
        if account:
            amount = float(input("Enter deposit amount: $"))
            account.deposit(amount)

    elif choice == '3':
        account_number = input("Enter account number: ")
        account = bank.get_account(account_number)
        if account:
            amount = float(input("Enter withdrawal amount: $"))
            account.withdraw(amount)

    elif choice == '4':
        from_account_number = input("Enter sender account number: ")
        to_account_number = input("Enter receiver account number: ")
        amount = float(input("Enter transfer amount: $"))
        bank.transfer(from_account_number, to_account_number, amount)

    elif choice == '5':
        print("Exiting the banking app.")
        break

    else:
        print("Invalid choice. Please try again.")
