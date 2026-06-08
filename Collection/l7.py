lst = [10,20,30,40,50]
position = int(input("Enter position : "))
n = len(lst)

print(f"Before deletion : {lst}")

if position>0 and position<=n:
    for i in range(position-1,n-1):
        lst[i] = lst[i+1]
    else:
        lst.pop()

print(f"After deletion : {lst}")    