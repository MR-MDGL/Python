# l. Create a parent class Vehicle with attributes like brand and model, Implement a sub class Car that adds attribute
# num_doors write methods to display both parent and child classes

class Vehicle():
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
class Car(Vehicle):
    def num_doors(self,num):
        self.num=num
        print(f'your car brand is {self.brand} model is {self.model} no of door it has {self.num}')
ob1=Car('Tesla','X')
ob1.num_doors(4)