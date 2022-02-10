
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
import os
from turtle import clear
class Budget():
             
    def __init__(self,category):
        os.system('cls')
        self.category = category
        self.Initbalance = float(input(f'How much is your current {category} balance?\n'))
        self.main()

    def __repr__(self):
        return f" balance is {self.decBalance}"
    

    def Deposit(self):
        self.deposit = float(input("\nHow much do you want to deposit?\n"))
        print("\nYour total deposit is £", self.deposit)
        self.incBalance = self.Initbalance + self.deposit
        print(f'\nYour total {self.category} balance now is £{self.incBalance}')

    
    def Withdraw(self):
        self.withdraw = float(input("\nHow much do you want to withdraw?\n"))
        print("\nYour total withdrawl amount is £", self.withdraw)
        self.decBalance = self.incBalance - self.withdraw
        print(f'\nYour total {self.category} balance now is £{self.decBalance}')  
     

    def main(self):
        os.system('cls')  
        print("\nYour current total balance is \n£", self.Initbalance)
        self.Deposit()
        self.Withdraw()
        os.system('pause')
        
          
food = Budget("food")
clothes = Budget("clothes")
Bills = Budget("Bills")

print(f'\nYour {food.category}{food}\n')

print(f'Your {clothes.category}{clothes}\n')

print(f'Your {Bills.category}{Bills}\n')




