#F-Strings with curly brackets
age = 25
print(f"John is {age} years old")
print(f"John will be {age+10} years old in 10 years!")

# Escape characters
print("Hello, they call me \"Jeff\"")
print("Person 1: \tHey, how are you?\nPerson 2: \tGood thanks! \U0001F604")

#Strings
word1 = "Good"
word2 = "Day"
word3 = "John"
sentence = word1 + " " + word2 + " " + word3
print(sentence)

# Integers and Floats

number1 = input("Enter whole number: ")
number2 = input("Enter decimal number: ")

integer_number = int(number1)
float_number = float(number2)
round_number = int(round(float_number))

print(number1)
print(number2)
print(round_number)

# Boolean
name = "Pep Guardogiola"
age = 3
bark = True
tweet = False

print("My pet is called", name, ", He is", age, "years old.")
print("Statement:", name, "barks.", bark)
print("Statement:", name, "tweets.", tweet)
