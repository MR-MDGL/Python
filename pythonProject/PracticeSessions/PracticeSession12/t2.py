# create a student class with instance varables name age and grade add method display info to print student's name and grade
# create two objects and call with different data
class student():
    name='david'
    grade="A"
    def display_info(self):
        print(self.name,self.grade)

obj=student()
obj.display_info()