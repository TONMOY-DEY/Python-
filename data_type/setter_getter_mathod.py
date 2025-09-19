class BankAccount:
    def __init__(self):
        self._balance=545

    @property
    def balance(self):  #read only // getter mathod
     return self._balance
    
    @balance.setter
    def balance(self ,amount):
       self._balance =amount
    

    
p1=BankAccount()
p2=BankAccount()

print(p1.balance)

p1.balance=15
print(p1.balance)



