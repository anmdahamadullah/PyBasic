


#Nesting: Writing if statement inside an if statement.
#Nesting:  একটি if স্টেটমেন্টের ভিতরে অন্য  if স্টেটমেন্ট লেখা।

Age=int(input("Enter Your Age:"))
if(Age >= 18 and Age <=30):
    print("Thanks! Fill out the next  step")
    gender = input("Enter Your Gender:")         
    if(gender == "male"):                       
         print("You Are Welcome! You Can Drive")
    elif(gender == "female"):
         print("You don't drive, you just cook")
        
else: 
    print("You Can't Drive, Because Your age Is 30 <.....",Age)
