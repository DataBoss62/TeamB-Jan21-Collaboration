#  conditionals  If-then-elif


# var1 = int(input("Enter a number:  "))
# var2 = input("Please enter your name!")
# if var1 > 50 and var2:
#     print("Greater than 50!")
# else:
#     print("Less than 50!")


# age = int(input("Enter your age: "))
# if age >= 85:
#     print("You are above 85")
# elif age >= 50:
#     print("You are between 50 and 85")
# elif age >= 20:
#     print("You are between 20 and 50")
# else:
#     print("You are below 20 years old")

# score = int(input("Enter your exam score "))
# if score > 85:
#       print("Distinction")
# elif score > 65 :     
#       print("Pass")
# else:
#     print("Fail")


# score = int(input("Enter your exam score "))
# key = []
# if score > 85 : key = 1
# if score > 65 and score <= 85: key = 2
# if score <= 65 : key = 3
# print(key)
# Exam_Score = {
#                 1: "Distinction",
#                 2: "Pass",
#                 3: "Fail"
#              }
# print(Exam_Score[key])

# Iterations - While and For loops

# var1 = True
# while var1:
   
#     var1 = input("Do you want to continue?")
#     print("Var1 is currently true !!")

# control = 0
# while control <= 10:
#     print(f"control is : {control}")
#     control += 1  # same as control = control + 1


# running = 1
# while running:
#     print("Menu -1. print hello - 2. print goodbye - 0. exit")
#     input1 = int(input("Please choose an option  "))
#     if input1 == 1:
#         print("Hello)")
#     elif input1 == 2:
#         print("Goodbye")
#     elif input1 == 0:
#         running = False
#     else:
#         print("not a valid option! Try again.")


# list1 = ["tom", "Tim", "Tam"]
# str1 = "Hello world"
# for name in list1:
#     print(name)
# for name in str1:
#     print(name)
    
dict1 = {1:"Tom", 2:"Tim", 3:"Tam"}
for key, value in dict1.items():
    print(key)
    print(value)
    print("*****")

# range function
# range(10)   # will give numbers 0-9
# range(1,10) # will start at 1
# for num in range(1,11):  # prints 1- 10
#      print(num)

# for num in range(0,11,2):  # prints 0-10 , starting at 0 stepping up by 2 or -1 to step down
#      print(num)

list1= range(1,101)

# for num in list1:
#     if num == 13:
#        break        # this loop breaks at 13
#     else:
#        print(num)


for num in list1:
    if num == 13 or num == 50:  # this loop keeps going for all 100 numbers, skips printing for 13 and 50
       continue
    else:
       print(num)


# Nested loops
control1 = 0
control2 = 0

while control1 < 10:   # inner loop, loops 5 times, hands back to outer loop to complete 10 times
    control1 += 1
    print("control1 = " + str(control1))
    while control2 < 5:
        control2 += 1
        print("CONTROL2 = " + str(control2))

