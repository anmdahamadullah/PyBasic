"""
>>> Q3:Create a class called order which stores item & its price.
Use Dander Function_ _ _gt(Greaterthen)_ _() to  convey that:
order1 > order2 if price of order1 > price of order2."""

class Order: #class
    def __init__(self,item,price):#obj Value Store, Function.
        self.item = item 
        self.price = price

    def __gt__(self,odr2): #Dander Function.Logic create
        return self.price > odr2.price 

odr1 = Order("Chips",20) 
odr2 = Order("Tea",15)     
print(odr1 > odr2)


