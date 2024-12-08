# Create a class Car with instance variable brand and model then create 3 obj  for diff cars and print their details
# with method car_info()

class car():
    def __init__(self,brand,colour):
        self.brand=brand
        self.colour=colour

    def car_info(self):
        print('brand',self.brand,'colour',self.colour)


obj=car("audi",'metalic black')
obj.car_info()

