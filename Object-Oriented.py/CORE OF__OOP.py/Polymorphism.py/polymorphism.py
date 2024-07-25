"""




>>> Polymorphism: Akta Jinish/method-ke binno-binno Condition onojayii bebohar korar namii Polymorphism.
    JEMON=====>>OPERATOR OVER LOADING.........

>>> OPERATOR OVER LOADING:- Holo  ganitik  OP(+,  -, *,  /,  etc......) Ara  Binno-binno Condition-a Binno OUTPUT return kore thake.

>>>Python-A  Er-shathe 'DANDER FUNCTION' Use Korte hobe............"""




# EXAMPLE:-OPERATOR OVER LOADING------->>> 2,ta  Complex Number ER  JOG,BIYOG  korbo......
# NOTE:Amader  Logic Create Kore 'Dander function' Use korte hobe..........


class Complex:  #CLASS.
    def __init__(self,real,img): #All-Value Store Function. (plus and minus.. dander)
        self.real = real
        self.img = img

    def display(self):
        print(f"{self.real}i\t+\t{self.img}j")  # Plus Dander...Print Function.
                                                

    def display2(self):
        print(f"{self.real}i\t-\t{self.img}j")  # Minus Dander Print Function.
                                                
    #Dander FUNCTION...Plus(+) er jonno....
    def __add__(self,num2):             # Plus korbar jonno python a Already Structure kora ase..jeta holo Dander()... 
        Real_Number = self.real + num2.real      
        Imagine_Number = self.img + num2.img 
        return Complex(Real_Number,Imagine_Number)
    
     #Dander FUNCTION...Minus(-) er jonno....
    def __sub__(self,num2):            # Minus korbar jonno python a Already Structure kora ase..jeta holo Dander()... 
        Real_Number = self.real - num2.real   
        Imagine_Number = self.img - num2.img       
        return Complex(Real_Number,Imagine_Number)
    
    
print("...Plus Dander..")
num1 = Complex(600,800) # Value Pass OBJECT to CLASS.
num1.display() 
print("+\t\t+")
num2 = Complex(100,200)
num2.display()  #Print Call.

Num3 = num1 + num2   #Average Complex Number....
print("Average Complex Number Is:")
Num3.display() # Print CALL
print("\n")

print("...Minus Dander...")
Num4 = Complex(20,30)  #Value Pass OBJECT to Class.
Num4.display2()
print("-\t\t-")
Num5 =Complex(40,50)
Num5.display2()

Num6 = Num4 - Num5   #Minus Complex Number....
print("Minus Complex Number Is:")
Num6.display2() #Print CALL.
print("\n")

