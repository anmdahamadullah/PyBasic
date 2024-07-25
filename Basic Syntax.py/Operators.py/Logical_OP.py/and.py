"""
>>> and:=> and operator is true when both values are true. and অপারেটর সত্য হয় যখন উভয় মান সত্য হয়."""

val1 = 40
val2 = 40
Total_value = val1 == val2 #and OP
print("Logical Operator 'and' Is:",Total_value)
print(type(Total_value))

print("\n")


#Example....2
class Student:  #Class
    def __init__(self,name,age): # Value Store Function,and Instructor '__init__'.
        self.name = name
        self.age = age
    def display(self):
        print(f"Name:{self.name}\nAge:{self.age}") # Value Print Function.


class Student2:  #Class
    def __init__(self,name,age): # Value Store Function,and Instructor '__init__'.
        self.name = name
        self.age = age
    def display2(self):
        print(f"Name:{self.name}\nAge:{self.age}") # Value Print Function.




obj1 = Student("Ahamad",20) #OBJECT.......
obj1.display()

print("Logical 'and' Operator")

obj2 = Student2("Ahamad",20)
obj2.display2()

obj3 = obj1 == obj2   #Boolean Value.........         Hossena keno, Why??????????????
print("Logical Operator 'and' Is:",obj3)
