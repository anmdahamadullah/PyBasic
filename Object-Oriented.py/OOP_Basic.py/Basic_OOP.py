"""




>>> OOP:Function Er Code Ke Reusability Baranoor-jonno Object oriented  Bebohar Kora Hoi........
     >>>> Rules >>>>>
>>> ক্লাস এবং অবজেক্ট.....
    1.ক্লাস: একটি Bluprint যা অবজেক্ট তৈরির জন্য ব্যবহৃত হয়। Class is a Blueprint,based on create Object.
    Bluprint: Ki Ki Feature Hobe.....(information) gola Class er Vhitore Likhbo...

    2.অবজেক্ট: একটি নির্দিষ্ট ইন্সট্যান্স যা ক্লাস থেকে তৈরি হয়। Class ke bebohar korbar jonnno toiri hoi...

           Syntax
class (#class name): #colon

s1 = (#classname)  #Object

>>> কনস্ট্রাক্টর (Constructor) হলো একটি বিশেষ মেথড যা কোনো ক্লাসের  Objet  তৈরি করার সময় স্বয়ংক্রিয়ভাবে কল করা হয়।

>>> কনস্ট্রাক্টরের প্রধান কাজ হলো অবজেক্ট তৈরি করার সময় প্রাথমিকভাবে কিছু ভ্যালু সেট করা। 

>>>  পাইথনে, কনস্ট্রাক্টরকে __init__ মেথড দ্বারা প্রতিনিধিত্ব করা হয়।

 
>>> ---> OOP-er Mool Vhitti... 4 tiiii.

   1.inheritance: Akti class-er boishistho Onno Kono Class-a Niye Asha Hoi...

   2.Abstraction: Unnecessary Jinish Goloke Lookiye Rakhe,important Jinish goloke Dekhai.
 
   3.Encapsulation: Class and Object golor Kaj-kei Encapsulation bole.

   4.Polymorphism: Akta Jinish ke Onek Poddotite bebohar korar namii Polymorphism.


>>> Methods:----->
    Three type of Methods............
    1.static method.
    2.instance method.
    3.class method.  
 


"""

class Person:
    # কনস্ট্রাকটর মেথড
    def __init__(self, name, age):
        self.name = name
        self.age = age                           #High Level......pore korbo

    # মেথড
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# অবজেক্ট তৈরি
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# মেথড কল করা
person1.display()
person2.display()
