  


# List:- Where multiple data are stored..যেখানে একাধিক ডেটা সংরক্ষণ করা হয়.
# All types of data can be stored inside the list.Lists-ভিতরে সব ধরনের DATA সংরক্ষণ করা যায়.Like...int,str,char....etc
#Note: List Is Mutable...(We can Change Value......)

""" Syntax... list Name = [] 'Third braket' """


#Example.1
print("Example:1")
Data = [20.5, 30,"Ahamad"]
print("Total Data:",Data)

#Example.2
print("\nExample:2")
Data = [20.5, 30,"Ahamad",]
print("Total Data:",Data)
Data[1]=90                  #List:-It can be Change Values....
print("Changed Data is:",Data)

#Example.3
print("\nExample:3")
Data = [20.5, 30,"Ahamad",]
print("Total Data:",Data)        #Lists Cliccing (Positive).....
print( "Clicing Data is:",Data[0:2])

#Example.4
print("\nExample:4")
Data = [20.5, 30,"Ahamad",]
print("Total Data:",Data)     #Lists Lenth......
print("Total Length:",len(Data))

#Example.5
print("\nExample:5")
Data = [20.5, 30,"Ahamad",]
print("Total Data:",Data)        #Lists Cliccing (Negetive).....
print( "Clicing Data is:",Data[-3:-1])




#List Have Function...........................
"""
1.list.append()  new value Joog kora...

2.list.sort() Value  shajanooo...
i,Accanding Sort: Small to Big...1,2,3,4,5,6,7,8,9.
ii,Deccanding Sort: Big to Small...9,8,7,6,5,4,3,2,1. :list.sort(reverse=True)

3.list.reverse() value   reverse-a  shajanoooo....

4.list.insert(3) :Jekoonoo perticular index a Value Add  kore..

5.list.remove(20)  :Je Value Input Kora Hoi sheii value Delete Kore.......Any input value are remove function..

6.list.pop(3)     :Jekonoo Index-A jeye Value Delete Kore.....
"""               