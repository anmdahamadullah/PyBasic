

# Random Password Create.......
"""    
>>> import string ---->Module......Python _ Module: jekono random  jinish deyyyy........

# string.ascii_letters : Have all english latter small and bigger.

# string.ascii_lowercase: Just Small Latter.

# string.ascii_uppercase: Bigger Latter.

# string.digits: Just Arithmetic Digit.

# string.punctuation: punctuation (@~!"£$%.....")"""

import random #Python _ Module: jekono random  jinish deyyyy........
import string #Python _ Module: jekono random  jinish deyyyy........
pass_len = 6
charValues =(string.ascii_letters + string.punctuation + string.digits)

#list comprehension..jokhon kono function ke bar bar call kore value  goloke akta list-a stor korahoi.
#syntax..[function, loop]

# ["".join]: Ayy shob value ke join korbar jonno ba akta single list bananoor jonno use kore.
password ="".join([random.choice(charValues) for i in range(pass_len)]) #list akaree print korbar jonno...
print("Your Random Password Is:",password)






#Arekta poddoti.....Another Logic.............
import random #Python _ Module: jekono random  jinish deyyyy........
import string #Python _ Module: jekono random  jinish deyyyy........
pass_len = 6
charValues =(string.ascii_letters + string.punctuation +string.digits)

password = ""
for i in range(pass_len):  
   password += random.choice(charValues)
print("Your Random Password Is:",password)
