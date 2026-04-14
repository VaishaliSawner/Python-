year=int(input("Enter the year"))

leap_year = "Leap year" if (year%4==0 and year%100!=0 or year%400==0) else "Not a Leap year"

print(leap_year)