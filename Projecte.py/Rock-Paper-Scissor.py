import random # Random Value Module....
""" 
_____________ROCK,PAPER,SCISSOR_______________
                 RULES
>>> Rock vs paper-------====>----Winner is.....Paper.
>>> Rock vs Scissor-----====>----Winner is......Rock.
>>> Scissor vs Rock-----====>----Winner is.....Rock.
>>> Scissor vs Paper----====>----Winner is.....Scissor.
>>> Scissor Vs Scissor--====>----DRAW Game.
>>> Rock Vs Rock--------====>----DRAW Game.
>>> Paper Vs Paper------====>----DRAW Game.
"""

 
while True: #Condition....
   user = input("\nEnter Your Selection ==> (1 For Rock, 2 For paper, 3 For scissor or (Q) for Quite Game)\n:")
   if(user == 'Q'): #Quite Game
    print("\nGame Is Over!!")
    break

   comp = random.randint(1,3) # 1 to 3 Random Value...

   user = int(user) # Input-nibe abong Return Korbe 'Integer value'......
   
   if(user == 1 and comp == 1):
    print("You select :=>'Rock'","\nComputer select :=>'Rock'") #Show => 'User and Computer Values'
    print("Rock == Rock")
    print("____Its time Draw! Try again____\n")
   elif(user == 2 and comp == 1):
    print("You select :=> 'Paper' :","\nComputer select :=>'Rock' :") #Show => 'User and Computer Values'
    print("Paper > Rock")
    print("_____Great!!  You Wine_____\n")
   elif(user == 3 and comp == 2):
    print("You select :=> 'Scissor'","\nComputer select :=> 'Paper'") #Show => 'User and Computer Values'
    print("Scissor > Paper")
    print("_____Great!!  You Wine_____\n")
   elif(user == 1 and comp == 3):
    print("You select :=> 'Rock'","\nComputer select :=> 'Scissor'") #Show => 'User and Computer Values'
    print("Rock > Scissor")
    print("_____Great!!  You Wine_____\n")
   elif(user == 2 and comp == 2):
    print("You select :=> 'Paper'","\nComputer select :=> 'Paper'") #Show => 'User and Computer Values'
    print("Paper == Paper")
    print("_____Its time Draw! Try again_____\n")
   elif(user == 1 and comp == 2):
    print("You select :=>'Rock'","\nComputer select :=> 'Paper'") #Show => 'User and Computer Values'
    print("Rock < Paper")
    print("____You loss!!Computer Wine____\n")
   elif(user == 3 and comp == 1):
    print("You select :=>'Scissor'","\nComputer select :=> 'Rock'") #Show => 'User and Computer Values'
    print("Scissor < Rock")
    print("_____You loss!!Computer Wine_____\n")
   elif(user == 3 and comp == 3):
    print("You select :=> 'Scissor'","\nComputer select :=> 'Scissor'") #Show => 'User and Computer Values'
    print("Scissor == Scissor")
    print("_____Its time Draw! Try again_____\n")
   elif(user == 2 and comp == 3):
    print("You select :=> 'Paper'","\nComputer select :=> 'Scissor'") #Show => 'User and Computer Values'
    print("Paper < Scissor")
    print("_____You loss!!Computer Wine_____\n")
   else:
    print("______Your Input-Value is Wrong!!!______\n")
   

     
 
