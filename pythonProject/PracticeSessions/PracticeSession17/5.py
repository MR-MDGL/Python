# 5. Write a Python program to demonstrate how super() can be used to call a parent class
# constructor.
class Super():
    def __init__(self):
        print('constructor called of class Super')
class Sub(Super):
    def __init__(self):
        super().__init__()
        print('class sub')




obj=Sub()
# obj.display()
