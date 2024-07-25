

#Create a Calculator......Using if,elif,else Statement

Operator = input("Choose An Operator:[+, -, *, /, **, %,]:")

num1 = int(input("Enter First Number:"))
num2 = int(input("Enter Second Number:"))
if(Operator == '+'):
    print("Your Value Is:",num1 + num2)
elif(Operator == '-'):
    print("Your Value Is:",num1 - num2)
elif(Operator == '*'):
    print("Your Value Is:",num1 * num2)
elif(Operator == '/'):
    print("Your Value Is:",num1 / num2)
elif(Operator == '**'):
    print("Your Value Is:",num1 ** num2)
elif(Operator == '%'):
    print("Your Value Is:",num1 % num2)
else:
    print("Your Choosing-Operator Is Wrong!!!!!")