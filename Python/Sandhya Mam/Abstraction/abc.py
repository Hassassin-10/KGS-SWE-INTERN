# ABC -> Abstract base class

from abc import ABC,abstractmethod

class Payment(ABC):
    @abstractmethod
    def transaction(self):
        pass
class GooglePay(Payment):
    def transaction(self):
        print("transaction done through gp")
class PhonePay(Payment):
    def transaction(self):
        print("transaction done through pp")
g = GooglePay()
p = PhonePay()
g.transaction()
p.transaction()