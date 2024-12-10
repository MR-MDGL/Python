class Mycar():
    def __init__(self,brand,colour):            #constructor
        self.brand=brand
        self.colour=colour

    def car_info(self):
        return (f'you have a {self.brand} and its an amazing {self.colour} colour with premium look')


class ElectricCar(Mycar):               #passing Mycar into Eleccar is inheritance
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

    






my_tesla=ElectricCar('Tesla','Model S','85 kwh ')
# print(my_tesla.car_info())
print()

# bmw=Mycar("bmw",'red')      #passing values to class
# print(f'its a {bmw.colour} {bmw.brand} and its damm gorgeous')
# print(bmw.car_info())

