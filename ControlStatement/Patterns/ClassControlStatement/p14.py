row  = int(input("Enter row number : "))
if row >= 5 and row%2:
    for i in range(1,row+1):
        for j in range(1,row+1):
            if j==1 or j == row or i == 1 or i == row or (i+j == row + 1) or i == j:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()        