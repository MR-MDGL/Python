# 6. Write a Python program to demonstrate the use of public, protected, and private access specifiers.


# class Private:
#     __privatVar=12
#     _protected=13
#     public=14
#     def __privateM(self):
#         print("private methode")
#         print(self.__privatVar)
#     def _protectedM(self):
#         print("protected methode")
#         print(self._protected)
#     def publicM(self):
#         print("public methode")
#         print(self.public)
# o=Private()
# o._protectedM()
# o._Private__privateM()
# o.publicM()



class AccessSpecifiers:
    __private_var = 12
    _protected_var = 13
    public_var = 14

    def __private_method(self):
        print("This is a private method.")
        print(f"Private variable value: {self.__private_var}")

    def _protected_method(self):
        print("This is a protected method.")
        print(f"Protected variable value: {self._protected_var}")

    def public_method(self):
        print("This is a public method.")
        print(f"Public variable value: {self.public_var}")

obj = AccessSpecifiers()
obj.public_method()
obj._protected_method()
obj._AccessSpecifiers__private_method()

