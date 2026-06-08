'''
1	2	2	4	8	32	…… n terms

===> 0 1 1 2 3 5 8 13....n terms
'''

n = int(input("Enter number of terms : "))

a = -1
b = 1

for i in range(n):
    c = a + b
    print(c,end=",")
    a,b = b,c