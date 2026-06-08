'''
 COUNT Occurence 
arr = [10, 20, 10, 30, 20, 10]

visited = []

for i in range(len(arr)):
    if arr[i] in visited:
        continue

    count = 1

    for j in range(i+1, len(arr)):
        if arr[i] == arr[j]:
            count += 1

    print(arr[i], ":", count)
    visited.append(arr[i])
    '''


arr = [1,2,3,4,5,4,6,2,1]
count = {}

for i in arr:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

print(count)