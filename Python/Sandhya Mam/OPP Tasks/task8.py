class Product:
    def __init__(self,product_name,product_id,price):
        self.name = product_name
        self.id = product_id
        self.price = price
    def details(self):
        print("PName:",self.name)
        print("PId:",self.id)
        print("Price:",self.price)

class ElectronicProduct(Product):
    def __init__(self, product_name, product_id, price,warranty_period):
        self.warranty = warranty_period
        super().__init__(product_name, product_id, price)
    def display_warranty(self):
        print("Warranty:",self.warranty)

class ClothingProduct(Product):
    def __init__(self, product_name, product_id, price,size):
        self.size = size
        super().__init__(product_name, product_id, price)
    def display_size(self):
        print("Size:",self.size)

E = ElectronicProduct("TV",10,5000,1)
E.details()
E.display_warranty()
print()
C = ClothingProduct("T-Shirt",4,100,"L")
C.details()
C.display_size()