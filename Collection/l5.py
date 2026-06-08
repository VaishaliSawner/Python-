lst = [1,2,3,4,5,2,2,5,5,6,6,7]

result = {}

for element in lst:
    if element in result:
        result[element] += 1
    else:
        result[element] = 1    
print(result)        