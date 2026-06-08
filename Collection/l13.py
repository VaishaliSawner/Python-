lst = [1,2,3,2,5,6,7,2,3,4,5,8,9]
element = 99
counter = 0
for item in lst:
    if element == item:
     counter += 1
print(f"Element found {counter} times" if counter else "Element not found")     