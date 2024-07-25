
 
# while True: #Condition....
#    user = input("\nEnter Your Selection ==> (1 For Rock, 2 For paper, 3 For scissor or (Q) for Quite Game)\n:")
#    if(user == 'Q'): #Quite Game
#     print("\nGame Is Over!!")
#     break
   
import random
user = random.randint(1,10)
comp = random.randint(1,10)
user2 = random.randint(1,10)
comp2 = random.randint(1,10) 
if(comp == user2):
  print("Draw")
elif(comp2 > user):
  print("Computer Wine")
elif(comp < user2):
  print("User Wine")
    




