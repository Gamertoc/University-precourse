class Person:
    name="noch kein Name"
    age=0
    eyeColor = ""

    def setName(self,x):
        self.name = x

    def setAge(self,x):
        self.age = x

    def setEyeColor(self,x):
        self.eyeColor = x

    def haveBirthday(self):
        self.age += 1

    def talk(self):
        print("My name is", self.name, "and I'm", self.age, "years old. My eye color is", self.eyeColor)
        
        
        
