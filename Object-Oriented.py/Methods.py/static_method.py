"""



>>> Koono Object Sara Class-er Modde Decorator-er Maddome Kaj Kore.

             Syntax
            --------- 
         @staticmethod
         def 'Attribute Name'():
             print("something")"""

class Info:#Class.
    def __init__(self,name,age): #Value Store  function.
        self.name = name 
        self.age = age
        
    def display(self):
        print(f"Name:{self.name}\nAge:{self.age}") #Value Print Function.

    @staticmethod #Static Method............
    def hello ():
        print("Hello! I am Static method")


p = Info("Naeem",20)
p.display()

Info.hello() #Static Method Call Without Object.......





