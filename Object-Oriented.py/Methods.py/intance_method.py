"""


>>> Normal Methods......"""

class Student_Info:
    def __init__(self,Name,Age,GPA,Location,College): # Ay Constructor Function  Value Rakhbe.....
        self.Name = Name
        self.Age = Age
        self.GPA = GPA
        self.Location = Location
        self.College= College

    def display(self):   #Ay Function Print Kore Dibe.....
        print(f"Name:{self.Name},\nAge:{self.Age},\nGPA:{self.GPA},\nLocation:{self.Location},\nCollege Name:{self.College}")
    



Object1 = Student_Info("Ahamad Ullah",20,"4.50","Bangladesh","Tamirul Millat")  #OBJECT..
Object1.display() #Print Function Call.
print("\nOthers Object\n")
Object2 = Student_Info("Habib Ullah",29,"5.00","CHINA","XDU")  #OBJECT..
Object2.display() #Print Function Call.
