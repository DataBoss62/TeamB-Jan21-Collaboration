# user_funds = 10.31
# item_price = [11.0]

# if item_price[0] < user_funds:
#     print("You have enough money!")
# if item_price[0] == user_funds:
#     print("You have the precise amount of money")
# if item_price[0] > user_funds:
#     print("Sorry you don't have enough money")


def product(n):
    total = 1
    for n in n:       
        total *= n
    return total

print(product([4,4,5]))