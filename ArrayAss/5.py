arr = [7, 10, 4, 3, 20, 15]
k = 3

# sort (bubble)
n = len(arr)
for i in range(n):
    for j in range(0, n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print("Kth smallest:", arr[k-1])
print("Kth largest:", arr[n-k])