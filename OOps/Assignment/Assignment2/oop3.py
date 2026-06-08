class Product:
    def __init__(self, id, name, price):
        self.__id = id
        self.__name = name
        self.__price = price


    def get_price(self):
        return self.__price
    
    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name


class Cart:
    __counter=0
    def __init__(self,name):
        self.__customer_name = name
        self.__products = []
        self.__bill_amount =0

    def get_bill_amount(self):
        return self.__bill_amount
    
    def add_product(self,p):
        self.__bill_amount = self.__bill_amount + p.get_price()
        self.__products.append(p)

    


    def display(self):
        print("Customer Name:",self.__customer_name)
        print("="*50)
        for product in self.__products:
            print(f"Product ID:{product.get_id()}: {product.get_name()}: {product.get_price()}")
            print(f"Bill Amount: {self.__bill_amount}")

        

    @staticmethod
    def final_amount(bill_amount,discount):
        return bill_amount - (bill_amount*discount/100)
    
    
    def remove(self,id):
        for product in self.__products:
            if product.get_id()==id:
                self.__products.remove(product)
                self.__bill_amount -= product.get_price()
                break
            else:
                print(f"Product not found..")
            print(f"Product removed successfully")

    
p1=Product(101,"Laptop",50000)
p2=Product(102,"Mobile",20000)
p3=Product(103,"Headphones",100)

c1 = Cart("Atul")
c1.add_product(p1)
c1.add_product(p2)
c1.add_product(p3)
c1.display()
c1.remove(100)

c1.display()
print(f"After Discount :{Cart.final_amount(c1.get_bill_amount(),10)}")
