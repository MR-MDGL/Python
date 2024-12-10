# 8. Create a Book class with:
# - A constructor to initialize t (title).
# - An overridden __del__ method to print a message when the object is deleted.
# - Demonstrate the deletion of a Book object.

class Book():
    def __init__(self,title):
        self.title=title
        print('constructor called ')

    def __del__(self):
        print(f'destructor deleted the ({self.title}) title')
ob1=Book('the alchemist')
# print(vars(ob1))
del ob1

