lst = [1,2,3,4,10,12,15,7,8,9]

low = 0
high = len(lst) - 1
print(lst)
while low < high:
    lst[low],lst[high] = lst[high],lst[low]
    low += 1
    high -= 1

print(lst)