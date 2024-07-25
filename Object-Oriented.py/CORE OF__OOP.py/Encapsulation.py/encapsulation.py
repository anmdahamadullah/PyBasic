

""" Encapsulation: Class and Object golor Kaj-kei Encapsulation bole."""



                                  #Ayyy shobiii Encapsulation......
class Student:
    name = "Ahamad Ullah"
    gpa = "4.50"
    age = 20
    location = "Bangladesh." #CLASS.

    def sat_value (self): #Value FUNCTION/METHOD....  
        self.name
        self.gpa 
        self.age
        self.location
    
    def display (self):  # Print__FUNCTION/METHOD....
        print(f"Name:{self.name},\nGPA:{self.gpa},\nAge:{self.age},\nLocation:{self.location}") 



Value = Student()   #Object.
Value.sat_value()  # Value Function CALL.
Value.display()   #Print Function CALL.
print("\nOthers Object=>\n")
Total_value = Student()   #Object.
Total_value.sat_value()  # Value Function CALL.
Total_value.display()   #Print Function CALL.

"""NOTE: OBJECT er Value Gola AKIII hobe,karon Super Class Orthat Main class Use Korsi.
 TAY different,different Value pawar-Jonno CONSTRUCTOR __init__ Use Korte HOBE......"""