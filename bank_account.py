class BankAccount:
    accounts = []
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount >= self.balance:
            self.balance -= 5
            print("Insufficient funds: Charging a $5 fee")
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        else:
            print("Negative account balance")
        return self

    @classmethod
    def print_account_info(cls):
        for account in cls.accounts:
            account.display_account_info()


primary = BankAccount(0.05, 20)
secondary = BankAccount(0.07, 50)

primary.deposit(1000).deposit(20).deposit(430).withdraw(500).yield_interest().display_account_info()
secondary.deposit(100).deposit(150).withdraw(20).withdraw(20).withdraw(20).withdraw(20).yield_interest().display_account_info()

BankAccount.print_account_info()