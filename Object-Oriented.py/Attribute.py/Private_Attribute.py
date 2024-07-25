
"""Private attribute: Jeta Akantoi private,Onno kew Access korte parena.
   Class er baire Access Hoina.
   
           Syntax..
attribute a Underscore-> _s_ <- Dilei Privat hoye jai."""



#Example: Bank Account Create.....

class Account:

    def __init__(self,acc_no,__accPass__):
        self.acc_no = acc_no
        self.__accPass__= __accPass__                   #Hossena  Keno???
    def display(self):
        print(f"Account Number:{self.acc_no},\nAccount Password:{self.__accPass__}")



obj = Account(123456,"Naeem")
obj.display()
