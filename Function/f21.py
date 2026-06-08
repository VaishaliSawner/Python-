x = [1,2,3,4,5,6,7,8,9,10]

result = list(filter(lambda n: not n%2,x))

print(result) # even

result = list(filter(lambda n: n%2, x))
print(result) # odd