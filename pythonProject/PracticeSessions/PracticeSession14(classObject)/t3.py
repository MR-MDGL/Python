


class Counter():
    objcount=0
    def __init__(self):
        Counter.objcount+=1
        # print(Counter.objcount)

    def noOfObj(self):
        print(f'total objects created {Counter.objcount}')
ob1=Counter()
ob2=Counter()
ob3=Counter()
ob4=Counter()
ob4.noOfObj()
