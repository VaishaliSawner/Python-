quantity=int(input("Enter the quantity"))

per_UnitCost = 100
Total_Cost=quantity*per_UnitCost
discount =0 

if(Total_Cost >=1000):
    discount= Total_Cost*(10/100)
print("Discount", discount)

Final_Price = Total_Cost - discount

print(Final_Price)

