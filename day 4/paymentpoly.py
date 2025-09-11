class Payment:
    def pay(self,amount):
        print(f"Payment of amount {amount}")
class cashPayment(Payment):
    def pay(self,amount):
        print(f"Paid amount {amount} in cash")
class cardPayment(Payment):
    def pay(self,amount):
        print(f"Paid amount {amount} using credit/debit card")
class UPIPayment(Payment):
    def pay(self,amount):
        print(f"Paid amount {amount} using UPI")
payments=[cashPayment(),cardPayment(),UPIPayment()]
for x in payments:
    x.pay(1000)
