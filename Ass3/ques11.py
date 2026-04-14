age = int(input("Enter age: "))
sex = input("Enter sex (M/F): ")
marital = input("Marital status (Y/N): ")

if sex == "F":
    print("Work location: Urban areas only")

elif sex == "M" and 20 <= age <= 40:
    print("Work anywhere")

elif sex == "M" and 40 < age <= 60:
    print("Urban areas only")

else:
    print("ERROR")