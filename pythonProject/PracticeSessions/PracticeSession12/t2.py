# create a student class with instance varables name age and grade add method display info to print student's name and grade
# create two objects and call with different data
class student():
    name=''
    grade=''
    def display_info(self,name,grade):
        print(name,"grade",grade)

obj=student()
# obj.display_info()
obj.display_info('Sunil',"S")
obj.display_info('Satvinder',"S")