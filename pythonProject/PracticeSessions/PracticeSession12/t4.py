# # create class library with class variable total_books to keep track of total books in the library
# # create the method to increase the total number of books  when a new book is added
#
class Library:
    total_books = 0

    def total_book(self):
        print(f'total books are {Library.total_books}' )

    def add_books(self, added_books):
        Library.total_books+=added_books
        print(f"after adding books {Library.total_books}")

book1=Library()
book1.total_book()
book1.add_books(10)
book1.total_book()
