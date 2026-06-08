class FoodItem:
    def __init__(self,name,price,quantity):
        self.__name=name
        self.__price=price
        self.__quantity=quantity


    def getprice(self):
        return self.__price
    
    def getquantity(self):
        return self.__quantity
    


class Burger(FoodItem):
    def totalbill(self):
        total=self.getprice() *self.getquantity()
        print("Total bill for Burger is ",total)

class Pizza(FoodItem):
    def totalbill(self):
        total=self.getprice() *self.getquantity()
        print("Total bill for Pizza is",total)

class Sandwich(FoodItem):
    def totalbill(self):
        total =self.getprice() *self.getquantity()
        print("Total bill for Sandwich is ",total)


b=Burger("VegBurger",100,2)
b.totalbill()

p=Pizza("CheezePizza",200,3)
p.totalbill()

s=Sandwich("VegSandwich",150,1)
s.totalbill()




