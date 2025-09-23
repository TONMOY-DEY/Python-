class BankAccount:
    balance=0
    account_number=0

class savingAccount(BankAccount):
  Account_holder="Mr.X"

class CurrentAccount(savingAccount):
    pass 

sa=CurrentAccount()
print(sa.balance)
print(sa.Account_holder)
print(sa.account_number)