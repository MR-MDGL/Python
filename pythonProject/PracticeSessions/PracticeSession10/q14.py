# 14.	Implement a nested function that demonstrates how inner functions can access variables from the outer function.

def outer_func(a):
    print("Outer function called",a)

    def inner_func(inner_var):
        print("Inner function",inner_var)

        print("Calling outer inside inner:",a)
    inner_func(4)
outer_func(45)