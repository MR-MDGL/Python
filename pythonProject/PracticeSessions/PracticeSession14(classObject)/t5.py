class Laptop():
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def display(self):
        print(f'Hey user you have {self.brand} laptop model {self.model}')
l1=Laptop('ACER aspire 7','Ryzen 5 3550H')
l1.display()