# create a class book that overides the __str__ method to display book details
class Books():
    def __init__(self,bookname):
        self.bookname=bookname

    def __str__(self):
        return (f'book name is {self.bookname}')

b1=Books('The alchemist')
print(b1)

