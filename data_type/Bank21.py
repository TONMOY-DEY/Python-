class BankAccount:
    balance=0
    account_number=0

class savingAccount(BankAccount):
  Account_holder="Mr.X"

class CurrentAccount:
    pass 

sa=savingAccount()
print(sa.balance)
print(sa.Account_holder)