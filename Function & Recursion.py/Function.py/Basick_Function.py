

"""Function is a block of statement thats performs a specific task.
.....>Type of Function()...
Two type of Function......
1.Build-in Function: All-ready have Function in Python..
i,print()
ii,len()
iii,type()
iv,range()
etc.......

2.User define Function:  User can be creating. 

              Syntax
   --------------------------------
   def (function name) parameter(a,b):  
        return ফলাফল ফেরত দেওয়া.   
"""
                                          
def calculate_sum(a, b):   #Function Definition.
    return a + b       #a,b:---> Parameter.
                                       
sum = calculate_sum(10,20)  #Function Call.
print(sum)              #10,20:----> Argument.
print(type(calculate_sum))


