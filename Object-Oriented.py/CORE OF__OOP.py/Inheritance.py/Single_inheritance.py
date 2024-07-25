

#Single inheritance ==> Parents ba Base Class, Theke Akta Child Class/sub-class Create kora.


class phone:          # Parents ba Base Class.       
    def call(self):
        print("You can Call.") 

    def message(self):
        print("You can Message.")

    def game(self):
        print("You can Play Game.")


class copy_phone(phone):             #CHILD Class.
    def copy(self):
       print("Welcome to Copy Phone!! ")

Obj = copy_phone() # Child class diyeii shobaike call dilam.......
Obj.call()
Obj.message()          
Obj.game()
Obj.copy()


