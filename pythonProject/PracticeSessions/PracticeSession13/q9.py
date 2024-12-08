# 9.Create a class BankAccount with methods to deposit, withdraw, and check balance

class BaknkAccount():
    def __init__(self,name,ballance):
        self.name=name
        self.ballance=ballance

    # if ballance==0:
    #     print("ammount is not sufficient")

    def deposit(self, add_money):
        self.ballance+=add_money
        print(f'{add_money} deposited successfully to your account ')
    def withraw(self,withdraw):
        if self.ballance<withdraw:
            print("insufficiant ballance ")
        else:
            self.ballance -= withdraw
            print(f'{withdraw} widthrawn successfully from your account')
    def finalballance(self):
        print (f'your have  {self.ballance} on your account')
a1=BaknkAccount('sunil',100)
a1.finalballance()
a1.withraw(101)
a1.finalballance()




# if we add withrown amount from bank account and amount isnt sufficnetn print insufficient ball error
