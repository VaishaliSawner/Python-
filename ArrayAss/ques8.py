# Insert element 

arr = [1, 2, 3, 4, 5]
print(arr)

pos = int(input("Enter position: "))
val = int(input("Enter value: "))


arr.append(0)


for i in range(len(arr) - 1, pos, -1):
    arr[i] = arr[i - 1]


arr[pos] = val

print("Array after insertion:", arr)






'''
arr = [10, 20, 30, 40, 50]

pos = int(input("Enter position: "))
element = int(input("Enter element: "))

new_arr = []

for i in range(len(arr) + 1):
    if i < pos:
        new_arr.append(arr[i])
    elif i == pos:
        new_arr.append(element)
    else:
        new_arr.append(arr[i-1])

print("New array:", new_arr)

'''

