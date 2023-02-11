def details():
    name = input("Enter your name: ")
    number = int(input("Enter your account number: "))
    ac_type = input("Fixed\nSavings\nCurrent\nEnter your account type: ")
    print("Name:", name)
    print("Account number:", number)
    print("Account Type:", ac_type)


class BankAccount:

    def __init__(self):
        self.balance = 0
        print("Hello!! welcome to the Deposit and Withdrawal machine")

    def deposit(self):
        amount = float(input("Enter the amount to be deposited: "))
        self.balance += amount
        print("\n Amount Deposited:", amount)

    def withdraw(self):
        amount = float(input("Enter amount to withdraw: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\n You withdrew:", amount)
        else:
            print("\n Insufficient Balance")

    def display(self):
        print("\n Net Available Balance=", self.balance)


s = BankAccount()

details()
s.deposit()
s.withdraw()
s.display()