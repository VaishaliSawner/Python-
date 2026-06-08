'''
  Perfect number
'''
n = int(input("Enter a number : "))

sum = 0
for i in range(1,(n//2)+1):
    if not n%i:
        sum += i
if sum == n:
    print(f"{n} is perfect number")
else:
    print(f"{n} is not perfect number")    