price = float(input("Enter cost price: "))

if price > 100000:
    tax = price * 15/100
elif price > 50000:
    tax = price * 10/100
else:
    tax = price * 5/100

print("Tax to be paid:", tax)