# '''
# create class - budget
# create object based on category
# withdraw method
# deposit method
# transfer (method)
# print info to terminal

# '''

from budgetClasses import Budget

food = Budget(100)

entertainment = Budget(200)
entertainment.deposit(food.withdraw(45))

print()
print(food)
print(entertainment)

food.deposit(1000)
print()
print(food)


