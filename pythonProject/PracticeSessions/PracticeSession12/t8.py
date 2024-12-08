# create a class counter with class variable count that keeps track of the number of objects created
# increment count each time an object is created and display the total number of objects created


class Myclass():
    obcount = 0

    def __init__(self):
        Myclass.obcount += 1
        # print("total objects created from Myclass count is ", Myclass.obcount)
    def show_obj_count(self):
        return(f'totoal object created { self.obcount }')

a = Myclass()
b = Myclass()
c = Myclass()
d = Myclass()
print(d.show_obj_count())

