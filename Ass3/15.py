year=int(input("Enter the year"))

result= "Leap year" if(year%4==0 and year%100!=0 or year%400==0) else "Not Leap year"

print(result)


