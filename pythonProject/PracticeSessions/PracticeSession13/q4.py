# Create a class Student with proerties name and marks. Modify and print the updated values.
class Students():
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
        print("constructor  called succesfully")
    def update(self,m1,m2):
        self.m1=m1
        self.m2=m2
        print(f"updated marks are {self.m1} and {self.m2}")
    def displaymarks(self):
        print(f"marks are {self.m1} and {self.m2}")
sunil=Students(89,99)
sunil.displaymarks()
sunil.update(100,100)


