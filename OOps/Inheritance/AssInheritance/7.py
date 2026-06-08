class Product:
    def discount(self,price):
        pass

class Electronics(Product):
    def discount(self,price):
        print("Discounted price is ",price-(price*10/100))

class Clothing(Product):
    def discount(self,price):
        print("Discounted price is ",price-(price*20/100))


class Grocery(Product):
    def discount(self,price):
        print("Discounted price is ",price-(price*5/100))

e = Electronics()
e.discount(1000)

c=Clothing()
c.discount(2000)

g=Grocery()
g.discount(500)

