lst = [10,20,30,40,50]
position = int(input("Enter position : "))
n = len(lst)
lst.append(None)
print(f"Before inserting : {lst}")
if position > 0 and position <= len(lst):
    element = int(input("Enter element : "))
    for i in range(n-1,position-2,-1):
        lst[i+1] = lst[i]
    else:
        lst[position-1] = element
    print(f"After inserting : {lst}")    
else:
    print("Invalid position")