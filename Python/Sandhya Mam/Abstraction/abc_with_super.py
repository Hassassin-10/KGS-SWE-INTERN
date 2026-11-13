from abc import ABC, abstractmethod

class Payment(ABC):
    def transaction(self):
        print("Payment transaction started")
    @abstractmethod
    def payment_mode(self):
        print("Hidden info")
class GooglePay(Payment):
    def payment_mode(self):
        print("Payment done through Google Pay")
        super().transaction()
class PhonePay(Payment):
    def payment_mode(self):
        print("Payment done through PhonePe")
        super().transaction()
g = GooglePay()
g.payment_mode()
p = PhonePay()
p.payment_mode()