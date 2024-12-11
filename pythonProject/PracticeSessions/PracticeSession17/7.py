class A():
    def m1(self):
        print('class A')
class B(A):
    def m2(self):
        print('class B')
class C(B):
    def m3(self):
        print('class C')
o=C()
o.m1()
o.m2()
o.m3()