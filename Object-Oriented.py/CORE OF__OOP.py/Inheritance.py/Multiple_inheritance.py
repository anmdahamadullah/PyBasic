


#Multiple inheritance ==> Akadik ba Multiple Parents Class theke  Akta Child class create Kora.

class A:   #Parent class1
    def valueA(self):
        print("Well come to Class A")


class B:#Parent class2
    def valueB(self):
        print("Welcome to Class B")


class C:   #Parent class3
    def valueC(self):
        print("Welcome to class C")
        


class D:   #Parent class4
    def valueD(self):
        print("Welcome to class D")


class E(A,B,C,D):  #Child CLASS.  Shob-Parents class.
    def ValueE(self):
        print("Welcome to Class E")



Object =E()    #OBJECT....  Shob Class Call..........
Object.valueA()
Object.valueB()
Object.valueC()
Object.valueD()
Object.ValueE()




