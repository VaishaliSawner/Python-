

'''
1
10
1 1
1  0
1   1
101010

'''




n=6

for i in range(1, n+1):
    for j in range(1, i+1):
        
        if i == n:
            if j % 2 == 0:
                print("0", end="")
            else:
                print("1", end="")
        
        elif j == 1:
            print("1", end="")
        
        elif j == i:
            if i % 2 == 0:
                print("0", end="")
            else:
                print("1", end="")
        
        else:
            print(" ", end="")
    
    print()   
