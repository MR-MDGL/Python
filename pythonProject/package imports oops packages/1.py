#import package from another direcotary (inside module and packages file/import from different packages/module1 and module2)

import sys
sys.path.append(r"E:\BEBO-Tech\Python\pythonProject\module and packages\pak1")# r is for raw format

import amodule as m1
# import module2 as m2

ob=m1.Car()
ob.display()


# m1.display()
# m2.show()