class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of {amount} successful. New balance is {self.balance}.")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawal of {amount} successful. New balance is {self.balance}.")
        else:
            print(f"Insufficient funds. Current balance is {self.balance}.")

    def view_balance(self):
        print(f"Current balance for account {self.name} is {self.balance}.")


def create_account():
    name = input("Enter your name: ")
    balance = float(input("Enter your initial balance: "))
    return BankAccount(name, balance)


def main():
    accounts = {}
    while True:
        print("1. Create new account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. View balance")
        print("5. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            account = create_account()
            accounts[account.name] = account
            print(f"Account created for {account.name} with initial balance {account.balance}.")
        elif choice == "2":
            name = input("Enter account name: ")
            if name in accounts:
                account = accounts[name]
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)
            else:
                print("Account not found.")
        elif choice == "3":
            name = input("Enter account name: ")
            if name in accounts:
                account = accounts[name]
                amount = float(input("Enter withdrawal amount: "))
                account.withdraw(amount)
            else:
                print("Account not found.")
        elif choice == "4":
            name = input("Enter account name: ")
            if name in accounts:
                account = accounts[name]
                account.view_balance()
            else:
                print("Account not found.")
        elif choice == "5":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
