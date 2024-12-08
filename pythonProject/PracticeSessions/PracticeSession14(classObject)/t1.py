
class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def carInfo(self):
        print(f'Hey sir you are driving a {self.make} model {self.model} manufactured on {self.year}')

    def startEngine(self):
        print('engine is started')


car1=Car('Mitsubishi Motors','X',2024)
car1.carInfo()
car1.startEngine()