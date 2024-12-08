Author_name="Unknown"
class book:
    def book_info(self,title):
        print(f'title of book is { title } and author is  { Author_name } ')
    def set_book_info(self,set_author):
        print(f'title of book is { title } and author is  { Author_name } ')
        Author_name=set_author

obj1=book()
obj1.book_info("The alchemist")