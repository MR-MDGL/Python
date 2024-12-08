# 5. Create a class Animal and instantiate multiple objects to represent different animals.

class Animal():
    def __init__(self,animal):
        self.animal=animal
    def display(self):
        print(f'animal is {self.animal}')

a1=Animal("lion")
a1.display()
a2=Animal('tiger')
a2.display()

