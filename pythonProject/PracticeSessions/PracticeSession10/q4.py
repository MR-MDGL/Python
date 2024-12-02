# Write a function to calculate the area of a rectangle, given its length and breadth.
def calculateAreaOfRectangle(l,b):
    return l*b
l=int(input("enter length of rectangle"))
b=int(input("enter breadth of rectangle"))
print( calculateAreaOfRectangle(l,b))