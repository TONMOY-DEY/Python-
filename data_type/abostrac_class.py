from abc import ABC,abstractmethod



class BankAccount(ABC):
    def __init__(self):
        self._balance=11000

    @abstractmethod
    def withdraw(self,amount):
        self._balance=self._balance-amount

    def check_balance(self):
        print(self._balance)

class SavingAccount(BankAccount):
    def withdraw(self,amount):
        if (self._balance -amount) < 11000:
            print("Withdraw Field")

        else:
            self._balance=self._balance-amount

sa=SavingAccount()
sa.withdraw(5000)
sa.check_balance()



