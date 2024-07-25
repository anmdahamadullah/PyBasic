

""" 
>>> Comments: Very Important in Program..
>>> We can Write All of, That We Want...but Remember!!!!!......................
>>> Comments: Thats Found program Mistake in  Line by line and  Remind Programs.

*Types Of Comments..
1. Single Line Comments:--> Use...'#'(Hash)

2.Multi-Line Comments:--> Use.... [""" """](Quotation)
"""

               #Comments...
Age=int(input("Enter Your Age:")) #input...
if(Age >= 18 and Age <= 40): #Condition
    print("Thanks! Fill out the next  step.")
    gender = input("\nEnter Your Gender:")       #Nesting: Writing if statement inside an if statement.
    if(gender == "male"):    #Condition          #Nesting: একটি if স্টেটমেন্টের ভিতরে অন্য if স্টেটমেন্ট লেখা।
         print("You Are Welcome! You Can Drive.")
    elif(gender == "female"): #Condition
         print("\nYou don't drive, you just cook.")
        
else: 
    print("You Can't Drive. Remember!!!  Age Should be... 18 < and  > 40")

