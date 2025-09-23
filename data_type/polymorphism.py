class BankAccount:
    def __init__(self):
        self._balance=10000
    
    def withdraw(self,amount):
        self._balance=self._balance-amount

    def check_balance(self):
        print("Current Balance:",self._balance)


class SavingAccount(BankAccount):
    def withdraw(self, amount):
        if self._balance < 10000:
           print("Withdrow failed")
        else:
            self._balance=self._balance-amount
           
sa=SavingAccount()
sa.withdraw(1000)
sa.check_balance()
sa.withdraw(90)