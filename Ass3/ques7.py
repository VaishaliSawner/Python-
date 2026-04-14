held = int(input("Classes held: "))
attended = int(input("Classes attended: "))

percentage = (attended / held) * 100
print("Attendance:", percentage)

if percentage >= 75:
    print("Allowed")
else:
    print("Not allowed")