# define global variable and local variable inside a method of class example create a metod
# show_variables() to display value of both variables
a=1000
class Myclass():
    a=100

    def showvar(self):
        a=10
        print(a,"local")
        print(self.a,'instance')
        print(globals()['a'],"global")



obj=Myclass()
obj.showvar()