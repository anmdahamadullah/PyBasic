

# Student Grad.....
      #Example.1



Student_marks=int(input("Enter Your Marks:  "))   #Input Marks.....

while True:
     if(100 < Student_marks):
      print("Your Marks Is Not Correct! Please Input Correct Marks:=>")
     break  #Hossena....Why....???????????

if(Student_marks >= 90 and Student_marks <=100):  #Condition......
     grad = "A+"
elif(Student_marks >= 80 and Student_marks <90):  #Condition......
     grad = "B"
elif(Student_marks>= 70 and Student_marks <80):   #Condition......
     grad = "A-"
elif(Student_marks >= 60 and Student_marks <70):  #Condition......
     grad = "B"
elif(Student_marks >= 50 and Student_marks <60):  #Condition......
     grad = "B-"
elif(Student_marks >=40 and Student_marks <50):   #Condition......
     grad = "C"
elif(Student_marks >= 30 and Student_marks <40):  #Condition...... 
     grad = "C-" 
else:
   print("You Fail!!")
Total_Great = grad
print("You Got--->",Total_Great)




        #Example.2
number=int(input("Enter Number 0 to 9:"  ))
if(number == 0):
     Value = "ZERO"
elif(number == 1):
     Value = "ONE"
elif(number == 2):
     Value = "TWO"
elif(number == 3):
      Value = "THREE"
elif(number == 4):
     Value = "FOUR"
elif(number == 5):
     Value = "FIVE"
elif(number == 6):
     Value = "SIX"
elif(number == 7):
     Value = "SEVEN"
elif(number == 8):
     Value = "Eight"
elif(number == 9):
     Value = "NINE"

else:
     print("You Wrong")
print("The Number Is:--->",Value)
        