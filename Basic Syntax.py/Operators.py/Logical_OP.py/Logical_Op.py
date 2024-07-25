
#Logical OP:-> [not, and, or] 

#example...not OP:- not Works against boolean values.বুলিয়ান মানের বিপরীতে কাজ করে..বুলিয়ান সত্য এবং মিথ্যা....TRUE, FALSE.
age = 40
marks =200
age = age < marks     #TRU..but Rullse in Boolean......False
marks = marks < age   #FALSE..but Rulles in Boolean.... True
print(not age)
print(not marks)

#Example..and OP:- and operator is true when both values ​are true.  and অপারেটর সত্য হয় যখন উভয় মান সত্য হয়.
val1 = 40
val2 = 40
value = val1 == val2 
print(value)
 
 #Example or OP:- The or operator is true when a value is true. or অপারেটর সত্য হয় যখন একটি মান সত্য হয়.
val1 = 90
val2 = 100
value = val1 < val2 or  val2 < val1
print(value)
