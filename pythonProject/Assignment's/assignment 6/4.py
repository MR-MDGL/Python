# 4. Write a Product class with:
# - Instance attributes for n (name) and p (price).
# - A class method set_d(cls, d) to set a discount for all products.
# - A method to calculate the final price after applying the discount.
class Product():
    def __init__(self,n,p):
        self.n=n
        self.p=p
        self.d=''

    def set_discount(self,d):
        self.d=d
        dis=(self.p * self.d) /100
        finalprice=self.p-dis
        self.p=finalprice
        print(f'final price of product {self.n} is {self.p} after applying {d}% discount')

ob1=Product('laptop',50000)
ob1.set_discount(30)
# ob1.final_price()

