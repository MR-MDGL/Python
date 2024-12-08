# 5. Create a Car class with:
# - An instance variable b (brand).
# - A class variable w (wheels) initialized to 4.
# - A method show() to print both b and w.

class Car():
    def __init__(self,b,w=4):
        self.w=w
        self.b=b
    def display(self):
        print(f'your brand is {self.b} wheels it has {self.w}')
ob1=Car('tesla')
ob1.display()