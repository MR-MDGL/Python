# functions day2

# arguments
# positional keyword and default
# -------------------------------
# *args------       positional variable length argument     gives output in a tuple
#       allow fun to accept any no of positional argument which will be passed as a tupel to the function

# def greet(*name):
#     print('hellow',name)
#
# greet("david")
# greet("john","merry","bob")

#
#------------------------------ **kwargs function to accept any no of argument's
# arguments passed as a key value pair
# def student_info(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key} {value}")
#
# student_info(name="sunil",id='007')



# example 3             #using both at same time
# def display_info(*args,**kwargs):
#     print("positional arguments are",args)
#     print("keyword arguments",kwargs)
# display_info(1,2,3,4,5,name="sunil",age="23")

# example4                  # using default with args
# def greet(name,*args):
#     print(name,args)
# greet('suil',"aman","satvinder","akshat")



# example5              # --using all three into one
def greet(name,*args,**kwargs):
    print(name)
    for i in args:
        print(i)
    for i,j in kwargs.items():
        print(i,j)
greet('suil',"aman","satvinder","akshat",name1='sunil',age='23')


