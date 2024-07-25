

#Q.1: WAP to ask user to enter names of their 3 favorite movies & store them a list.
movies = []
movi1 = input("Enter 1st movie:")
movi2 = input("Enter 2nd movie:")
movi3 = input("Enter 3rd movie:")

movies.append(movi1)
movies.append(movi2)
movies.append(movi3)

print(movies)



#Q.2:-> WAP to check if a list contains a Palindrom of elements.(Hint:use copy() method)

#Palindrome meanse:-  Jekhan thekei pori akii shobdo hobe.
#jemon:  madam,racecar..etc.. Example..

                                                          
list1=[1,2,1]       #[1,2,3] not palindrome                                          
copy1 = list1.copy()                                         
copy1.reverse()                                       
if(copy1 == list1):                                  
    print("Palindrome")
else:
    print("Not Palindrome")


                                                                     
list1=["m","a","d","a","m"]       #["m","a","d","a","m","p"] not palindrome                                          
copy1 = list1.copy()                                         
copy1.reverse()                                       
if(copy1 == list1):                                  
    print("Palindrome")
else:
    print("Not Palindrome")


           
           
           
           
           
           
           
           
