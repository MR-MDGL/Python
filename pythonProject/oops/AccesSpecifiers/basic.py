# acces specifiers
# 3 (priveate,public ,protected)
class A():
    __a='private'       #accesed only inside this class
    b='public variable'     #accesed anywhere normally
    _c='protected variable'     #accesed only on to inherited classes not outside
    def displayPrivate(self):
        print('var is ',self.__a)
    def ab(self):
        print(self.__a)
class B(A):
    def show(self):
        print('var is ',self._c)
        print(f'var is {self.b}')
        # print(self.__a)

class C()

# ob=B()
# ob.show()
# ob.displayPrivate()
o=A()
o.displayPrivate()

obj=C()
print(obj.A.display())
