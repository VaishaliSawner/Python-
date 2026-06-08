"""3. Online Shopping Cart
Problem
Create a shopping cart system.
Requirements
A cart should:
store customer name
maintain list of products
maintain total bill
Functionalities
Add product
Remove product
Calculate final amount
Apply discount using static method
Track total carts created
Concepts Practiced
list inside object
object interaction
static method
class variable"""

class Cart:
    count = 0
    def __init__(self,cus_name):
        self.__cus_name = cus_name
        self.__product_list = []
        self.total_bill = 0

    def add_product(self,product):
        self.__product_list.append(product)
        print(self.__product_list)
    def remove_product(self,product):
        for i in range(len(self.__product_list)):
            if product == self.__product_list[i][0]:
                self.__product_list.remove(self.__product_list[i])
        print(self.__product_list)
obj = Cart("Sanjana")
obj.add_product(["Mobile",5000])
obj.add_product(["Charger",100])
obj.add_product(["Earbuds",1000])

obj.remove_product("Charger")