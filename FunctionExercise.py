# Conditionals  Tutorial



def Grade (homework, assessment, finalScore):
    answer = round((((homework + assessment + finalScore)/175) * 100))
    return answer


name = input("What is your name? ")
homework = int(input ("Enter homework score out of 25 "))
assessment = int(input("Enter assessment score out of 50 ")) 
finalScore = int(input("Enter final score out of 100 "))

finalGrade = Grade(homework,assessment,finalScore)

print (f"{name}, Your final ICT score is {finalGrade}%" )
 