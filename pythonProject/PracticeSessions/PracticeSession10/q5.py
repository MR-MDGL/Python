# Create a function that prints a pattern of stars in increasing order up to a given number of rows.
row=int(input("enter your rows"))
def pattern(n):
    for i in range (1,n+1):
        for j in range (i):
            print("*",end=" ")
        print()
pattern(row)