
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
             
    def __init__(self,category):
        os.system('cls')
        self.category = category
        self.InitBalance = float(input(f'How much is your current {category} balance?\n'))
        self.main()

    def __repr__(self):
        return f" balance is {self.InitBalance}"
    

    def Deposit(self):
        self.deposit = float(input("\nHow much do you want to deposit?\n"))
        print("\nYour total deposit is £", self.deposit)
        self.incBalance = self.InitBalance + self.deposit
        print(f'\nYour total {self.category} balance now is £{self.incBalance}')

    
    def Withdraw(self):
        self.withdraw = float(input("\nHow much do you want to withdraw?\n"))
        print("\nYour total withdrawl amount is £", self.withdraw)
        self.decBalance = self.InitBalance - self.withdraw
        print(f'\nYour total {self.category} balance now is £{self.decBalance}')  

    def ctime (self):   
        self.timeStr = time.ctime()
        return(self.timeStr)

    def main(self):
        os.system('cls')  
        print(f'\nYour current {self.category} balance is \n£{self.InitBalance}')

        run = 1
        while run:
                main_option = int(input('\nChoose an option:\n1) Make a deposit\n2) Make a withdrawl\n'))
                if main_option == 1:
                    self.Deposit()
                    self.ctime()
                    self.bal1 = str(self.InitBalance) + " ," + self.timeStr +'\n'
                    self.trans1 = str(self.deposit) + " ," +self.timeStr +'\n'
                    self.final1 = str(self.incBalance) + " ," + self.timeStr +'\n'
                    run = 0
                elif main_option == 2:
                       self.Withdraw()
                       self.ctime()
                       self.bal1 = str(self.InitBalance) + " ," + self.timeStr +'\n'
                       self.trans1 = str(self.withdraw) + " ," + self.timeStr +'\n'
                       self.final1 = str(self.decBalance) + " ," + self.timeStr +'\n'
                       run = 0
                else:
                     run = 1
                     os.system('cls')
        os.system('pause')
        
          
food = Budget("food")
with open("food.txt", "w") as file1:
     file1.write(food.bal1) 
     file1.write(food.trans1) 
     file1.write(food.final1)
         
bills = Budget("bills")
with open("bills.txt", "w") as file1:
     file1.write(bills.bal1) 
     file1.write(bills.trans1) 
     file1.write(bills.final1)

clothes = Budget("clothes")
with open("clothes.txt", "w") as file1:
     file1.write(clothes.bal1) 
     file1.write(clothes.trans1) 
     file1.write(clothes.final1)    