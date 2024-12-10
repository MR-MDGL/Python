# 7. Extend the Car class to include a method del_attr(a) that:
# - Deletes the attribute a if it exists.
# - Prints an appropriate message if the attribute doesn’t exist.

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def del_attr(self, a):
        if hasattr(self, a):
            value = getattr(self, a)
            delattr(self, a)
            print(f"Attribute '{a}' with value '{value}' has been deleted.")
        else:
            print(f"Attribute '{a}' does not exist.")

car = Car("Toyota", "Camry", 2020)

car.del_attr("model")
car.del_attr("car color")

print(vars(car))

