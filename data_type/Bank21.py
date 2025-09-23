class BankAccount:
    balance=0
    account_number=0

class savingAccount(BankAccount):
    pass

class CurrentAccount:
    pass 

sa=savingAccount()
print(sa.balance)