# 1. Create a program to demonstrate how the issubclass() function works with inheritance.

# 5. Write a Python program to demonstrate how super() can be used to call a parent class
# constructor.
# 6. Write a Python program to demonstrate the use of public, protected, and private access specifiers.
# 7. Create a program to show hierarchical inheritance with a base class Vehicle and derived classes Car and Bike.
# 8. Write a program to show how the is instance() function can be used with inheritance.
# 9. Create a class BankAccount that demonstrates encapsulation by having private attributes account_number and balance. Provide methods to deposit and withdraw money.
# 10. Implement a program to show how to prevent instantiation of an abstract class.
class A():
    print('class A')
class B(A):
    print('class B')
print(issubclass(B,A))
