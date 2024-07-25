


Tup = (10,21,23,22,"USD$","Banana","Apple","Potatoes")
X = "Potatoes" #খুঁজতে হবে ..Find TheValue...
idx =0  #Index...
while idx < len(Tup): #Tup. er Last Porjonto..
    if(Tup[idx] == X): #Find Number.
        print("Found:=>",X)
        print("Index is:=>",idx)
        break
    idx += 1
else:
    print("Not found")



      #Example..2
tup = (1,2,3,4,5,6,7,8,9,10)
X = 10 #Find the number?
idx = 0
for idx in range(0,len(tup),1):
    if(idx == X):
       print("found:=>",X)
       print("index:=>",idx)
       break
    idx += 1
else:
    print("Not found!!")