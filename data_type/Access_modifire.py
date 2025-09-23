class BankAccount:
    def __init__(self,owner,balance,pin):
        self.owner=owner #public
        self._balance=balance   #protected # ei kane _balance mane balance kae private kora rakha ore proteced kore rakha
        self.__pin=pin #private

    def varify_pin(self,pin):
            if self.__pin == pin:
                print("pin Matched")

            else:
                print("Wrong PIN.please try again.")


    def check_balance(self):
     print(self._balance)

ba1=BankAccount("Mr Nobody",500,1234)
print(ba1.owner)
ba1.varify_pin(2345)

# print(ba1._balance) #this is a wrong proses📢
print(ba1._BankAccount__pin)    #this is a wrong proces 📢