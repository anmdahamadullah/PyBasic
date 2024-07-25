"""
>>> Q2: Define a Employee class with attributes role,department & salary.
This class also showDetails() methods.
Create an Engineer class thats inherits properties from Employee & has additional attributer: name & age?

"""
#Poddoti=1/Method.1
class Employee: #Class
    def self1(self,role,dep,salary):#Store object Value...Function
        self.role = role
        self.dep = dep
        self.salary = salary
    def showDetails(self): #Print ..Function..........
        print(f"Role:{self.role} \nDepartment:{self.dep} \nSalary:{self.salary}")
   

class Engineer(Employee): #Inheritance....methods
    def __init__(self,name,age): #Store object Value.
        self.name = name
        self.age = age
    def showDetails2(self): #Print Value Function.
        print(f"Name: {self.name}\nAge:{self.age}")



e1 = Engineer("Ahamad","20") #OBJ.....
e1.showDetails2()
e1.self1("Manager","High","1,0000")
e1.showDetails()
print("\n\n")



# Ba Amnioooo Korte Pari....#Poddoti=2/Method.2
class Employee: #Class.
    def __init__(self,role,dep,salary): #Store object Value.
        self.role = role
        self.dep = dep
        self.salary = salary
    def showDetails(self): #Print....
        print(f"Role:{self.role} \nDepartment:{self.dep} \nSalary:{self.salary}")
   

class Engineer(Employee): #Inheritance....methods
    def __init__(self,name,age):#Store object Value.
        self.name = name
        self.age = age
        super().__init__("Engineer","IT","80,000") #Super/Parents Class-a Value Pass..
    def Display(self):
        print(f"Name:{self.name}\nAge:{self.age}") #Sho Name,Age..Function.....



eng1 = Engineer("Naeem","20") #OBJ.......
eng1.Display() #name & age..display......
eng1.showDetails()