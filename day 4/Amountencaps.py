class BankAccount:
    __balance=0
    def deposit(self,amt):
        self.__balance+=amt
    def withdraw(self,amt):
        if amt>self.__balance:
            print("Insufficient balance cannot withdraw")
        else:
            self.__balance -= amt
    def get_balance(self):
        return self.__balance
acc=BankAccount()
acc.deposit(20000)
acc.withdraw(10000)
print(f"Available balance is:{acc.get_balance()}")
class x(BankAccount):
   print(BankAccount().__balance)