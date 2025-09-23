class AccountHolderInfo:
   person_name="MR A"

   def a(self):
      print("I am from Account Holder")

class BankAccount:
    balance=0
    account_number=0
    person_name="MR B"

    def b(self):
       print("I am from Bank Account Holder")

class savingAccount(BankAccount,AccountHolderInfo):
 pass

class CurrentAccount(BankAccount,AccountHolderInfo):
    pass 

sa=CurrentAccount()
# print(sa.balance)
# print(sa.Account_holder)
# print(sa.account_number)
# print(sa.person_name)
sa.a()
sa.b()