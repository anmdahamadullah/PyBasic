"""


>>> Class Attribute-goloor Value Change Korbar Jonnoi 'Class Method' Use Kora Hoi.
 

                             Syntax
                          @classmethod
                     def Attrib_name(class,Name)"""


class Person:#Class.
    Name = "Ahamad Ullah"
    @classmethod  #Static Method__ Syntax.
    def changeName(cls,Name):
        cls.Name = Name


P1 = Person() #Object.
P1.changeName("Habib Ullah")#Change Value..
print(Person.Name)

