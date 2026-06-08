# Delete Element 
arr = [10, 20, 30, 40, 50]

pos = int(input("Enter position to delete: "))                               

new_arr = []

for i in range(len(arr)):
    if i != pos:
        new_arr.append(arr[i])

print("New array:", new_arr)



'''
arr = [1, 2, 3, 4, 5]

pos = int(input("Enter position to delete: "))


for i in range(pos, len(arr) - 1):
    arr[i] = arr[i + 1]


arr.pop()

print("Array after deletion:", arr)
'''

