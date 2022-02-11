
'''
create class - Budget
  init method
  attributes
  repr

name each object after the budget it's for
withdraw method
deposit method
testing lines of code


from operator import methodcaller

create class budget
start init method
some attributesset 



'''
import time
from datetime import datetime
import os
from turtle import clear

class Budget():
             
    def __init__(self,category):    # Ask user to enter their category budget
        os.system('cls')
        self.category = category
        self.InitBalance = float(input(f'How much is your current {category} balance?\n'))
        self.main()

    def __repr__(self):
        return f" balance is {self.InitBalance}"
    

    def Deposit(self):
        self.deposit = float(input("\nHow much do you want to deposit?\n"))    # user has chosen to add a deposit to their budget
        print("\nYour total deposit is £", self.deposit)
        self.incBalance = self.InitBalance + self.deposit
        print(f'\nYour total {self.category} balance now is £{self.incBalance}')

    
    def Withdraw(self):
        self.withdraw = float(input("\nHow much do you want to withdraw?\n"))  # user has chosen to withdraw from their budget
        print("\nYour total withdrawl amount is £", self.withdraw)
        self.decBalance = self.InitBalance - self.withdraw
        print(f'\nYour total {self.category} balance now is £{self.decBalance}')  

    def ctime (self):               # function to grab current date and time , no seconds
        self.timeStr = time.ctime()
        return(self.timeStr)

    def main(self):
        os.system('cls')  
        print(f'\nYour current {self.category} balance is \n£{self.InitBalance}')   # Ask user to enter current budget for the category 

        run = True
        while run:
                main_option = int(input('\nChoose an option:\n1) Make a deposit\n2) Make a withdrawl\n'))  # 2 options for given budget, deposit or withdraw
                if main_option == 1:
                    self.Deposit()
                    self.ctime()
                    self.bal1 = str(self.InitBalance) + " ," + self.timeStr +'\n'
                    self.trans1 = str(self.deposit) + " ," +self.timeStr +'\n'
                    self.final1 = str(self.incBalance) + " ," + self.timeStr +'\n'
                    with open(self.category+'.txt', "w") as file1:         # opens a txt file and writes the initial balance, transaction amount and final balance to it.
                        file1.write(self.bal1) 
                        file1.write(self.trans1) 
                        file1.write(self.final1)
                    run = False

                elif main_option == 2:
                       self.Withdraw()
                       self.ctime()
                       self.bal1 = str(self.InitBalance) + " ," + self.timeStr +'\n'   # appends the current date and time to the amount
                       self.trans1 = str(self.withdraw) + " ," + self.timeStr +'\n'
                       self.final1 = str(self.decBalance) + " ," + self.timeStr +'\n'
                       with open(self.category+'.txt', "w") as file1:         # opens a txt file and writes the initial balance, transaction amount and final balance to it.
                        file1.write(self.bal1) 
                        file1.write(self.trans1) 
                        file1.write(self.final1)
                       run = False

                else:                       # will go back to options if any other key (other than 1 or 2) is entered
                     run = True
                     os.system('cls')
        os.system('pause')
        
          
food = Budget("food")                      
        
bills = Budget("bills")

clothes = Budget("clothes")
 