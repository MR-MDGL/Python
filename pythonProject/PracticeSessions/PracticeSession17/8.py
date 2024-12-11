# 8. Write a program to show how the is instance() function can be used with inheritance.
class A():
    pass
class B():
    pass
o=B()
print(isinstance(o,A))
print(isinstance(o,B))