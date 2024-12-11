# 9. Create a class BankAccount that demonstrates encapsulation by having private attributes
# account_number and balance.provide method to deposit and withdraw money
class BankAccount():
    def __init__(self,accountnum,ball=0):
        self.__account_number=accountnum
        self.__ballance=ball
    def deposit(self,deposit_money):
        if 0 < deposit_money:
            self.__ballance+=deposit_money
            print(f'deposited {deposit_money} into your bank account')
        else:
            print('depost ammount should be in positive numbers')

    def withdrawMoney(self,withdraw_ammount):
        if withdraw_ammount > 0 and withdraw_ammount < self.__ballance:
            print(f'withdrawn of {withdraw_ammount} succesfully from your account')
        else:
            print('withdrawn should be in positive numbers only')
    def getAccountBallance(self):
        print(f'your current ballance is {self.__ballance}')
    def getAccountNumber(self):
        print(f'account number is {self.__account_number}')
c1=BankAccount(987654321,100)
c1.getAccountNumber()
c1.getAccountBallance()
c1.withdrawMoney(-2)
c1.withdrawMoney(20)
c1.deposit(40)
c1.getAccountNumber()
