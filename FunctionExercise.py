# Conditionals  Tutorial



def Grade (homework, assessment, finalScore):
    answer = (((homework + assessment + finalScore)/175) * 100)
    return round(answer,2)


name = input("What is your name? ")
homework = int(input ("Enter homework score out of 25 "))
while homework >25:
    print("invalid number, try again")
    homework = int(input ("Enter homework score out of 25 "))

assessment = int(input("Enter assessment score out of 50 ")) 
while assessment > 50:
    print("invalid number, try again")
    assessment = int(input("Enter assessment score out of 50 ")) 

finalScore = int(input("Enter final score out of 100 "))
while finalScore > 100:
    print("invalid number, try again")
    finalScore = int(input("Enter final score out of 100 ")) 

finalGrade = Grade(homework,assessment,finalScore)

if finalGrade >= 80:
    grade = "A"
elif finalGrade >= 70:
    grade = "B"
elif finalGrade >= 60:
    grade = "C"
else:
    grade = "F"

print (f"{name}, Your final ICT score is {finalGrade}% with a grade {grade}" )
print(f"{name} scored: {Grade(homework,assessment,finalScore)}")  # alternative
