

#Write:  "w": লেখার জন্য (ফাইলটি আগেই থাকলে এটি মুছে ফেলে নতুন করে তৈরি করবে.......)


file = open("New.txt", "w")

file.write("My name is Ahamad Ullah,and My age is:20."
           "\nI Want to be a Good Artificial Intelligence Engineer."
           "\nI love Python language Programming")
file.close()
print("File Write done...")




      # Same File But Open with()........
with open("With.txt", "w")as f:#.......Syntax
       #Just f. Mode......
    f.write("My name is Ahamad Ullah,and My age is:20"
            "\nI Want to be a Good Artificial Intelligence Engineer.")



