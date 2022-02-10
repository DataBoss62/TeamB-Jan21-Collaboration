class Dog():
    def __init__(self,name):       # must have this with a def
        self.name = name

    def __repr__(self):
        return f"this string shows: {self.name}"

    def speak(self):
        return f'{self.name} says "woof"'
    

dog1 = Dog("Spot")
dog2 = Dog("Fido")
dog3 = Dog("TuTu")
dog4 = Dog("Jack")


# print(dog1.name)    # not required after second def statement
# print(dog2.name)
# print(dog3.name)
# print(dog4.name)

print(dog1.speak())
print(dog1)
print(dog2)
print(dog3)
print(dog4)