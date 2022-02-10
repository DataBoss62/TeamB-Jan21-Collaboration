class Student():

    def __init__(self, name, age, class_="student"):
        self.name = name
        self.age = age
        self.class_ = class_
        

    def __repr__(self):
        return f"{self.name} is {self.age} years old, and is in the class: {self.class_}."


    def gradeAvg(self, score1,score2,score3):
        result = int((score1 + score2 + score3)/3)
        self.avgScore = result
        return result

stud1 = Student("John", "21", "DFE")
stud2 = Student("Jane", "22","Software")
John = Student("John", "21", "DFE")
stud1.gradeAvg(88,90,74)
print(stud1)
print(stud1.avgScore)
print(getattr(John,"age"))





