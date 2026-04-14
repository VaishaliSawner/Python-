selling_Price=int(input("Enter the selling Price"))
cost_Price=int(input("Enter the cost Price"))
Profit=selling_Price-cost_Price
Loss=cost_Price-selling_Price

if(selling_Price > cost_Price):
    print(Profit)
else:
    print(Loss)