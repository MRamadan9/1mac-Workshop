
import datetime
from time import sleep


class ATM():
    def __init__(self, balance, bank_name):
        self.balance = balance
        self.bank_name = bank_name
        self.withdrawals_time_list=[]
        self.withdrawals_list = []
        

    def withdraw(self, request):
        br = '-'*30

        print(br)
        print('<<< Welcome to ' + str(self.bank_name) + ' >>>')
        print('Your Current balance is  ' + str(self.balance))
        print(br)

        if request > self.balance:
            print('Can\'t give you all this money !!')
            return self.balance

        elif request < 0:
            print('More than zero plz!!')

        else:
            self.withdrawals_list.append(request)
            self.withdrawals_time_list.append(datetime.datetime.now().strftime('%a-%d-%b-%Y %H:%M:%S'))
            self.balance -= request
            time = datetime.datetime.now().strftime('%a-%d-%b-%Y %H:%M:%S')
            while request > 0:

                if request >= 100:
                    request -= 100
                    print('give 100 ' + time)

                elif request >= 50:
                    request -= 50
                    print('give 50 ' + time)

                elif request >= 10:
                    request -= 10
                    print('give 10 ' + time)

                elif request >= 5:
                    request -= 5
                    print('give 5  ' + time)

                elif request < 5:
                    print('give ' + str(request) + '  ' + time) 
                    request = 0
            print (br)
        return self.balance

    def show_withdrawals(self):
        for withdrawal in self.withdrawals_list:

            print ('Your withdraw list is   ' + str(withdrawal))
            sleep(5)




balance1 = 500
balance2 = 1000

atm1 = ATM(balance1,'Smart Bank', )
atm2 = ATM(balance2, 'Baraka Bank')

atm1.withdraw(277)
atm1.show_withdrawals()
atm1.withdraw(800)
atm1.show_withdrawals()
atm2.withdraw(100)
atm2.show_withdrawals()
atm2.withdraw(2000)
atm2.show_withdrawals()
