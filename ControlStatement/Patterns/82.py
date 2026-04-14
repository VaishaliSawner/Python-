
'''

A
AB
A C
A  D
ABCDE

'''

for i in range(6):
    for j in range(1,i+1):
        if(i==5 or j==1 or i==j):
            print(chr(j+64),end="")
        else:
            print(" ",end="")
    print()