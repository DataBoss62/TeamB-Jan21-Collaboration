class Animal():
    def __init__(self, hasLegs, genus):
        self.hasLegs = hasLegs
        self.genus = genus

    def speak(self):
        return "Animal makes a noise "   
         

class Cat(Animal): # Cat object will inherit hasLegs attributes
    def __init__(self, name, breed, hasLegs, genus):
        super().__init__(hasLegs, genus)     # guiding the data to the Animal class 
        self.name = name
        self.breed = breed

cat1 = Cat("Tom", "Siamese", True, "feline")
print(cat1.name)
print(cat1.breed)
print(cat1.hasLegs)
print(cat1.speak())


