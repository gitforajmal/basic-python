print ("Hello World!", "Welcome to Python")
age = 10,21
sc1, sc2 = 24,26
print (age)
print (sc2)
print (sc1+ sc2)
print ( age[1], age)
print("I am", "Ajmal")
print(f"The sum is {10+20}")
print(f"{sc1}")
print(f"1. {(15+30)/2}") #formatted string
a1, a2= 10,15
print(a1+a2)
print(a1-a2)
print(a1*a2)
print(a1/a2)
print(a1%a2)
print ("Hi" * 10)
se = "Ajmal is a developer"
print(se[0:6]) #substring
#Arrays
products = ["apples", "banana", "orange", "Pear"]
print(products)
products.append("grapes")
products[3]= "Avocado"
print(products)
del products[3]
print(products)
print(len(products))
veggies = ["Pepper", "Beans"]
#Combine Array
print(products + veggies)
list = [23,12,43,42,54]
print("length", len(list), "Min ", min(list), "Max ", max(list))
#Dictionary
students = {"Adam": 8, "Idris": 7, "Nouh": 9}
print(students)
print(students['Adam'])
students['Nouh'] = 10
print(students)
del students['Nouh']
print(students)
#Tuples
tupp = ("an", "bat", "cat")
print(tupp)
tupp2 = (1,2)
print(tupp + tupp2)

#Conditional operation
age = 19
if age < 13:
    print("In If")
    print("condition")
    print("Child")
elif age >=13 and age < 18:
    print("Teen")
else:
    print("Adult")
    
#For Loop
flist = ['one', 'two','three','four']
for item in flist:
    print (item)
for i in range(3,6):
    print (i)
for i in range(0,10,3):
    print (i)
#While Loop
c =10
while c < 15:
    c = c+1
    if c==3:
        pass    #break, continue, pass are control statements in while loop
    print (c)
# Try - Except
try:
    if snm < 2:
        print(snm)
except:
    print("Error in Block")

#Function
def addNum(a, b):
    print(f"sum is {a+b}")
    return a + b

sumN = addNum(10,20)
print ("sum v", sumN)

print(dir('hello'))
print (help('hello'.split))
print("Conversion of type ", int("35") + 15)

print("End of Basics")
