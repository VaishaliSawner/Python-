
'''
123456
54321
1234
321
12
1

'''
count=6

for i in range(6,0,-1):
    for j in range(1,i+1):
        if i%2==0:
            print(j,end="")
        else:
            count=count-1
            print(count,end="")
    count=i
    print()