import Account

class BussinessAcount(Account.Account):
    def __init__(self, number, holder, balance, loanlimit):
        super().__init__(number, holder, balance)
        self.loanlimit = loanlimit
    
    def loan(self):
        amount = float(input("Loan Amount: R$"))
        if amount > self.loanlimit:
            print(f"Loan refused! Value greater than the limit")
        else:
            print(f"Loan completed successfully!")
            self.balance += amount
            self.loanlimit -= amount