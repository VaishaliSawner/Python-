'''
1	2	2	4	8	32	…… n terms

'''

n = int(input("Enter number of terms : "))
a,b = 1,2
if n >=2:
    print(a,end=" ")
    print(b, end=" ")
    for i in range(n-2):
     print(a*b,end=" ")
     a,b = b,a*b
else:
   print("Terms must be greter then or equals to 2")