# Conditionals  Tutorial

# count = 0
# name = str(input("What is name "))
# for i in range(5, 11):
#     print(i)

count = 0
names = []
while count < 5:  
    name = str(input("What is your name? "))
    names.append(name)
    count += 1

for name in names:
    print(name + "  is awesome")



 

 