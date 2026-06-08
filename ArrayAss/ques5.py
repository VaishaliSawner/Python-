
#Replace muiltple of 5 with 0

arr=[10,2,20,7]
print("Old array",arr)

for i in range(len(arr)):
    if arr[i] %5 ==0:
        arr[i]=0

print("Updated array:",arr)
