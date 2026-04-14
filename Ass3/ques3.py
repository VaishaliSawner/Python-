salary = float(input("Enter salary: "))
years = int(input("Enter years of service: "))

if years > 5:
    bonus = salary * 5/100   # 5% discount
else:
    bonus = 0

print("Bonus amount:", bonus)