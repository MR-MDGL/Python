# create a class car and print message when an object is deleated
class Car():
    def __init__(self,brand,model='not assigned'):
        self.brand=brand
        self.model=model

    def display_car_info(self):
        print(f'you have a {self.brand} {self.model}')
Tesla=Car('TESLA',"Model S")
Tesla.display_car_info()
print('Tesla.model is deleted successfully')
del Tesla.model
Tesla.display_car_info()

