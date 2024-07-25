""" 



>>> To take input should be used:-->  input() function <---

RULE--------------------------------->>>>>
1.Integer = int(input(integer number))
2.Float = float(input(Float number))
3.String = input(String Words)-----> Because  Input always comes in "string"
"""


        #Integer....
age = int(input("Enter Your Age:")) #integer Input......
print("Your Age is:",age,"So..") #Condition....
if(age >=18): #Condition....
    print("You can Drive!")
elif(age < 18):#Condition....
    print("You can't Drive!")
print(type(age)) #Data Type..



        #String.....
name = input("\nEnter Your Name:?",)   #string Input.......
print("Your Name is:",name)
print(type(name)) #Data Type.
     


         #Float....
results = float(input("\nEnter Your HSC Results:"))  #float Input.....
print("Your Results Is:",results)
if(results == 5.00): #Condition...
    print("Welcome! You Got A+")
elif(results >= 2.00):#Condition...
    print("You Passed Exam")
elif(results < 2.00):#Condition...
    print("You Fail Exam!")
print(type(results))  #Dta Type.
