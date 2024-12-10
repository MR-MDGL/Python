#create a class animal with method sound() then create classes Cat Dog and override sound() to their respective sounds
class Animal():
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        print('dog barks')
class Cat(Animal):
    def sound(self):
        print('cat meyows ')

ob1=Dog()
ob2=Cat()
ob1.sound()
ob2.sound()
