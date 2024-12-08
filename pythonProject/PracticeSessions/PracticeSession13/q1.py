# create person with constructor that inintialise name and age and print details
class Person():

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display_person_info(self):
        print(self.name,self.age)
p1=Person('sunil',23)
p2=Person('satvinder',24)
p1.display_person_info()
p2.display_person_info()

