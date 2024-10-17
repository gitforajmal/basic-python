#Class and OOP
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def getBio(self):
        print("I am a Person")

p1 = Person('Bob', 20)
print(p1)
print(p1.getName(), p1.getAge())

#Inheritance
class Student(Person):
    def __init__(self, name, age, schoolName):
        super().__init__(name, age)
        self.schoolName = schoolName
    def getSchool(self):
        return self.schoolName
    def getBio(self):
        print("I am a student")
        
s1 = Student("Adam", 10, "Elementary School")
s1.getBio()
print(s1.getSchool(), s1.getName(), s1.getAge())
