

#Enter n element in array and print array 
n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

print("Array is:", arr)