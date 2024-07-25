
#Guess the number...GAME

import random    #Python _ Module: jekono random  jinish deyyyy........
target = random.randint(1,20)  #Jekonoo Random Number dibe...digit


while True:
    userChoice =input("Guess the target Number or Quit(Q) :") #User input
    if(userChoice == "Q"):
          print("-----Game Over-----")
          break
    userChoice = int(userChoice) #1-10 Integer value.....
    if (userChoice == target):
       print("------You Wine!!   Game Over------")
       break #loops Break..
    
    elif (userChoice < target):
      print("Your number was too small. Take a bigger guess.....")
    else:
     print("Your number was too big. Take a smaller guess.....")




