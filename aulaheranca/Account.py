class Account():
    def __init__(self, number, holder, balance):
        self.number = number
        self.holder = holder
        self.balance = balance

    def deposit(self):
        amount = float(input("Deposit Amount: $"))
        self.balance += amount
        print(f"Deposit of ${amount} made successfully!")

    def withdraw(self):
        amount = float(input("Withdraw Amount: $"))
        if amount <= self.balance and amount > 0:
            self.balance -= amount
            print(f"Withdraw of ${amount} made successfully!")
        else:
            print("Amount greater than the limit")
