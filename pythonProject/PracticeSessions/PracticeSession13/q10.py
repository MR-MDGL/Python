# 10. Create a class ShoppingCart to add, remove, and display items.  (use dictionary )

# ---------------------------------------------using list
class ShoppingCart():
    def __init__(self,*items):
        self.list1=list(items)

    def addProduct(self,*additem):
        for item in additem:
            if item not in self.list1:
                self.list1.append(additem)
                print('item added succesfully ')
    def display(self):
        print(f'items in your cart {self.list1} ')
        # print(type(self.list1))


    def removeitem(self,*removeItem):
        for item in removeItem:
            if item in self.list1:
                self.list1.remove(item)



#object and callings
# user1=ShoppingCart("apple watch")
# user1.display()
# user1.addProduct('mac')
# user1.display()
# user1.removeitem('mac')
# user1.display()

# hritik=ShoppingCart('laptop')
# hritik.display()
# hritik.addProduct('smartphone')
# hritik.addProduct('pc')
# hritik.display()
# hritik.removeitem('laptop','smartphone','pc')
# hritik.display()

