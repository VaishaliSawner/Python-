a=int(input("Enter the a "))
b=int(input("Enter the b "))
c=int(input("Enter the c "))
d=int(input("Enter the d "))

if(a<b and a<c and a<d):
    print("a is smaller")
elif(b<a and b<c and b<d):
    print("b is smaller")
elif(c<a and c<b and c<d):
    print("c is smaller")
else:
    print("d is smaller ")