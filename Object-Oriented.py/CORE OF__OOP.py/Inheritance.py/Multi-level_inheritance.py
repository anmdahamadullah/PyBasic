

#  Multi-level inheritance ==> Parents ba Base Class Theke 1st akta-Child Class create,
#  abong ay 1st Child Class theke Arekta 2nd  Child Class Create kora.

class phone:          # Parents ba Base Class.       
    def call(self):
        print("You can Call.") 

    def message(self):
        print("You can Message.")

    def game(self):
        print("You can Play Game.")

class copy_phone(phone):          # 1st CHILD Class.
    def copy(self):
       print("Welcome to Copy Phone!")


class Apple(copy_phone):           # 2nd CHILD Class.
    def apple(self):
        print("Welcome to Apple Phone Company!")
        

obj = Apple() #Shob gola call korsiiii.........
obj.call()
obj.message()
obj.game()
obj.copy()
obj.apple()