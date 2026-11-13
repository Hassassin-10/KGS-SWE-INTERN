# Method Overriding diff class same method name same no of parameter

class Application:
    def payment(self):
        print("Payment is done")
class GooglePay(Application):
    def payment(self):
        print("payment is done through google pay")
        return super().payment()
class PhonePay(GooglePay):
    def payment(self):
        print("payment is done through Phone pay")
        return super().payment()
    
g = GooglePay()
p = PhonePay()
g.payment()
p.payment()