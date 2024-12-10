# # 5. Write a function play_sound(animal) that takes an object of any subclass of Animal and calls its sound() method. Create subclasses of Animal to demonstrate polymorphism.
# # 6. Define a base class Appliance with a method turn_on(). Create subclasses Washing Machine, Refrigerator, and Microwave that override the tum_on() method. Write a program
# # to demonstrate calling the method for different objects using a loop.
# # 7. Write a program with a base class Shape and subclasses Square, Triangle, and Circle. Implement a method draw in each subclass and demonstrate polymorphism
# # using a loop to call draw on a list of shapes.
# # 8. Create a class hierarchy for Transport with subclasses Airplane, Ship, and Car. Each subclass should override a method move(). Write a program to demonstrate polymorphism.
# class Animal():
#     def sound(self):
#         pass
# class Dog(Animal):
#     def sound(self):
#         print('bark bark')
# class Cat(Animal):
#     def sound(self):
#         print('mew mew')
# def play_sound(animal):
#     print(animal)


# multiple inheritance 2 parent 1 child
class A():
    def m1(self):
        print('class a')


class B(A):
    def m1(self):
        super().m1()
        print('overided m1')


ob = B()
ob.m1()