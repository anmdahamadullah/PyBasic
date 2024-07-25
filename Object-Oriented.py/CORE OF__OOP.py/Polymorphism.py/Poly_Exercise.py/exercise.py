


 #New..........Example:(Average and Minus Value Count....)==============================================>>>>>>>>>>>>>>>>>>
class Complex:  #CLASS.
    def __init__(self,real1,real2): #All-Value Store Function. (plus and minus.. dander)
        self.real1 = real1
        self.real2 = real2


    def display(self):
        print(f"{self.real1} \t+\t{self.real2} ")  # Plus Dander...Print Function.
                                                
    def display2(self):
        print(f"{self.real1} \t\t{self.real2} ")  # Minus Dander Print Function.



    def display3(self):
        print("==>",f"\t{self.real2}","","","","<==") #Plus Korbar jonno....



    def display4(self):
         print("==>","","","",self.real1 - self.real2,"","","","","<==")  # Minus korbar jonno........


        #Dander FUNCTION...Plus(+) er jonno....
    def __add__(self,num2):             # Plus korbar jonno python a Already Structure kora ase..jeta holo Dander()... 
        Real_Number = self.real1 + num2.real1 + self.real2 + num2.real2 
        Imagine_Number = self.real2 + num2.real2 + self.real1 + num2.real1
        return Complex(Real_Number,Imagine_Number)
    

      #Dander FUNCTION...Minus(-) er jonno....
    def __sub__(self,num2):            # Minus korbar jonno python a Already Structure kora ase..jeta holo Dander()... 
        Real_Number = self.real1 - num2.real1
        Imagine_Number = self.real2 - num2.real2      
        return Complex(Real_Number,Imagine_Number)
    
    

print("\n...Plus Dander....")
num1 = Complex(100,100) # Value Pass OBJECT to CLASS.
num1.display() 
num2 = Complex(100,100)
num2.display()  #Print Call.

Num3 = num1 + num2 #Average Complex Number....
print("___________________")
print("Average Number Is:")
Num3.display3() # Print CALL
print("\n")



print("...Minus Dander...")
Num4 = Complex(2000,3000)  #Value Pass OBJECT to Class.
Num4.display2()
print("-\t\t-")
Num5 =Complex(1000,1000)
Num5.display2()

Num6 = Num4 - Num5 #Minus Complex Number....
print("____________________")
Num6.display2() #Print CALL.
print("The Minus Value is:")
Num6.display4()
print("\n")
