held = int(input("Classes held: "))
attended = int(input("Classes attended: "))
medical = input("Medical cause? (Y/N): ")

percentage = (attended / held) * 100
print("Attendance:", percentage)

if percentage >= 75 or medical == "Y":
    print("Allowed")
else:
    print("Not allowed")