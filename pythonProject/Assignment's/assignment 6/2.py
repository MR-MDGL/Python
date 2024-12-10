# 2.Write a Counter class with a class variable count to keep track of how many objects have been created
# Test this by creating multiple objects and printing the count
class Main():
    countobj=0
    def __init__(self):
        Main.countobj+=1
    def obcount(self):
        print(Main.countobj)
ob1=Main()
ob2=Main()
ob2.obcount()
