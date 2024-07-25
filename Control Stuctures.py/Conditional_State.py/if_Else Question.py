



""" Q.1: Wap to check if a number entered by the user is odd or even.
     
    Q.2: WAP to find the greatest of 3 numbers entered by the user.

    Q.3: WAP TO check if a number is a multiple of 7 or not. 
"""

                   #1,Answer...    
num = int(input("Enter Number:"))   
rem = num % 2
                      #ODD and EVEN
if(rem == 0):
    print("EVEN")
else:
    print("ODD")
   

            
         #2nd Q...
a = int(input("Enter Frist Number:"))
b = int(input("Enter second Number:"))
c = int(input("Enter third Number:"))

if(a>=b and a>=c):
    print("Frist number is Largest",a)

elif(b>=c):
    print("Second number is Largest",b)
else:
    print("Thard number is Largest",c)




        #3rd..Q
x=int(input("Enter Number:"))

if(x % 7 == 0):
    print("Multiple Of Seven")
else:
    print("Not a Multiple Number")

