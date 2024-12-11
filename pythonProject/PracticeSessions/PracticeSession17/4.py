# 4. Implement a class Product with private attributes price and stock. Use getter and setter
# methods to ensure the price and stock values cannot be negative.
class Product:
    def __init__(self,price,stock):
        self.__price=price
        self.__stock=stock
    @property
    def price(self):
        print(self.__price)
    @property
    def stock(self):
        print(self.__stock)
    @price.setter
    def price(self,new_price):
        if 0 < new_price:
            self.__price=new_price
        else:
            return 'price cant be 0 or less'
    @stock.setter
    def stock(self, new_stock):
        if 0 < new_stock:
            self.__price = new_stock
        else:
            return 'stock cant be 0 or less'
    def display(self):
        print(f'price is: {self.__price}\nstock is: {self.__stock}\n')
o=Product(99,20)
o.display()
o.price=200
o.stock=10
o.display()