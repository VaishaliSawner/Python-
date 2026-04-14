a=int(input("Enter the a"))
b=int(input("Enter the b"))
c=int(input("Enter the c"))

if(a==b and a==c):
    print("Equaliteral Triangle")
elif(a!=b and a==c or a==b and a!=c):
    print("Isosceles Triangle")
else:
    print("Scalence triangle")