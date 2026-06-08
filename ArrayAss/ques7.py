# Binary search 

arr =[10,20,30,40,50,60,70]
key=int(input("Enter element to search"))

low=0
high=len(arr) -1


while low <= high:
    mid = (low+high) // 2

    if arr[mid] == key:
        print("Found at index",mid)
        break
    elif arr[mid]<key:
        low = mid +1
    else:
        high = mid-1

else:
    print("Not found ")
